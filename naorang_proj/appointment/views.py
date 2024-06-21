from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Appointment
# from django.contrib.auth.models import User
from staff.models import User
from django.db.models import Q, When
from patientreg.models import PatientName
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.http import HttpResponse, JsonResponse

from django.template.loader import render_to_string
from .forms import AppointmentForm


def appointment(request):

    context = {

        'posts': Appointment.objects.all()

    }
    return render(request, 'appointment/home.html', context)


class AppointmentListView(ListView):
    model = Appointment

    template_name = 'staff/staff.html'
    context_object_name = 'posts'
    ordering = ['-start']


def appointmentcreate(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            form
            return redirect('staff-home')

    else:
        form = AppointmentForm()

    return render(request, 'appointment/appointmentcreate.html', {'form': form})


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    fields = ['appointment_for', 'patient_name', 'start', 'end', 'title', 'content', 'status', 'contact_no', 'dr_name', 'reshadule']

    def form_valid(self, form):
        form.instance.staff = self.request.user.staff
        patient_name = form.cleaned_data.get('patient_name')
        contact_no = form.cleaned_data.get('contact_no')
        appointment_for = form.cleaned_data.get('appointment_for')
        patientname = PatientName.objects.all()
        exist = PatientName.objects.filter(Q(pname__icontains=patient_name) & Q(contact_no__icontains=contact_no)).distinct()
        if appointment_for == None:
            if exist:
                form.instance.appointment_for = PatientName.objects.get(pname=patient_name, contact_no=contact_no)

        return super().form_valid(form)


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = 'appointment/appointment_detail.html'


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    fields = ['appointment_for', 'patient_name', 'start', 'end', 'title', 'content', 'contact_no', 'dr_name', 'reshadule']

    def form_valid(self, form):
        form.instance.staff = self.request.user.staff
        return super().form_valid(form)


def status_change(request):
    if request.method == 'GET':
        appointment_id = request.GET['appointment_id']
        appointment = Appointment.objects.get(id=appointment_id)
        if appointment.status == "scheduled":
            a = Appointment(status='waiting', patient_name=appointment.patient_name, appointment_for=appointment.appointment_for, start=appointment.start, end=appointment.end, title=appointment.title, content=appointment.content, contact_no=appointment.contact_no, staff=appointment.staff, date_posted=appointment.date_posted, reshadule=appointment.reshadule, id=appointment.id)
            a.save()

            return HttpResponse('success')
        else:
            a = Appointment(status='scheduled', patient_name=appointment.patient_name, appointment_for=appointment.appointment_for, start=appointment.start, end=appointment.end, title=appointment.title, content=appointment.content, contact_no=appointment.contact_no, staff=appointment.staff, date_posted=appointment.date_posted, reshadule=appointment.reshadule, id=appointment.id)
            a.save()
            return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")


class AppointmentDeleteView(DeleteView):
    model = Appointment

    success_url = '/staff/staff'
    #template_name = 'appointment/appointment_detail.html'


def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = appointment.get(pk=post_id)
        m = Like(post=likedpost)
        m.save()
        return HttpResponse("sucess!")
    else:
        return HttpResponse("Request method is not Get")


def home(request):
    return render(request, 'appointment/home.html')
