from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Projet,Tache
from django.contrib.auth.models import User
from .forms import TacheForm

@login_required
def liste_projets(request):
    projets = Projet.objects.all()
    taches = Projet.objects.all()
    return render(request, 'gestion_projets/liste_projets.html', {'projets': projets, 'tache': taches})

@login_required
def mes_projets(request,user_id):
    user = get_object_or_404(User, id=user_id)
    projets = user.projets.all()
    return render(request, 'gestion_projets/mes_projets.html', {'projets' : projets})

@login_required
def detail_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    taches = projet.taches.all()  # Utilise `related_name` pour accéder aux tâches

    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save(commit=False)
            tache.projet = projet
            tache.save()
            return redirect('detail_projet', projet_id=projet.id)
    else:
        form = TacheForm()

    return render(request, 'gestion_projets/detail_projet.html', {'projet': projet, 'taches': taches, 'form' : form})

def supprimer_tache(request, tache_id):
    tache = get_object_or_404(Tache, pk=tache_id)
    projet_id = tache.projet.id
    tache.delete()
    return redirect('detail_projet', projet_id=projet_id)


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