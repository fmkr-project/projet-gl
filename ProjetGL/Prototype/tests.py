from django.contrib.auth.models import User
from Prototype.forms import checkName, checkMail, checkPW, checkPW_Confirm, SignUpForm
from django.test import TestCase

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
