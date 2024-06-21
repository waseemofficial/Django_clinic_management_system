from django.db import models
from patientreg.models import PatientName
#from django.contrib.auth.models import User
from staff.models import User
from django.utils import timezone


class PatientHistory(models.Model):

    General_Medicine = 'General_Medicine'
    Neurology = 'Neurology'
    Pediatrics = 'Pediatrics'
    Geriatrics = 'Geriatrics'
    OBG = 'OBG'
    Dermatology = 'Dermatology'
    Urogenital = 'Urogenital'
    ENT = 'ENT'
    Orthopedics = 'Orthopedics'
    Regimenal_Therapy = 'Regimenal Therapy'
    Other = 'Other'

    DEPARTMENT_CHOICES = (
        (General_Medicine, 'General Medicine'),
        (Neurology, 'Neurology'),
        (Pediatrics, 'Pediatrics'),
        (Geriatrics, 'Geriatrics'),
        (OBG, 'OBG'),
        (Dermatology, 'Dermatology'),
        (Urogenital, 'Urogenital'),
        (ENT, 'ENT'),
        (Orthopedics, 'Orthopedics'),
        (Regimenal_Therapy, 'Regimenal Therapy'),
        (Other, 'Other'),
    )

    # HISTORY
    history_of_a = models.OneToOneField(PatientName, on_delete=models.CASCADE,)
    presenting_complaints = models.TextField(max_length=500, null=True, blank=True, default='')
    history_of_presenting_complaints = models.TextField(max_length=500, null=True, blank=True, default='')
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES, default='', null=True, blank=True)
    past_historys = models.NullBooleanField(default='')
    past_history_note = models.CharField(max_length=500, null=True, blank=True, default='')
    drug_history = models.NullBooleanField(default='')
    drug_history_note = models.CharField(max_length=500, null=True, blank=True, default='')
    drug_allergies = models.CharField(max_length=500, null=True, blank=True, default='')
    treatment_history = models.NullBooleanField(default='')
    treatment_history_note = models.CharField(max_length=500, null=True, blank=True, default='')
    surgeries = models.CharField(max_length=500, null=True, blank=True)
    personal_history_sleep = models.CharField(max_length=500, null=True, blank=True, default='')
    personal_history_appetite = models.CharField(max_length=500, null=True, blank=True, default='')
    personal_history_diet = models.CharField(max_length=500, null=True, blank=True, default='')
    personal_history_bowel_bladder_habits = models.CharField(max_length=500, null=True, blank=True, default='')
    addictions = models.NullBooleanField(default='')
    occupational_history = models.CharField(max_length=500, null=True, blank=True, default='')
    family_history = models.TextField(max_length=500, null=True, blank=True, default='')

    def __str__(self):
        return self.history_of_a.pname

    def get_absolute_url(self):
        return reverse('patient-data', kwargs={'pk': self.pk})

    # GYNAEC HISTORY


class PatientGynaec(models.Model):

    history_of_b = models.OneToOneField(PatientName, on_delete=models.CASCADE,)
    menarche = models.CharField(max_length=500, null=True, blank=True)
    menopause = models.CharField(max_length=500, null=True, blank=True)
    married_life = models.CharField(max_length=500, null=True, blank=True)
    last_menstrual_period = models.CharField(max_length=500, null=True, blank=True)
    flow = models.CharField(max_length=500, null=True, blank=True)
    regularity = models.CharField(max_length=500, null=True, blank=True)
    cycle = models.CharField(max_length=500, null=True, blank=True)
    dysmenorrhea = models.CharField(max_length=500, null=True, blank=True)
    clots = models.CharField(max_length=500, null=True, blank=True)
    leucorrhea = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.history_of_b.pname

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})

    # OBSTETRIC HISTORY


class PatientObstetric(models.Model):

    history_of_c = models.OneToOneField(PatientName, on_delete=models.CASCADE,)
    G = models.CharField(max_length=500, null=True, blank=True)
    P = models.CharField(max_length=500, null=True, blank=True)
    L = models.CharField(max_length=500, null=True, blank=True)
    A = models.CharField(max_length=500, null=True, blank=True)
    D = models.CharField(max_length=500, null=True, blank=True)
    age_and_sex_child = models.CharField(max_length=500, null=True, blank=True)
    method_of_delivery = models.CharField(max_length=500, null=True, blank=True)
    nvd = models.CharField(max_length=500, null=True, blank=True)
    lscs = models.CharField(max_length=500, null=True, blank=True)
    immunization_of_children = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.history_of_c.pname

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})

    # GENERAL EXAMINATION


class PatientGeneral(models.Model):

    history_of_d = models.OneToOneField(PatientName, on_delete=models.CASCADE,)
    built_and_nourishment = models.CharField(max_length=500, null=True, blank=True)
    pallor = models.CharField(max_length=500, null=True, blank=True)
    edema = models.CharField(max_length=500, null=True, blank=True)
    cyanosis = models.CharField(max_length=500, null=True, blank=True)
    clubbing = models.CharField(max_length=500, null=True, blank=True)
    icterus = models.CharField(max_length=500, null=True, blank=True)
    lymphadenopathy = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.history_of_d.pname

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})

    # VITALS


class PatientVitals(models.Model):

    history_of_e = models.ForeignKey(PatientName, on_delete=models.CASCADE,)
    pulse = models.CharField(max_length=500, null=True, blank=True)
    blood_pressure = models.CharField(max_length=500, null=True, blank=True)
    respiratory_rate = models.CharField(max_length=500, null=True, blank=True)
    weight = models.CharField(max_length=500, null=True, blank=True)
    temperature = models.CharField(max_length=500, null=True, blank=True)
    mizaj_1 = models.CharField(max_length=500, null=True, blank=True)
    mizaj_2 = models.CharField(max_length=500, null=True, blank=True)
    date_vitals = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.history_of_e.pname

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})

    # SYSTEMIC EXAMINATION:


class PatientSystemic(models.Model):

    history_of_f = models.ForeignKey(PatientName, on_delete=models.CASCADE,)
    respiratory_system = models.CharField(max_length=500, null=True, blank=True)
    cardiovascular_system = models.CharField(max_length=500, null=True, blank=True)
    abdomen = models.CharField(max_length=500, null=True, blank=True)
    central_nervous_system = models.CharField(max_length=500, null=True, blank=True)
    locomotor_system = models.CharField(max_length=500, null=True, blank=True)
    local_examination = models.CharField(max_length=500, null=True, blank=True)
    date_tested = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.history_of_f.pname

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})

    # INVESTIGATIONS


class PatientInvestigations(models.Model):

    history_of_g = models.OneToOneField(PatientName, on_delete=models.CASCADE,)
    investigations = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.history_of_g.pname

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})

    # PROVISIONAL DIAGNOSIS


class PatientProvisional(models.Model):

    history_of_h = models.OneToOneField(PatientName, on_delete=models.CASCADE,)
    previsional_diagnosis = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.history_of_h.pname

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})

    # FINAL DIAGNOSIS


class PatientDiagnosis(models.Model):

    history_of_i = models.OneToOneField(PatientName, on_delete=models.CASCADE,)
    filal_Diagnosis = models.TextField(max_length=500, null=True, blank=True)
    date_diagnosis = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.history_of_i.pname

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})

    # ADVICE


class PatientAdvice(models.Model):

    history_of_j = models.ForeignKey(PatientName, on_delete=models.CASCADE,)
    advice = models.TextField(max_length=500, null=True, blank=True)
    date_visited = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.history_of_j.pname

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})
