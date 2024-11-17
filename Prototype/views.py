from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projet,Tache



@login_required
def liste_projets(request):
    projets = Projet.objects.all()
    taches = Projet.objects.all()
    return render(request, 'gestion_projets/liste_projets.html', {'projets': projets, 'tache': taches})


@login_required
def detail_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    taches = projet.taches.all()  # Utilise `related_name` pour accéder aux tâches
    return render(request, 'gestion_projets/detail_projet.html', {'projet': projet, 'taches': taches})

def login(request):
    return render(request, 'login.html')


@login_required
def index(request):

    projet = Projet.objects.all()
    # Regrouper les tâches par statut
    taches_a_faire = Tache.objects.filter(statut='a_faire')
    taches_en_cours = Tache.objects.filter(statut='en_cours')
    taches_terminees = Tache.objects.filter(statut='termine')

    return render(request, 'gestion_projets/index.html', {
        'projet': projet,
        'taches_a_faire': taches_a_faire,
        'taches_en_cours': taches_en_cours,
        'taches_terminees': taches_terminees,
    })