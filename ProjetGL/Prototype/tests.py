from django.conf import settings
from django.contrib.auth.models import User, Group
from django.urls import reverse

from Prototype.forms import checkName, checkMail, checkPW, checkPW_Confirm, SignUpForm
from django.test import TestCase
from Prototype.models import *


class SignUpFormTests(TestCase):

    def test_check_name_unique(self):
        #Pour l'unicité
        User.objects.create_user(username='testuser', email='test@example.com', password='password123')

        self.assertEqual(checkName('testuser'), "Ce nom d'utilisateur est déjà pris.")
        self.assertEqual(checkName('1testuser'), "Le nom d'utilisateur ne peut pas commencer par un chiffre.")
        self.assertEqual(checkName('newtestuser'), "")

    def test_check_email_unique(self):
        #Pour l'unicité
        User.objects.create_user(username='testuser2', email='test@example.com', password='password123')

        self.assertEqual(checkMail('test@example.com'), "Cette adresse email est déjà utilisée.")
        self.assertEqual(checkMail('newemail@example.com'), "")  # Email valide

    def test_check_password_length(self):
        self.assertEqual(checkPW('short'), "Le mot de passe doit contenir au moins 8 caractères.")
        self.assertEqual(checkPW('validPW123!'), "")  # Mot de passe valide

    def test_check_password_confirmation(self):
        self.assertEqual(checkPW_Confirm('password123', 'password1234'), "Les mots de passe ne correspondent pas.")
        self.assertEqual(checkPW_Confirm('password123', 'password123'), "")  # Mots de passe valides

    def test_signup_form_valid(self):
        form_data = {
            'username': 'user',
            'email': 'user@example.com',
            'password1': 'ValidPW12345!',
            'password2': 'ValidPW12345!',
            'is_chef_projet': False
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())  # Le formulaire doit être valide

    def test_signup_form_invalid_password(self):
        form_data = {
            'username': 'user',
            'email': 'user@example.com',
            'password1': 'shortPW',
            'password2': 'shortPW',
            'is_chef_projet': False
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_signup_form_invalid_username_taken(self):
        User.objects.create_user(username='userExist', email='existe@example.com', password='password123')

        form_data = {
            'username': 'userExist',
            'email': 'newuser@example.com',
            'password1': 'ValidPW12345!',
            'password2': 'ValidPW12345!',
            'is_chef_projet': False
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)


class ProjetModelTest(TestCase):

    def setUp(self):
        # Crée un utilisateur pour tester
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

        # Crée un projet pour tester
        self.projet = Projet.objects.create(
            nom="Test Projet",
            description="Ceci est un projet de test.",
            date_debut="2024-01-01",
            date_fin="2024-12-31"
        )
        self.projet.membres.add(self.user)

    def test_projet_str(self):
        """Teste la représentation en chaîne (__str__) du modèle Projet"""
        self.assertEqual(str(self.projet), "Test Projet")

    def test_projet_membres(self):
        """Teste si l'utilisateur est bien ajouté au projet"""
        self.assertIn(self.user, self.projet.membres.all())

class ModifierProjetViewTest(TestCase):

    def setUp(self):
        # Créer un utilisateur chef de projet
        self.user = User.objects.create_user(username='chef', password='password123')
        group = Group.objects.create(name='chef_projets')
        self.user.groups.add(group)

        # Connecter l'utilisateur
        self.client.login(username='chef', password='password123')

        # Créer un projet pour le test
        self.projet = Projet.objects.create(
            nom="Projet Test",
            description="Description de test",
            date_debut="2024-01-01",
            date_fin="2024-12-31"
        )

    def test_modifier_projet_get(self):
        """Teste que la page de modification du projet s'affiche correctement"""
        response = self.client.get(reverse('modifier_projet', args=[self.projet.id]))
        self.assertEqual(response.status_code, 200)  # Vérifie que la réponse est OK
        self.assertTemplateUsed(response, 'gestion_projets/modifier_projet.html')  # Vérifie le bon template

    def test_modifier_projet_post(self):
        """Teste que les modifications du projet sont bien sauvegardées"""
        response = self.client.post(
            reverse('modifier_projet', args=[self.projet.id]),
            {'nom': 'Projet Modifié', 'description': 'Description mise à jour'}
        )
        self.projet.refresh_from_db()  # Recharge les données depuis la base
        self.assertEqual(self.projet.nom, 'Projet Modifié')
        self.assertEqual(self.projet.description, 'Description mise à jour')
        self.assertRedirects(response, reverse('page_chef_projets'))  # Vérifie la redirection

class SupprimerProjetViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='chef', password='password123')
        group = Group.objects.create(name='chef_projets')
        self.user.groups.add(group)

        self.client.login(username='chef', password='password123')

        self.projet = Projet.objects.create(
            nom="Projet Test",
            description="Description de test",
            date_debut="2024-01-01",
            date_fin="2024-12-31"
        )

    def test_supprimer_projet_post(self):
        """Teste que le projet est supprimé via POST"""
        response = self.client.post(reverse('supprimer_projet', args=[self.projet.id]))
        self.assertEqual(Projet.objects.count(), 0)  # Le projet doit être supprimé
        self.assertRedirects(response, reverse('page_chef_projets'))  # Vérifie la redirection

class AccessRestrictionTest(TestCase):

    def setUp(self):
        # Utilisateur chef de projet
        self.chef = User.objects.create_user(username='chef', password='password123')
        chef_group = Group.objects.create(name='chef_projets')
        self.chef.groups.add(chef_group)

        # Utilisateur normal
        self.user = User.objects.create_user(username='user', password='password123')

        # Projet
        self.projet = Projet.objects.create(
            nom="Projet Test",
            description="Description de test",
            date_debut="2024-01-01",
            date_fin="2024-12-31"
        )

    def test_access_granted_to_chef_projets(self):
        """Teste que les chefs de projet ont accès à la vue de modification"""
        self.client.login(username='chef', password='password123')
        response = self.client.get(reverse('modifier_projet', args=[self.projet.id]))
        self.assertEqual(response.status_code, 200)  # Accès autorisé

    def test_access_denied_to_non_chef_projets(self):
        """Teste que les utilisateurs non chefs de projet sont redirigés vers la page de connexion"""
        self.client.login(username='user', password='password123')
        response = self.client.get(reverse('modifier_projet', args=[self.projet.id]))
        self.assertEqual(response.status_code, 302)  # Vérifie qu'il y a une redirection
        self.assertRedirects(
            response,
            f"{settings.LOGIN_URL}?next={reverse('modifier_projet', args=[self.projet.id])}"
        )