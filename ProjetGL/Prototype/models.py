from django.db import models
from django.db.models import F, Q, Count
from django.contrib.auth.models import User

class Projet(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    '''
    fini = models.GeneratedField(
        expression=Count("tache"),
        output_field=models.IntegerField(),
        db_persist=True
    )

    nbtaches = models.GeneratedField(
        expression=Count("tache", filter=Q(projet=nom)),
        output_field=models.IntegerField(),
        db_persist=True
    )
    '''
    def __str__(self):
        return self.nom

class Tache(models.Model):
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
