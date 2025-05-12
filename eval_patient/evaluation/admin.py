# admin.py
from django.contrib import admin
from .models import Patient, ContexteEpidemiologique, SignesVitaux,SymptomesGeneraux, SymptomesRespiratoires, SymptomesDigestifs,SymptomesNeurologiques, SymptomesDermatologiques, SymptomesSpecifiques,DifferenciationMaladie,SymptomesPositifs,MaladieDetectee

admin.site.register(Patient)
admin.site.register(ContexteEpidemiologique)
admin.site.register(SignesVitaux)
admin.site.register(SymptomesGeneraux)
admin.site.register(SymptomesRespiratoires)
admin.site.register(SymptomesDigestifs)

@admin.register(SymptomesNeurologiques)
class SymptomesNeurologiquesAdmin(admin.ModelAdmin):
    list_display = ('patient', 'convulsions', 'raideur_nuque')

@admin.register(SymptomesDermatologiques)
class SymptomesDermatologiquesAdmin(admin.ModelAdmin):
    list_display = ('patient', 'eruption_cutanée', 'lesions_ulceratives')

@admin.register(SymptomesSpecifiques)
class SymptomesSpecifiquesAdmin(admin.ModelAdmin):
    list_display = ('patient', 'ganglions_enflés', 'jaunisse')

class DifferenciationMaladieAdmin(admin.ModelAdmin):
    list_display = ('maladie', 'signes_majeurs', 'contexte_epidemiologique', 'examens_cles')
    search_fields = ('maladie', 'signes_majeurs', 'contexte_epidemiologique')
    list_filter = ('maladie',)
    ordering = ('maladie',)

admin.site.register(DifferenciationMaladie, DifferenciationMaladieAdmin)


@admin.register(SymptomesPositifs)
class SymptomesPositifsAdmin(admin.ModelAdmin):
    list_display = ('patient', 'symptome_type', 'symptome_nom')
    search_fields = ('patient__nom', 'symptome_nom')

class MaladieDetecteeAdmin(admin.ModelAdmin):
    # Spécifiez les champs à afficher dans la liste des objets
    list_display = ('patient', 'maladie', 'signes_majeurs', 'contexte_epidemiologique', 'examens_cles', 'date_detection')
    
    # Ajouter des filtres pour faciliter la recherche
    list_filter = ('patient', 'maladie', 'date_detection')
    
    # Permettre des recherches par certains champs
    search_fields = ('patient__nom', 'maladie', 'signes_majeurs')
    
    # Permettre de trier par date
    ordering = ('-date_detection',)

    # Ajouter un champ pour un affichage personnalisé dans l'interface d'administration
    def __str__(self):
        return f"Maladie détectée: {self.maladie} pour {self.patient.nom}"

# Enregistrer le modèle et la classe d'administration
admin.site.register(MaladieDetectee, MaladieDetecteeAdmin)
