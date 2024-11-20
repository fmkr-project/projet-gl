from django.db import models
from django.contrib.auth.models import User

class Projet(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()

    membres = models.ManyToManyField(User, related_name='projets')


    def __str__(self):
        return self.nom

class Tache(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    statut = models.CharField(
        max_length=20,
        choices=[
            ('a_faire', 'À faire'),
            ('en_cours', 'En cours'),
            ('termine', 'Terminé'),
        ],
        default='a_faire'
    )
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="taches")

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    tache = models.ForeignKey('Tache', on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)  # Date de création
    date_modification = models.DateTimeField(auto_now=True)  # Date de dernière modification

    def __str__(self):
        return f"{self.auteur.username}: {self.contenu[:30]}"