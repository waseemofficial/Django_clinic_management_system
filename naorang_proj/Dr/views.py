from django.shortcuts import render
from patientdata.models import (
    PatientHistory,
    PatientGynaec,
    PatientObstetric,
    PatientGeneral,
    PatientVitals,
    PatientSystemic,
    PatientInvestigations,
    PatientProvisional,
    PatientDiagnosis,
    PatientAdvice
)

from django.views.generic import ListView
from patientreg.models import PatientName


def dr(request):
    return render(request, 'Dr/Dr.html')


class Drlook(ListView):
    context_object_name = 'drlook'
    template_name = 'dr/drlook.html'
    queryset = PatientName.objects.all()

    def get_context_data(self, **kwargs):

        context = super(Drlook, self).get_context_data(**kwargs)
        context['patienthistory'] = PatientHistory.objects.all()
        context['patientgynaec'] = PatientGynaec.objects.all()
        context['patientobstetric'] = PatientObstetric.objects.all()
        context['patientgeneral'] = PatientGeneral.objects.all()
        context['patientvitals'] = PatientVitals.objects.all()
        context['patientsystemic'] = PatientSystemic.objects.all()
        context['patientinvestigations'] = PatientInvestigations.objects.all()
        context['patientprovisional'] = PatientProvisional.objects.all()
        context['patientdiagnosis'] = PatientDiagnosis.objects.all()
        context['patientadvice'] = PatientAdvice.objects.all()
        return context


# class drmanage(request):
 #   model = PatientHistory
