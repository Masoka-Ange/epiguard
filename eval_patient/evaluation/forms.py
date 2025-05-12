# forms.py
from django import forms
from .models import Patient, ContexteEpidemiologique, SignesVitaux, SymptomesGeneraux, SymptomesRespiratoires, SymptomesDigestifs,SymptomesNeurologiques, SymptomesDermatologiques, SymptomesSpecifiques,DifferenciationMaladie
from django import forms
from .models import Province, Hopital, Medecin

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class ContexteEpidemiologiqueForm(forms.ModelForm):
    class Meta:
        model = ContexteEpidemiologique
        fields = '__all__'
        widgets = {
            'voyages_recents': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'contact_avec_malades': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'epidemie_locale': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'patient': forms.HiddenInput()  # Masquer le champ patient
        }
class SignesVitauxForm(forms.ModelForm):
    class Meta:
        model = SignesVitaux
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput()  # Masquer le champ patient
        }

class SymptomesGenerauxForm(forms.ModelForm):
    class Meta:
        model = SymptomesGeneraux
        fields = '__all__'
        widgets = {
            'fievre': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'fatigue': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'sueurs_nocturnes': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'perte_poids_inexplique': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'myalgies': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'arthralgies': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'cephalees': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'patient': forms.HiddenInput()  # Masquer le champ patient
        }

class SymptomesRespiratoiresForm(forms.ModelForm):
    class Meta:
        model = SymptomesRespiratoires
        fields = '__all__'
        
        widgets = {
            'toux': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'dyspnée (Difficulté respiratoire )': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'douleur_thoracique': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'congestion_nasale': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'patient': forms.HiddenInput()  # Masquer le champ patient
        }

class SymptomesDigestifsForm(forms.ModelForm):
    class Meta:
        model = SymptomesDigestifs
        fields = '__all__'
        widgets = {
            'diarrhee': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'vomissements': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'douleurs_abdominales': forms.RadioSelect(choices=[(True, 'Oui'), (False, 'Non')]),
            'patient': forms.HiddenInput()  # Masquer le champ patient
        }

class SymptomesNeurologiquesForm(forms.ModelForm):
    class Meta:
        model = SymptomesNeurologiques
        fields = '__all__'
        widgets = {
            'convulsions': forms.RadioSelect(choices=[(True, "Oui"), (False, "Non")]),
            'raideur_nuque': forms.RadioSelect(choices=[(True, "Oui"), (False, "Non")]),
            'paralysie_flasque_aiguë': forms.RadioSelect(choices=[(True, "Oui"), (False, "Non")]),
            'troubles_conscience': forms.RadioSelect(choices=[(True, "Oui"), (False, "Non")]),
            'vertiges': forms.RadioSelect(choices=[(True, "Oui"), (False, "Non")]),
            'patient': forms.HiddenInput()  # Masquer le champ patient
        }

class SymptomesDermatologiquesForm(forms.ModelForm):
    class Meta:
        model = SymptomesDermatologiques
        fields = '__all__'
        widgets = {
            'eruption_cutanée (préciser l’aspect : macules, papules, vésicules, etc.)': forms.RadioSelect(choices=[(True, "Oui"), (False, "Non")]),
            'lesions_ulceratives': forms.RadioSelect(choices=[(True, "Oui"), (False, "Non")]),
            'saignement_cutane': forms.RadioSelect(choices=[(True, "Oui"), (False, "Non")]),
            'patient': forms.HiddenInput()  # Masquer le champ patient
        }

class SymptomesSpecifiquesForm(forms.ModelForm):
    class Meta:
        model = SymptomesSpecifiques
        fields = '__all__'
        widgets = {
            'ganglions_enflés': forms.RadioSelect(choices=[(True, "Oui"), (False, "Non")]),
            'jaunisse (ictère)': forms.RadioSelect(choices=[(True, "Oui"), (False, "Non")]),
            'douleurs_oculaires': forms.RadioSelect(choices=[(True, "Oui"), (False, "Non")]),
            'patient': forms.HiddenInput()  # Masquer le champ patient
        }

class DifferenciationMaladieForm(forms.ModelForm):
    class Meta:
        model = DifferenciationMaladie
        fields = ['maladie', 'signes_majeurs', 'contexte_epidemiologique', 'examens_cles']
        widgets = {
            'maladie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la maladie'}),
            'signes_majeurs': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Signes majeurs'}),
            'contexte_epidemiologique': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contexte épidémiologique'}),
            'examens_cles': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Examens clés'}),
        }


class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = ['name']


class HopitalForm(forms.ModelForm):
    class Meta:
        model = Hopital
        fields = ['name', 'address', 'emergency_contact', 'province', 'photo']


class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin  # Assurez-vous que Medecin est votre modèle
        fields = ['name', 'post_nom', 'sexe', 'specialite', 'emergency_contact', 'province', 'hopital']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom du médecin'}),
            'post_nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le post-nom du médecin'}),
            'sexe': forms.Select(attrs={'class': 'form-select'}),
            'specialite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la spécialité'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le contact d\'urgence'}),
            'province': forms.Select(attrs={'class': 'form-select', 'id': 'province_select'}),
            'hopital': forms.Select(attrs={'class': 'form-select', 'id': 'hopital_select'}),
        }
class ProvinceHopitalForm(forms.Form):
    province = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        label="Province",
        widget=forms.Select(attrs={'onchange': 'fetchHopitals()'}),
    )
    hopital = forms.ModelChoiceField(
        queryset=Hopital.objects.none(),
        label="Hôpital",
        widget=forms.Select(attrs={'id': 'hopital-select'}),
    )
    matricule = forms.CharField(
        max_length=100,
        label="Matricule",
        widget=forms.TextInput(attrs={'placeholder': 'Entrez le matricule'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))
                self.fields['hopital'].queryset = Hopital.objects.filter(province_id=province_id)
            except (ValueError, TypeError):
                self.fields['hopital'].queryset = Hopital.objects.none()
        else:
            self.fields['hopital'].queryset = Hopital.objects.none()        