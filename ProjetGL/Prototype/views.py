from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User,Group
from django.urls import reverse


from .models import Projet,Tache,Commentaire
from .forms import TacheForm, SignUpForm


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
def mes_taches(request):
    # Filtrer toutes les tâches attribuées à l'utilisateur connecté
    taches_a_faire = Tache.objects.filter(statut='a_faire', responsable=request.user)
    taches_en_cours = Tache.objects.filter(statut='en_cours', responsable=request.user)
    taches_termine = Tache.objects.filter(statut='termine', responsable=request.user)

    return render(request, 'gestion_projets/mes_taches.html', {
        'taches_a_faire': taches_a_faire,
        'taches_en_cours': taches_en_cours,
        'taches_termine': taches_termine,
    })

@login_required
def detail_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    taches = projet.taches.all()  # Utilise `related_name` pour accéder aux tâches

    return render(request, 'gestion_projets/detail_projet.html', {'projet': projet, 'taches': taches})

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
    # Récupérer tous les projets
    projets = Projet.objects.all()

    # Si un projet est sélectionné, filtrez les tâches par projet
    selected_projet_id = request.GET.get('projet')
    if selected_projet_id:
        selected_projet = get_object_or_404(Projet, id=selected_projet_id)
        taches_a_faire = selected_projet.taches.filter(statut='a_faire')
        taches_en_cours = selected_projet.taches.filter(statut='en_cours')
        taches_termine = selected_projet.taches.filter(statut='termine')
    else:
        selected_projet = None
        taches_a_faire = Tache.objects.filter(statut='a_faire')
        taches_en_cours = Tache.objects.filter(statut='en_cours')
        taches_termine = Tache.objects.filter(statut='termine')

    return render(request, 'gestion_projets/index.html', {
        'projets': projets,
        'selected_projet': selected_projet,
        'taches_a_faire': taches_a_faire,
        'taches_en_cours': taches_en_cours,
        'taches_termine': taches_termine,
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


# Vérification que l'utilisateur appartient au groupe chef_projets
def est_chef_projet(user):
    return user.groups.filter(name='chef_projets').exists()


@login_required
@user_passes_test(est_chef_projet)  # Vérifie si l'utilisateur est un chef de projet
def page_chef_projets(request):
    # Filtrer les chefs de projets
    projets = Projet.objects.all()
    chefs_projets = Group.objects.get(name='chef_projets').user_set.all()
    return render(request, 'gestion_projets/page_chef_projets.html', {'chefs_projets': chefs_projets,'projets' : projets})


@login_required
@user_passes_test(est_chef_projet)  # Assurez-vous que seul un chef de projet peut ajouter des projets
def creer_projet(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')

        # Créer le projet
        projet = Projet.objects.create(
            nom=nom,
            description=description,
            date_debut=date_debut,
            date_fin=date_fin
        )

        # Assignation des membres au projet
        membres = request.POST.getlist('membres')  # Liste d'IDs d'utilisateurs sélectionnés
        for membre_id in membres:
            utilisateur = User.objects.get(id=membre_id)
            projet.membres.add(utilisateur)

        return redirect('page_chef_projets')  # Redirige vers la page des chefs de projet
    else:
        utilisateurs = User.objects.all()  # Récupérer tous les utilisateurs
        return render(request, 'gestion_projets/creer_projet.html', {'utilisateurs': utilisateurs})


@login_required
@user_passes_test(est_chef_projet)  # Assurez-vous que seul un chef de projet peut attribuer des tâches
def ajouter_tache(request, projet_id):
    # Récupérer le projet
    projet = get_object_or_404(Projet, id=projet_id)
    taches = projet.taches.all()  # Utilise `related_name` pour accéder aux tâches
    users = User.objects.all()

    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save(commit=False)
            tache.projet = projet
            tache.save()
            return redirect('detail_projet', projet_id=projet.id)
    else:
        form = TacheForm()
        # Rendre le formulaire d'ajout de tâche
    return render(request, 'gestion_projets/ajouter_tache.html', {'projet': projet, 'taches': taches, 'form' : form})

@login_required
@user_passes_test(est_chef_projet)
def supprimer_projet(request, projet_id):
        projet = get_object_or_404(Projet, id=projet_id)
        projet.delete()
        return redirect('page_chef_projets')

@login_required
@user_passes_test(est_chef_projet)
def modifier_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    membres = projet.membres.all()  # Utilisateurs assignés au projet
    taches = projet.taches.all()   # Tâches associées au projet

    if request.method == 'POST':
        # Mettre à jour les informations du projet
        projet.nom = request.POST.get('nom')
        projet.description = request.POST.get('description')
        projet.save()

        # Mettre à jour les tâches
        for tache in taches:
            tache_titre = request.POST.get(f"titre_{tache.id}")
            tache_statut = request.POST.get(f"statut_{tache.id}")
            tache_responsable_id = request.POST.get(f"responsable_{tache.id}")

            if tache_titre:
                tache.titre = tache_titre
            if tache_statut:
                tache.statut = tache_statut
            if tache_responsable_id:
                responsable = User.objects.filter(id=tache_responsable_id).first()
                tache.responsable = responsable

            tache.save()

        return redirect('page_chef_projets')  # Rediriger après la sauvegarde

    return render(request, 'gestion_projets/modifier_projet.html', {
        'projet': projet,
        'taches': taches,
        'membres': membres,
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.save()

            if form.cleaned_data.get('is_chef_projet'):
                group, created = Group.objects.get_or_create(name='chef_projets')
            else :
                group, created = Group.objects.get_or_create(name='dev')

            group.user_set.add(user)

            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
@user_passes_test(est_chef_projet)
def visualiser_avancement(request, projet_id):
    # Récupérer le projet
    projet = get_object_or_404(Projet, id=projet_id)

    # Récupérer les tâches associées au projet
    taches = projet.taches.all()

    # Calculer l'avancement
    total_taches = taches.count()
    taches_terminees = taches.filter(statut='termine').count()

    avancement = (taches_terminees / total_taches * 100) if total_taches > 0 else 0

    return render(request, 'gestion_projets/avancement_projet.html', {
        'projet': projet,
        'taches': taches,
        'avancement': avancement
    })
