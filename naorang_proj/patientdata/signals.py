from django.db.models.signals import post_save
#from django.contrib.auth.models import User
from staff.models import User
from django.dispatch import receiver
from .models import PatientHistory, PatientGynaec, PatientObstetric, PatientGeneral, PatientVitals, PatientSystemic, PatientInvestigations, PatientProvisional, PatientDiagnosis, PatientAdvice
from patientreg.models import PatientName  # signal sender

# HISTORY


@receiver(post_save, sender=PatientName)
def create_patienthistory(sender, instance, created, **kwargs):
    if created:
        PatientHistory.objects.create(history_of_a=instance)


@receiver(post_save, sender=PatientName)
def save_patienthistory(sender, instance, **kwargs):
    instance.patienthistory.save()

    # GYNAEC HISTORY


@receiver(post_save, sender=PatientName)
def create_patientgynaec(sender, instance, created, **kwargs):
    if created:
        PatientGynaec.objects.create(history_of_b=instance)


@receiver(post_save, sender=PatientName)
def save_patientgynaec(sender, instance, **kwargs):
    instance.patientgynaec.save()

    # OBSTETRIC HISTORY


@receiver(post_save, sender=PatientName)
def create_patientobstetric(sender, instance, created, **kwargs):
    if created:
        PatientObstetric.objects.create(history_of_c=instance)


@receiver(post_save, sender=PatientName)
def save_patientobstetric(sender, instance, **kwargs):
    instance.patientobstetric.save()

    # GENERAL EXAMINATION


@receiver(post_save, sender=PatientName)
def create_patientgeneral(sender, instance, created, **kwargs):
    if created:
        PatientGeneral.objects.create(history_of_d=instance)


@receiver(post_save, sender=PatientName)
def save_patientgeneral(sender, instance, **kwargs):
    instance.patientgeneral.save()

    # VITALS


@receiver(post_save, sender=PatientName)
def create_patientvitals(sender, instance, created, **kwargs):
    if created:
        PatientVitals.objects.create(history_of_e=instance)


#@receiver(post_save, sender=PatientName)
# def save_patientvitals(sender, instance, **kwargs):
 #   instance.patientvitals.save()

    # SYSTEMIC EXAMINATION:

@receiver(post_save, sender=PatientName)
def create_patientsystemic(sender, instance, created, **kwargs):
    if created:
        PatientSystemic.objects.create(history_of_f=instance)


#@receiver(post_save, sender=PatientName)
# def save_patientsystemic(sender, instance, **kwargs):
#    instance.respiratory_system.save()

    # INVESTIGATIONS


@receiver(post_save, sender=PatientName)
def create_patientinvestigations(sender, instance, created, **kwargs):
    if created:
        PatientInvestigations.objects.create(history_of_g=instance)


@receiver(post_save, sender=PatientName)
def save_patientinvestigations(sender, instance, **kwargs):
    instance.patientinvestigations.save()

    # PROVISIONAL DIAGNOSIS


@receiver(post_save, sender=PatientName)
def create_patientprovisional(sender, instance, created, **kwargs):
    if created:
        PatientProvisional.objects.create(history_of_h=instance)


@receiver(post_save, sender=PatientName)
def save_patientprovisional(sender, instance, **kwargs):
    instance.patientprovisional.save()

    # FINAL DIAGNOSIS


@receiver(post_save, sender=PatientName)
def create_patientfinal(sender, instance, created, **kwargs):
    if created:
        PatientDiagnosis.objects.create(history_of_i=instance)


@receiver(post_save, sender=PatientName)
def save_patientfinal(sender, instance, **kwargs):
    instance.patientdiagnosis.save()

    # ADVICE


@receiver(post_save, sender=PatientName)
def create_patientadvice(sender, instance, created, **kwargs):
    if created:
        PatientAdvice.objects.create(history_of_j=instance)


#@receiver(post_save, sender=PatientName)
# def save_patientadvice(sender, instance, **kwargs):
 #   instance.advice.save()
