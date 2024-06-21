from django.contrib import admin

from .models import PatientHistory, PatientGynaec, PatientObstetric, PatientGeneral, PatientVitals, PatientSystemic, PatientInvestigations, PatientProvisional, PatientDiagnosis, PatientAdvice

admin.site.register(PatientHistory)
admin.site.register(PatientGynaec)
admin.site.register(PatientObstetric)
admin.site.register(PatientGeneral)
admin.site.register(PatientVitals)
admin.site.register(PatientSystemic)
admin.site.register(PatientInvestigations)
admin.site.register(PatientProvisional)
admin.site.register(PatientDiagnosis)
admin.site.register(PatientAdvice)
