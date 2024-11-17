from django.contrib import admin
from .models import Projet, Tache

class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    filter_horizontal = ('membres',)

admin.site.register(Projet,ProjetAdmin)

admin.site.register(Tache)

