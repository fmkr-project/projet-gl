from django.shortcuts import render, get_object_or_404
from .models import Projet

def liste_projets(request):
    projets = Projet.objects.all()
    taches = Projet.objects.all()
    return render(request, 'gestion_projets/liste_projets.html', {'projets': projets, 'tache': taches})

def detail_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    taches = projet.taches.all()  # Utilise `related_name` pour accéder aux tâches
    return render(request, 'gestion_projets/detail_projet.html', {'projet': projet, 'taches': taches})
