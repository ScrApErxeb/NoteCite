from django.contrib import admin
from .models import Service

# Créer un modèle d'administration personnalisé pour les services
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'created_at')  # Champs affichés dans la liste des services
    search_fields = ('name', 'category')  # Recherche par nom et catégorie
    list_filter = ('category',)  # Filtrer par catégorie
    ordering = ('-created_at',)  # Trier par date de création

