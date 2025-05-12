from django.db import models
from django.db import models
import random
import string
# models.py
from django.db import models

class Patient(models.Model):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    nom = models.CharField(max_length=200)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    age = models.IntegerField()
    poids = models.FloatField()
    adresse_complete = models.TextField()
    occupation = models.CharField(max_length=100)
    lieu_residence = models.CharField(max_length=100)
    contact_telephonique = models.CharField(max_length=15)

    def __str__(self):
        return self.nom

class ContexteEpidemiologique(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    voyages_recents = models.BooleanField()
    voyages_details = models.CharField(max_length=200, blank=True, null=True)
    contact_avec_malades = models.BooleanField()
    contact_details = models.CharField(max_length=200, blank=True, null=True)
    epidemie_locale = models.BooleanField()

    def __str__(self):
        return f"Contexte Epidémiologique pour {self.patient.nom}"

class SignesVitaux(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    temperature = models.FloatField()
    frequence_cardiaque = models.IntegerField()
    frequence_respiratoire = models.IntegerField()
    tension_arterielle = models.CharField(max_length=50)
    saturation_oxygene = models.FloatField()

    def __str__(self):
        return f"Signes vitaux de {self.patient.nom}"

class SymptomesGeneraux(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    fievre = models.BooleanField()
    fievre_duree = models.IntegerField(null=True, blank=True)
    fatigue = models.BooleanField()
    sueurs_nocturnes = models.BooleanField()
    perte_poids_inexplique = models.BooleanField()
    myalgies = models.BooleanField()
    arthralgies = models.BooleanField()
    cephalees = models.BooleanField()
    
    def __str__(self):
        return f"Symptômes généraux de {self.patient.nom}"

class SymptomesRespiratoires(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    toux = models.BooleanField()
    toux_type = models.CharField(max_length=50, choices=[('Sèche', 'Sèche'), ('Productive', 'Productive')], blank=True, null=True)
    dyspnée = models.BooleanField()
    douleur_thoracique = models.BooleanField()
    congestion_nasale = models.BooleanField()
    
    def __str__(self):
        return f"Symptômes respiratoires de {self.patient.nom}"

class SymptomesDigestifs(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    diarrhee = models.BooleanField()
    diarrhee_type = models.CharField(max_length=100, choices=[('Dehydration', 'Avec déshydratation'), ('Sang', 'Avec sang')], blank=True, null=True)
    vomissements = models.BooleanField()
    douleurs_abdominales = models.BooleanField()
    
    def __str__(self):
        return f"Symptômes digestifs de {self.patient.nom}"

class SymptomesNeurologiques(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    convulsions = models.BooleanField()
    raideur_nuque = models.BooleanField()
    paralysie_flasque = models.BooleanField()
    localisation_paralysie = models.CharField(max_length=100, blank=True, null=True)
    troubles_conscience = models.BooleanField()
    vertiges = models.BooleanField()

    def __str__(self):
        return f"Symptômes neurologiques de {self.patient.nom}"

class SymptomesDermatologiques(models.Model):
    SAIGN_CHOICES = [
        ('AUCUN','aucun'),
        ('ECCHYMOSES', 'ecchymoses'),
        ('PETECHIES', 'pétéchies'),
    ]
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    eruption_cutanée = models.BooleanField()
    eruption_details = models.CharField(max_length=200, blank=True, null=True)
    lesions_ulceratives = models.BooleanField()
    saignement_cutane = models.BooleanField()
    saignement_details = models.CharField(max_length=10, choices=SAIGN_CHOICES)

    def __str__(self):
        return f"Symptômes dermatologiques de {self.patient.nom}"

class SymptomesSpecifiques(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    ganglions_enflés = models.BooleanField()
    localisation_ganglions = models.CharField(max_length=100, blank=True, null=True)
    jaunisse = models.BooleanField()
    douleurs_oculaires = models.BooleanField()

    def __str__(self):
        return f"Symptômes spécifiques de {self.patient.nom}"
    
class SymptomesPositifs(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptome_type = models.CharField(max_length=100)
    symptome_nom = models.CharField(max_length=100)
    date_enregistrement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.symptome_nom}"
    
from django.db import models

class MaladieDetectee(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    maladie = models.CharField(max_length=200)
    signes_majeurs = models.TextField()
    contexte_epidemiologique = models.TextField()
    examens_cles = models.TextField()
    date_detection = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.maladie} - {self.patient.nom}"


class DifferenciationMaladie(models.Model):
    maladie = models.CharField(max_length=200)
    signes_majeurs = models.TextField()
    contexte_epidemiologique = models.TextField()
    examens_cles = models.TextField()

    def __str__(self):
        return self.maladie

def generate_hopital_matricule():
    """
    Génère un matricule unique et sécurisé pour les hôpitaux.
    """
    length = 8  # Longueur du matricule
    numbers = random.choice(string.digits)
    uppercase = random.choice(string.ascii_uppercase)
    special = random.choice("@#$%&*!")
    lowercase = random.choice(string.ascii_lowercase)
    
    # Mélanger les caractères obligatoires avec des caractères aléatoires
    other_chars = ''.join(random.choices(string.ascii_letters + string.digits + "@#$%&*!?", k=length - 4))
    matricule = numbers + uppercase + special + lowercase + other_chars
    
    # Mélanger les caractères pour plus d'aléatoire
    return ''.join(random.sample(matricule, len(matricule)))


def generate_medecin_matricule():
    """
    Génère un matricule unique et sécurisé pour les médecins.
    """
    length = 8  # Longueur du matricule
    numbers = random.choice(string.digits)
    uppercase = random.choice(string.ascii_uppercase)
    special = random.choice("@#$%&!")
    lowercase = random.choice(string.ascii_lowercase)
    
    # Mélanger les caractères obligatoires avec des caractères aléatoires
    other_chars = ''.join(random.choices(string.ascii_letters + string.digits + "@#$%&!?", k=length - 4))
    matricule = numbers + uppercase + special + lowercase + other_chars
    
    # Mélanger les caractères pour plus d'aléatoire
    return ''.join(random.sample(matricule, len(matricule)))

class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Hopital(models.Model):
    MATRICULE_LENGTH = 8
    matricule = models.CharField(
        max_length=MATRICULE_LENGTH,
        unique=True,
        default=generate_hopital_matricule,
        editable=False
    )
    name = models.CharField(max_length=100)
    address = models.TextField()
    emergency_contact = models.CharField(max_length=15)
    province = models.ForeignKey('Province', on_delete=models.CASCADE, related_name='hopitaux')
    photo = models.ImageField(upload_to='hopital_photos/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Medecin(models.Model):
    MATRICULE_LENGTH = 8
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    matricule = models.CharField(
        max_length=MATRICULE_LENGTH,
        unique=True,
        default=generate_medecin_matricule,  # Appel de la fonction sans lambda
        editable=False
    )
    name = models.CharField(max_length=100)
    post_nom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    specialite = models.CharField(max_length=100)
    emergency_contact = models.CharField(max_length=15)
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE, related_name='medecins')
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.post_nom}"

    

class CaseData(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    date = models.DateField()
    cases_positive = models.IntegerField()
    cases_negative = models.IntegerField()

    def __str__(self):
        return f"{self.province.name} - {self.date}"