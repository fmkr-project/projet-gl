from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Projet,Tache,Commentaire
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

@login_required
def detail_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)

    if request.method == 'POST':
        contenu = request.POST.get('contenu')
        if contenu:
            Commentaire.objects.create(tache=tache, auteur=request.user, contenu=contenu)
            return HttpResponseRedirect(reverse('detail_tache', args=[tache_id]))

    return render(request, 'gestion_projets/detail_tache.html', {'tache': tache})

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

def changer_statut_tache(request, tache_id, nouveau_statut):
    # Récupérer la tâche avec l'ID
    tache = get_object_or_404(Tache, id=tache_id)

    # Liste des statuts valides
    statuts_valides = ['a_faire', 'en_cours', 'termine']

    if nouveau_statut in statuts_valides:
        tache.statut = nouveau_statut
        tache.save()

    # Rediriger vers une autre page (par exemple, la page du projet)
    return redirect('detail_projet', projet_id=tache.projet.id)


@login_required
def modifier_commentaire(request, commentaire_id):
    commentaire = get_object_or_404(Commentaire, id=commentaire_id)

    # Vérifiez si l'utilisateur est l'auteur du commentaire
    if request.user != commentaire.auteur:
        return redirect('detail_tache', tache_id=commentaire.tache.id)

    if request.method == 'POST':
        contenu = request.POST.get('contenu')
        if contenu:
            commentaire.contenu = contenu
            commentaire.save()
            return redirect('detail_tache', tache_id=commentaire.tache.id)

    return render(request, 'gestion_projets/modifier_commentaire.html', {'commentaire': commentaire})

@login_required
def supprimer_commentaire(request, commentaire_id):
    commentaire = get_object_or_404(Commentaire, id=commentaire_id)

    # Vérifiez que seul l'auteur peut supprimer
    if request.user == commentaire.auteur:
        tache_id = commentaire.tache.id  # Stockez l'ID de la tâche avant suppression
        commentaire.delete()
        return redirect('detail_tache', tache_id=tache_id)

    # Si l'utilisateur n'est pas l'auteur, redirigez simplement
    return redirect('detail_tache', tache_id=commentaire.tache.id)
