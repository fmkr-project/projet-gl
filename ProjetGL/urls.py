"""
URL configuration for ProjetGL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Prototype import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # URL de l'accueil
    path('projets/', views.liste_projets, name='liste_projets'),
    path('projets/<int:projet_id>/', views.detail_projet, name='detail_projet'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mes_projets/<int:user_id>/', views.mes_projets, name='mes_projets'),
    path('taches/delete/<int:tache_id>/',views.supprimer_tache,name='supprimer_tache'),
    path('tache/<int:tache_id>/', views.detail_tache, name='detail_tache'),
    path('tache/<int:tache_id>/changer-statut/<str:nouveau_statut>/', views.changer_statut_tache, name='changer_statut_tache'),
    path('commentaire/<int:commentaire_id>/modifier/', views.modifier_commentaire, name='modifier_commentaire'),
    path('commentaire/<int:commentaire_id>/supprimer/', views.supprimer_commentaire, name='supprimer_commentaire'),
    path('chefs_projets/', views.page_chef_projets, name='page_chef_projets'),
    path('mes_taches/', views.mes_taches, name='mes_taches'),
    path('projets/creer/', views.creer_projet, name='creer_projet'),
    path('projets/<int:projet_id>/delete/',views.supprimer_projet,name='supprimer_projet'),
    path('projets/<int:projet_id>/edit/', views.modifier_projet, name='modifier_projet'),
    path('projets/<int:projet_id>/add/', views.ajouter_tache, name='ajouter_tache'),
    path('signup/', views.signup, name='signup'),
]