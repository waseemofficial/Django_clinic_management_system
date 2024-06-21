from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointment
from patientreg.models import PatientName


#@receiver(post_save, sender=Appointment)
#def search_patientname(sender, instance, created, **kwargs):
 #   if created:
  #      patientname = PatientName.objects.filter(pk=appointment.appointment_for.pk)
   #     if patientname.pname == appointment.patient_name:
    #        appointment.appointment_for = PatientName
     #       instance.appointment.save()
    #  PatientHistory.objects.create(history_of_a=instance)
