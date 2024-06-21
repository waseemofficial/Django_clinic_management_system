from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PatientHistory, PatientGynaec, PatientObstetric, PatientGeneral, PatientVitals, PatientSystemic, PatientInvestigations, PatientProvisional, PatientDiagnosis, PatientAdvice
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from patientreg.models import PatientName

from .forms import PatientvitalsForm, PatienthistoryForm, PatientsystemicForm, PatientobstetricForm, PatientgeneralForm, PatientinvestigationsForm, PatientprovisionalForm, PatientdiagnosisForm, PatientadviceForm
from django.http import JsonResponse
from django.template.loader import render_to_string


def patientdata(request):

    context = {

        'posts': PatientHistory.objects.all()
        #'patientgynaec': PatientGynaec.objects.all(),
        #'patientobstetic': PatientObstetric.objects.all(),
        #'patientgeneral': PatientGeneral.objects.all(),
        #'patientvitals': PatientVitals.objects.all(),
        #'patientsystemic': PatientSystemic.objects.all(),
        #'patientinvestigations': PatientInvestigations.objects.all(),
        #'patientprovisional': PatientProvisional.objects.all(),
        #'patientdiagnosis': PatientDiagnosis.objects.all(),
        #'patientadvice': PatientAdvice.objects.all()


    }
    return render(request, 'patientdata/patientdata.html', context)


def patientvitals_list(request):
    patientvitals = PatientVitals.objects.all()
    return render(request, 'patientdata/patientvitals_list.html', {'patientvitals': patientvitals})
# def save_patienthistory_form(request,form,template_name):
 #   data=dict()
  #  if request.method =='POST':
   #     if form.is_valid():
    #        form.save()
    #       data['form_is_valid']=True
    #      patienthistory=PatientHistory.objects.all()


def patienthistory_update1(request, id):
    patienthistory = PatientHistory.objects.get(id=id)


def save_patientvitals_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            data['form_is_valid'] = True
            patientvitals = PatientVitals.objects.all()
            data['html_patientreg_detail'] = render_to_string('patientdata/partial_patientvitals_detail.html', {
                'patientvitals': patientvitals
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def patientvitals_create(request, pk):

    patientname = get_object_or_404(PatientName, pk=pk)
    patientvitals = PatientVitals.objects.create(history_of_e=patientname)

    if request.method == 'POST':
        form = PatientvitalsForm(request.POST, instance=patientvitals)

    else:
        form = PatientvitalsForm(instance=patientvitals)
    return save_patientvitals_form(request, form, 'patientdata/partial_patientvitals_update.html')
    # return render(request, )


def patientvitals_update(request, pk):
    patientvitals = get_object_or_404(PatientVitals, pk=pk)
    if request.method == 'POST':
        form = PatientvitalsForm(request.POST, instance=patientvitals)
    else:
        form = PatientvitalsForm(instance=patientvitals)
    return save_patientvitals_form(request, form, 'patientdata/partial_patientvitals_update.html')


def patientvitals_delete(request, pk):
    patientvitals = get_object_or_404(PatientVitals, pk=pk)
    data = dict()
    if request.method == 'POST':
        patientvitals.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        patientvitals = PatientVitals.objects.all()
        data['html_patientreg_detail'] = render_to_string('patientdata/partial_patientvitals_detail.html', {
            'post': patientvitals
        })
    else:
        context = {'patientvitals': patientvitals}
        data['html_form'] = render_to_string('patientdata/partial_patientvitals_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)

# patient history


def save_patienthistory_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            data['form_is_valid'] = True
            patienthistory = PatientHistory.objects.all()
            data['html_patientreg_detail'] = render_to_string('patientreg/patientreg_detail.html', {
                'patienthistory': PatientHistory
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def patienthistory_update(request, pk):
    patienthistory = get_object_or_404(PatientHistory, pk=pk)
    if request.method == 'POST':
        form = PatienthistoryForm(request.POST, instance=patienthistory)
    else:
        form = PatienthistoryForm(instance=patienthistory)
    return save_patienthistory_form(request, form, 'patientdata/partial_patienthistory_update.html')

# patient systemic


def patientsystemic_create(request, pk):

    patientname = get_object_or_404(PatientName, pk=pk)
    patientsystemic = PatientSystemic.objects.create(history_of_f=patientname)

    if request.method == 'POST':
        form = PatientsystemicForm(request.POST, instance=patientsystemic)

    else:
        form = PatientsystemicForm(instance=patientsystemic)
    return save_patientsystemic_form(request, form, 'patientdata/partial_patientsystemic_update.html')
    # return render(request, )


def save_patientsystemic_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            data['form_is_valid'] = True
            patientsystemic = PatientSystemic.objects.all()
            data['html_patientreg_detail'] = render_to_string('patientdata/partial_patientsystemic_detail.html', {
                'patientsystemic': PatientSystemic
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def patientsystemic_update(request, pk):
    patientsystemic = get_object_or_404(PatientSystemic, pk=pk)
    if request.method == 'POST':
        form = PatientsystemicForm(request.POST, instance=patientsystemic)
    else:
        form = PatientsystemicForm(instance=patientsystemic)
    return save_patientsystemic_form(request, form, 'patientdata/partial_patientsystemic_update.html')


def patientsystemic_delete(request, pk):
    patientsystemic = get_object_or_404(PatientSystemic, pk=pk)
    data = dict()
    if request.method == 'POST':
        patientsystemic.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        patientsystemic = PatientSystemic.objects.all()
        data['html_patientreg_detail'] = render_to_string('patientdata/partial_patientsystemic_detail.html', {
            'post': patientsystemic
        })
    else:
        context = {'patientsystemic': patientsystemic}
        data['html_form'] = render_to_string('patientdata/partial_patientsystemic_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)

# patient Obstetric


def save_patientobstetric_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            data['form_is_valid'] = True
            patientobstetric = PatientObstetric.objects.all()
            data['html_patientreg_detail'] = render_to_string('patientreg/patientreg_detail.html', {
                'patientobstetric': PatientObstetric
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def patientobstetric_update(request, pk):
    patientobstetric = get_object_or_404(PatientObstetric, pk=pk)
    if request.method == 'POST':
        form = PatientobstetricForm(request.POST, instance=patientobstetric)
    else:
        form = PatientobstetricForm(instance=patientobstetric)
    return save_patientobstetric_form(request, form, 'patientdata/partial_patientobstetric_update.html')

# patient General


def save_patientgeneral_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            data['form_is_valid'] = True
            patientgeneral = PatientGeneral.objects.all()
            data['html_patientreg_detail'] = render_to_string('patientreg/patientreg_detail.html', {
                'patientgeneral': PatientGeneral
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def patientgeneral_update(request, pk):
    patientgeneral = get_object_or_404(PatientGeneral, pk=pk)
    if request.method == 'POST':
        form = PatientgeneralForm(request.POST, instance=patientgeneral)
    else:
        form = PatientgeneralForm(instance=patientgeneral)
    return save_patientgeneral_form(request, form, 'patientdata/partial_patientgeneral_update.html')


# patient Investigations


def save_patientinvestigations_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            data['form_is_valid'] = True
            patientinvestigations = PatientInvestigations.objects.all()
            data['html_patientreg_detail'] = render_to_string('patientreg/patientreg_detail.html', {
                'patientinvestigations': PatientInvestigations
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def patientinvestigations_update(request, pk):
    patientinvestigations = get_object_or_404(PatientInvestigations, pk=pk)
    if request.method == 'POST':
        form = PatientinvestigationsForm(request.POST, instance=patientinvestigations)
    else:
        form = PatientinvestigationsForm(instance=patientinvestigations)
    return save_patientinvestigations_form(request, form, 'patientdata/partial_patientinvestigations_update.html')

# patient Provisional


def save_patientprovisional_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            data['form_is_valid'] = True
            patientprovisional = PatientProvisional.objects.all()
            data['html_patientreg_detail'] = render_to_string('patientreg/patientreg_detail.html', {
                'patientprovisional': PatientProvisional
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def patientprovisional_update(request, pk):
    patientprovisional = get_object_or_404(PatientProvisional, pk=pk)
    if request.method == 'POST':
        form = PatientprovisionalForm(request.POST, instance=patientprovisional)
    else:
        form = PatientprovisionalForm(instance=patientprovisional)
    return save_patientprovisional_form(request, form, 'patientdata/partial_patientprovisional_update.html')

# patient diagnosis


def save_patientdiagnosis_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            data['form_is_valid'] = True
            patientdiagnosis = PatientDiagnosis.objects.all()
            data['html_patientreg_detail'] = render_to_string('patientreg/patientreg_detail.html', {
                'patientdiagnosis': PatientDiagnosis
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def patientdiagnosis_update(request, pk):
    patientdiagnosis = get_object_or_404(PatientDiagnosis, pk=pk)
    if request.method == 'POST':
        form = PatientdiagnosisForm(request.POST, instance=patientdiagnosis)
    else:
        form = PatientdiagnosisForm(instance=patientdiagnosis)
    return save_patientdiagnosis_form(request, form, 'patientdata/partial_patientdiagnosis_update.html')


# patient advice


def save_patientadvice_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            data['form_is_valid'] = True
            patientadvice = PatientAdvice.objects.all()
            data['html_patientreg_detail'] = render_to_string('patientreg/patientreg_detail.html', {
                'patientadvice': PatientAdvice
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def patientadvice_create(request, pk):

    patientname = get_object_or_404(PatientName, pk=pk)
    patientadvice = PatientAdvice.objects.create(history_of_j=patientname)

    if request.method == 'POST':
        form = PatientadviceForm(request.POST, instance=patientadvice)

    else:
        form = PatientadviceForm(instance=patientadvice)
    return save_patientadvice_form(request, form, 'patientdata/partial_patientadvice_update.html')


def patientadvice_update(request, pk):
    patientadvice = get_object_or_404(PatientAdvice, pk=pk)
    if request.method == 'POST':
        form = PatientadviceForm(request.POST, instance=patientadvice)
    else:
        form = PatientadviceForm(instance=patientadvice)
    return save_patientadvice_form(request, form, 'patientdata/partial_patientadvice_update.html')


def patientadvice_delete(request, pk):
    patientadvice = get_object_or_404(PatientAdvice, pk=pk)
    data = dict()
    if request.method == 'POST':
        patientadvice.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        patientadvice = PatientAdvice.objects.all()
        data['html_patientreg_detail'] = render_to_string('patientdata/partial_patientadvice_detail.html', {
            'post': patientadvice
        })
    else:
        context = {'patientadvice': patientadvice}
        data['html_form'] = render_to_string('patientdata/partial_patientadvice_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


class PatientHistoryListView(ListView):
    model = PatientHistory
    template_name = 'patientdata/patientdata.html'
    context_object_name = 'posts'
    paginate_by = 4


class PatienthistoryDetailView(DetailView):
    model = PatientHistory
    #template_name = 'patientdata/patienthistory_detail.html'


class PatienthistoryUpdateView(LoginRequiredMixin, UpdateView):
    model = PatientHistory
    #template_name = 'patientdata/patienthistory_form.html'
    #success_url = '/patientreg/{{id }}'
    fields = ['presenting_complaints', 'history_of_presenting_complaints', 'department', 'past_historys', 'past_history_note', 'drug_history', 'drug_history_note', 'drug_allergies', 'treatment_history', 'treatment_history_note', 'surgeries', 'personal_history_sleep', 'personal_history_appetite', 'personal_history_diet', 'personal_history_bowel_bladder_habits', 'addictions', 'occupational_history', 'family_history']

    def form_valid(self, form):
        # form.instance. = self.request.user
        return super().form_valid(form)
