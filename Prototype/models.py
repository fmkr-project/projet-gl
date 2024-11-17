from django.db import models
from django.contrib.auth.models import User

class Projet(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()


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