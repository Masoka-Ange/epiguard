# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm, ContexteEpidemiologiqueForm, SignesVitauxForm,SymptomesGenerauxForm, SymptomesRespiratoiresForm, SymptomesDigestifsForm,SymptomesNeurologiquesForm,SymptomesDermatologiquesForm,SymptomesSpecifiquesForm,DifferenciationMaladieForm,ProvinceForm, HopitalForm, MedecinForm,ProvinceHopitalForm
from .models import Patient,DifferenciationMaladie,SymptomesPositifs,MaladieDetectee,Province,Medecin,Hopital
from django.contrib import messages
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404
from .models import Province, Hopital

def patient_form_view(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('contexte_form', patient_id=patient.id)
    else:
        form = PatientForm()
    return render(request, 'patient_form.html', {'form': form})

def contexte_form_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = ContexteEpidemiologiqueForm(request.POST)
        if form.is_valid():
            contexte = form.save(commit=False)
            contexte.patient = patient
            contexte.save()
            return redirect('signes_form', patient_id=patient.id)
    else:
        form = ContexteEpidemiologiqueForm(initial={'patient': patient})
    return render(request, 'contexte_form.html', {'form': form, 'patient': patient})

def signes_form_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = SignesVitauxForm(request.POST)
        if form.is_valid():
            signes = form.save(commit=False)
            signes.patient = patient
            signes.save()
            return redirect('symptomes_generaux_form', patient_id=patient.id)
    else:
        form = SignesVitauxForm(initial={'patient': patient})  # Remplir le formulaire avec le patient courant
    return render(request, 'signes_form.html', {'form': form, 'patient': patient})

def symptomes_generaux_form_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = SymptomesGenerauxForm(request.POST)
        if form.is_valid():
            symptomes_generaux = form.save(commit=False)
            symptomes_generaux.patient = patient
            symptomes_generaux.save()
            return redirect('symptomes_respiratoires_form', patient_id=patient.id)
    else:
        form = SymptomesGenerauxForm(initial={'patient': patient})  
    return render(request, 'symptomes_generaux_form.html', {'form': form, 'patient': patient})

def symptomes_respiratoires_form_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = SymptomesRespiratoiresForm(request.POST)
        if form.is_valid():
            symptomes_respiratoires = form.save(commit=False)
            symptomes_respiratoires.patient = patient
            symptomes_respiratoires.save()
            return redirect('symptomes_digestifs_form', patient_id=patient.id)
    else:
        form = SymptomesRespiratoiresForm(initial={'patient': patient})  
    return render(request, 'symptomes_respiratoires_form.html', {'form': form, 'patient': patient})

def symptomes_digestifs_form_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = SymptomesDigestifsForm(request.POST)
        if form.is_valid():
            symptomes_digestifs = form.save(commit=False)
            symptomes_digestifs.patient = patient
            symptomes_digestifs.save()
            return redirect('symptomes_neurologiques', patient_id=patient_id)  # Redirection corrigée
    else:
        form = SymptomesDigestifsForm(initial={'patient': patient})  
    return render(request, 'symptomes_digestifs_form.html', {'form': form, 'patient': patient})  # Template corrigé

def symptomes_neurologiques_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == "POST":
        form = SymptomesNeurologiquesForm(request.POST)
        if form.is_valid():
            symptomes = form.save(commit=False)
            symptomes.patient = patient
            symptomes.save()
            return redirect('symptomes_dermatologiques', patient_id=patient_id)
    else:
        form = SymptomesNeurologiquesForm(initial={'patient': patient})  
    return render(request, 'symptomes_neurologiques.html', {'form': form, 'patient': patient})

def symptomes_dermatologiques_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == "POST":
        form = SymptomesDermatologiquesForm(request.POST)
        if form.is_valid():
            symptomes = form.save(commit=False)
            symptomes.patient = patient
            symptomes.save()
            return redirect('symptomes_specifiques', patient_id=patient_id)
    else:
        form = SymptomesDermatologiquesForm(initial={'patient': patient})  
    return render(request, 'symptomes_dermatologiques.html', {'form': form, 'patient': patient})

def symptomes_specifiques_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == "POST":
        form = SymptomesSpecifiquesForm(request.POST)
        if form.is_valid():
            symptomes = form.save(commit=False)
            symptomes.patient = patient
            symptomes.save()
            return redirect('success_view',patient_id=patient_id)  # Redirection finale
    else:
        form = SymptomesSpecifiquesForm(initial={'patient': patient})  
    return render(request, 'symptomes_specifiques.html', {'form': form, 'patient': patient})

def add_differenciation_maladie(request):
    if request.method == 'POST':
        form = DifferenciationMaladieForm(request.POST)
        if form.is_valid():
            # Vérifier si la maladie existe déjà dans la base de données
            maladie_nom = form.cleaned_data['maladie']
            if not DifferenciationMaladie.objects.filter(maladie=maladie_nom).exists():
                form.save()
                return redirect('add_differenciation_maladie')
            else:
                form.add_error('maladie', 'Cette maladie existe déjà.')  # Ajouter une erreur si la maladie existe déjà
    else:
        form = DifferenciationMaladieForm()

    maladies = DifferenciationMaladie.objects.all()
    return render(request, 'differenciation_maladie.html', {'form': form, 'maladies': maladies})


from django.shortcuts import render, get_object_or_404
from .models import Patient

def success_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)  # Remplacer 'patient_id' par 'id'
    return render(request, 'success.html', {'patient': patient})


# views.py

from django.shortcuts import render, get_object_or_404
from .models import Patient, SymptomesGeneraux, SymptomesRespiratoires, SymptomesDigestifs, SymptomesNeurologiques, SymptomesDermatologiques, SymptomesSpecifiques, SymptomesPositifs

def save_and_display_positive_symptoms(request, patient_id):
    # Récupérer le patient
    patient = get_object_or_404(Patient, id=patient_id)

    # Enregistrer les symptômes généraux positifs
    for symptome in SymptomesGeneraux.objects.filter(patient=patient):
        if symptome.fievre:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Général", symptome_nom="Fièvre")
        if symptome.fatigue:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Général", symptome_nom="Fatigue")
        if symptome.sueurs_nocturnes:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Général", symptome_nom="Sueurs nocturnes")
        if symptome.perte_poids_inexplique:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Général", symptome_nom="Perte de poids inexpliquée")
        if symptome.myalgies:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Général", symptome_nom="Myalgies")
        if symptome.arthralgies:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Général", symptome_nom="Arthralgies")
        if symptome.cephalees:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Général", symptome_nom="Céphalées")

    # Enregistrer les symptômes respiratoires positifs
    for symptome in SymptomesRespiratoires.objects.filter(patient=patient):
        if symptome.toux:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Respiratoire", symptome_nom="Toux")
        if symptome.dyspnée:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Respiratoire", symptome_nom="Dyspnée")
        if symptome.douleur_thoracique:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Respiratoire", symptome_nom="Douleur thoracique")
        if symptome.congestion_nasale:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Respiratoire", symptome_nom="Congestion nasale")

    # Enregistrer les symptômes digestifs positifs
    for symptome in SymptomesDigestifs.objects.filter(patient=patient):
        if symptome.diarrhee:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Digestif", symptome_nom="Diarrhée")
        if symptome.vomissements:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Digestif", symptome_nom="Vomissements")
        if symptome.douleurs_abdominales:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Digestif", symptome_nom="Douleurs abdominales")

    # Enregistrer les symptômes neurologiques positifs
    for symptome in SymptomesNeurologiques.objects.filter(patient=patient):
        if symptome.convulsions:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Neurologique", symptome_nom="Convulsions")
        if symptome.raideur_nuque:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Neurologique", symptome_nom="Raideur du nuque")
        if symptome.paralysie_flasque:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Neurologique", symptome_nom="Paralysie flasque")
        if symptome.troubles_conscience:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Neurologique", symptome_nom="Troubles de la conscience")
        if symptome.vertiges:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Neurologique", symptome_nom="Vertiges")

    # Enregistrer les symptômes dermatologiques positifs
    for symptome in SymptomesDermatologiques.objects.filter(patient=patient):
        if symptome.eruption_cutanée:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Dermatologique", symptome_nom="Eruption cutanée")
        if symptome.lesions_ulceratives:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Dermatologique", symptome_nom="Lésions ulceratives")
        if symptome.saignement_cutane:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Dermatologique", symptome_nom="Saignement cutané")

    # Enregistrer les symptômes spécifiques positifs
    for symptome in SymptomesSpecifiques.objects.filter(patient=patient):
        if symptome.ganglions_enflés:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Spécifique", symptome_nom="Ganglions enflés")
        if symptome.jaunisse:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Spécifique", symptome_nom="Jaunisse")
        if symptome.douleurs_oculaires:
            SymptomesPositifs.objects.create(patient=patient, symptome_type="Symptôme Spécifique", symptome_nom="Douleurs oculaires")

    # Récupérer et afficher les symptômes positifs enregistrés
    symptomes_positifs = SymptomesPositifs.objects.filter(patient=patient)

    # Afficher la page avec les symptômes enregistrés
    return render(request, 'symptomes_positifs.html', {'patient': patient, 'symptomes_positifs': symptomes_positifs})

from django.shortcuts import render
from .models import SymptomesPositifs, DifferenciationMaladie, Patient
def prediction_symptomes(request, patient_id):
    # Récupérer le patient
    patient = Patient.objects.get(id=patient_id)

    # Récupérer les symptômes positifs du patient
    symptomes_positifs = SymptomesPositifs.objects.filter(patient=patient)

    # Récupérer toutes les maladies et leurs signes majeurs
    maladies = DifferenciationMaladie.objects.all()

    # Comparer les symptômes positifs avec les signes majeurs
    maladies_correspondantes = []
    symptomes_detectes_par_maladie = {}  # Dictionnaire pour stocker les symptômes détectés pour chaque maladie

    for maladie in maladies:
        signes_majeurs = maladie.signes_majeurs.split(",")  # On suppose que les signes majeurs sont séparés par une virgule
        symptomes_detectes = []

        # Convertir les signes majeurs en minuscules et diviser en mots
        signes_majeurs_normalises = [signe.strip().lower() for signe in signes_majeurs]

        # Comparer chaque symptôme du patient avec les signes majeurs de la maladie
        for symptome in symptomes_positifs:
            symptome_nom = symptome.symptome_nom.strip().lower()

            # Vérifier si le symptôme du patient correspond à un des signes majeurs
            for signe in signes_majeurs_normalises:
                if signe in symptome_nom or symptome_nom in signe:
                    symptomes_detectes.append(symptome.symptome_nom)
                    break  # Si un symptôme correspond, on arrête de chercher

        # Si on détecte au moins 3 signe majeur, on l'ajoute à la liste des maladies correspondantes
        if len(symptomes_detectes) >= 3:
            maladies_correspondantes.append({
                "maladie": maladie,
                "signes_majeurs": symptomes_detectes,
                "contexte_epidemiologique": maladie.contexte_epidemiologique,
                "examens_cles": maladie.examens_cles,
            })

            # Enregistrer la maladie détectée dans la base de données
            MaladieDetectee.objects.create(
                patient=patient,
                maladie=maladie.maladie,
                signes_majeurs=", ".join(symptomes_detectes),  # Joindre les signes majeurs détectés par une virgule
                contexte_epidemiologique=maladie.contexte_epidemiologique,
                examens_cles=maladie.examens_cles,
            )

        # Sauvegarder les symptômes détectés pour chaque maladie
        symptomes_detectes_par_maladie[maladie.maladie] = symptomes_detectes

    return render(request, 'prediction.html', {
        'patient': patient,
        'symptomes_positifs': symptomes_positifs,
        'maladies': maladies,
        'symptomes_detectes_par_maladie': symptomes_detectes_par_maladie,
        'maladies_correspondantes': maladies_correspondantes,
    })

def home(request):
    return render(request, 'home.html')
    
def home_admin(request):
    return render(request, 'diagnosis/home_admin.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def success_page_part(request):
    return render(request, 'diagnosis/success_page_part.html')


def success_page(request):
    return render(request, 'diagnosis/success_page.html')


# Afficher la liste des provinces
def province_list(request):
    provinces = Province.objects.all()
    return render(request, 'diagnosis/province_list.html', {'provinces': provinces})

# Afficher les hôpitaux associés à une province
def hopital_list(request, province_id):
    province = get_object_or_404(Province, id=province_id)
    hopitaux = Hopital.objects.filter(province=province)
    return render(request, 'diagnosis/hopital_list.html', {'hopitaux': hopitaux, 'province': province})
    

def medecin_list(request):
    medecin = Medecin.objects.all()
    return render(request, 'diagnosis/medecin_list.html', {'medecin': medecin})

def add_province(request):
    if request.method == 'POST':
        form = ProvinceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Province ajoutée avec succès.")
            return redirect('province_list')
    else:
        form = ProvinceForm()
    return render(request, 'diagnosis/add_province.html', {'form': form})

def add_hopital(request):
    if request.method == 'POST':
        form = HopitalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Hôpital ajouté avec succès.")
            return redirect('add_hopital')  # Redirection vers la même page pour afficher le nouvel hôpital
    else:
        form = HopitalForm()

    # Récupérer tous les hôpitaux
    hopitaux = Hopital.objects.all()

    return render(request, 'diagnosis/add_hopital.html', {'form': form, 'hopitaux': hopitaux})


def add_medecin(request):
    if request.method == 'POST':
        form = MedecinForm(request.POST)
        if form.is_valid():
            medecin = form.save(commit=False)
            if request.user.is_authenticated and hasattr(request.user, 'profile'):
                medecin.hopital = request.user.profile.hopital  # Récupérer l'hôpital du profil utilisateur
            medecin.save()
            messages.success(request, "Médecin ajouté avec succès.")
            return redirect('success_page_part')  # Remplacez par l'URL de votre page de succès
    else:
        # Pré-remplir le champ hopital avec celui de l'utilisateur connecté si l'utilisateur est authentifié
        hopital_default = request.user.profile.hopital if request.user.is_authenticated and hasattr(request.user, 'profile') else None
        form = MedecinForm(initial={'hopital': hopital_default})
    
    return render(request, 'diagnosis/add_medecin.html', {'form': form})

def get_hopitaux_by_province(request, province_id):
    # Récupérer les hôpitaux pour la province donnée
    hopitaux = Hopital.objects.filter(province_id=province_id)
    hopitaux_list = [{'id': hopital.id, 'name': hopital.name} for hopital in hopitaux]
    return JsonResponse({'hopitaux': hopitaux_list})

def success_page_part(request):
    return render(request, 'diagnosis/success_page_part.html')

def medecin_list_by_hopital(request, hopital_id):
    # Récupérer l'hôpital par son ID
    hopital = get_object_or_404(Hopital, id=hopital_id)
    
    # Récupérer tous les médecins associés à cet hôpital
    medecins = Medecin.objects.filter(hopital=hopital)
    
    return render(request, 'diagnosis/medecin_list_by_hopital.html', {
        'hopital': hopital,
        'medecins': medecins
    })

# Formulaire de sélection de la province et de l'hôpital
def province_hopital_form(request):
    if request.method == 'POST':
        form = ProvinceHopitalForm(request.POST)
        if form.is_valid():
            province = form.cleaned_data['province']
            hopital = form.cleaned_data['hopital']
            matricule = form.cleaned_data['matricule']

            # Vérification matricule et correspondance province-hôpital
            if hopital.matricule == matricule and hopital.province == province:
                # Stocker l'ID et le nom de l'hôpital dans la session
                request.session['hopital_id'] = hopital.id
                request.session['hopital_name'] = hopital.name
                messages.success(request, "Hôpital vérifié avec succès.")
                return redirect('hopital_dashboard')
            else:
                messages.error(request, "Matricule ou correspondance hôpital/province invalide.")
    else:
        form = ProvinceHopitalForm()

    return render(request, 'diagnosis/province_hopital_form.html', {'form': form})

# Chargement des hôpitaux en fonction de la province sélectionnée (AJAX)
def fetch_hopitals(request):
    province_id = request.GET.get('province_id')
    hopitals = Hopital.objects.filter(province_id=province_id).values('id', 'name')
    return JsonResponse(list(hopitals), safe=False)

def hopital_dashboard(request):
    # Récupérer le nom de l'hôpital à partir de la session
    hopital_name = request.session.get('hopital_name')
    
    if not hopital_name:
        return redirect('province_hopital_form')
    
    # Récupérer l'hôpital basé sur le nom (ou une autre logique pour identifier l'hôpital)
    # Si vous avez une relation avec l'utilisateur, vous pouvez chercher par utilisateur.
    # Exemple : hopital = get_object_or_404(Hopital, user=request.user)
    hopital = get_object_or_404(Hopital, name=hopital_name)
    
    # Passer l'hôpital à la vue pour le template
    return render(request, 'diagnosis/hopital_dashboard.html', {'hopital': hopital, 'hopital_name': hopital_name})

# Affichage de la liste des médecins affectés à l'hôpital et validation du matricule
def select_medecin(request):
    hopital_id = request.session.get('hopital_id')
    hopital_name = request.session.get('hopital_name')

    if not hopital_id:
        messages.error(request, "Aucun hôpital sélectionné.")
        return redirect('province_hopital_form')

    # Récupérer la liste des médecins associés à cet hôpital
    medecins = Medecin.objects.filter(hopital_id=hopital_id)

    # Si le formulaire est soumis
    if request.method == 'POST':
        medecin_id = request.POST.get('medecin')
        matricule = request.POST.get('matricule')
        
        try:
            # Vérifier si le médecin sélectionné existe et que son matricule est correct
            medecin = Medecin.objects.get(id=medecin_id, matricule=matricule)
            request.session['medecin_name'] = medecin.name
            request.session['hopital_name'] = hopital_name  # Stocker le nom de l'hôpital dans la session
            messages.success(request, f"Bienvenue, Dr. {medecin.name} à l'hôpital {hopital_name} !")
            return redirect('patient_form')
        except Medecin.DoesNotExist:
            messages.error(request, "Matricule invalide pour ce médecin.")

    return render(request, 'diagnosis/select_medecin.html', {'medecins': medecins, 'hopital_name': hopital_name})


# Validation du médecin sélectionné avec matricule et nom de l'hôpital
def validate_medecin(request):
    medecin_id = request.session.get('medecin_id')
    hopital_name = request.session.get('hopital_name')

    if not medecin_id:
        messages.error(request, "Veuillez sélectionner un médecin.")
        return redirect('select_medecin')

    # Si le formulaire est soumis
    if request.method == 'POST':
        matricule = request.POST.get('matricule')
        try:
            # Vérification si le médecin existe avec le matricule
            medecin = Medecin.objects.get(id=medecin_id, matricule=matricule)
            
            # Stocker le nom du médecin et de l'hôpital pour l'affichage ultérieur
            request.session['medecin_name'] = medecin.name
            request.session['hopital_name'] = hopital_name  # Assurer que l'hôpital est dans la session
            messages.success(request, f"Bienvenue, Dr. {medecin.name} à l'hôpital {hopital_name} !")
            return redirect('welcome_page')  # Rediriger vers la page de bienvenue
        except Medecin.DoesNotExist:
            messages.error(request, "Matricule invalide pour ce médecin.")

    return render(request, 'diagnosis/validate_medecin.html', {'hopital_name': hopital_name})


def welcome_page(request):
    medecin_name = request.session.pop('medecin_name', None)
    hopital_name = request.session.pop('hopital_name', None)
    
    if not medecin_name or not hopital_name:
        return redirect('select_medecin')

    return render(request, 'diagnosis/welcome.html', {
        'medecin_name': medecin_name,
        'hopital_name': hopital_name
    })

# Afficher la liste des maladie detecter
def maladie_detectee_list(request):
    maladie = MaladieDetectee.objects.all()
    return render(request, 'diagnosis/maladie_detectee_list.html', {'maladie': maladie})

def supprimer_maladie(request, maladie_id):
    if request.method == "POST":
        maladie = get_object_or_404(MaladieDetectee, id=maladie_id)
        maladie.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "error": "Requête invalide"}, status=400)
