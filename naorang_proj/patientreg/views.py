from django.shortcuts import render, get_object_or_404
from .models import PatientName
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
#from django.contrib.auth.models import User
from staff.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.db.models import Q, When
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from patientdata.views import PatientHistory


def patientall(request):

    context = {

        'patientregs': PatientName.objects.all()

    }

    return render(request, 'patientreg/patientall.html', context)


class PatientallListView(ListView):
    model = PatientName

    template_name = 'patientreg/patientall.html'
    context_object_name = 'posts'
    ordering = ['-date_created']
    paginate_by = 4


class PatientregCreateView(LoginRequiredMixin, CreateView):
    model = PatientName
    fields = ['image', 'pname', 'title_n', 'age', 'addult_child', 'p_h_g_name', 'sex', 'address', 'email', 'contact_no', 'foreigner_NRI', 'passport_no', 'country', 'passport_of_country']

    def form_valid(self, form):
        form.instance.staff = self.request.user
        pname = form.cleaned_data.get('pname')
        contact_no = form.cleaned_data.get('contact_no')

        patientname = PatientName.objects.all()
        exist = PatientName.objects.filter(Q(pname__icontains=pname) & Q(contact_no__icontains=contact_no)).distinct()

        if exist:

            if pname == patient.pname:

                form.add_error('pname', 'Incident with this Patient Name already exist')
            if contact_no == patient.contact_no:
                form.add_error('contact_no', 'Incident with this Contact Nunmber already exist')

            return self.form_invalid(form)
        return super().form_valid(form)


class PatientregDetailView(DetailView):
    model = PatientName
    template_name = 'patientreg/patientreg_detail.html'
    paginate_by = 4


def patientprofile(request, pk):
    patient = PatientName.objects.filter(pk=pk)
    context = {
        "patient": patient
    }

    return render(request, 'patientreg/patient_profile.html', context)


class PatientregUpdateView(LoginRequiredMixin, UpdateView):
    model = PatientName
    fields = ['image', 'pname', 'title_n', 'age', 'addult_child', 'p_h_g_name', 'sex', 'address', 'email', 'contact_no', 'foreigner_NRI', 'passport_no', 'country', 'passport_of_country']

    def form_valid(self, form):
        #form.instance.staff = self.request.user
        return super().form_valid(form)


def patient_search(request):
    return render(request, 'patientreg/patient_search.html')
