from __future__ import unicode_literals
from staff.models import Staff
from django.db import models
from patientreg.models import PatientName
from django.core import serializers
#from django.contrib.auth.models import User
from staff.models import User
from datetime import date
from django.utils import timezone
from django.urls import reverse


class TodayManager(models.Manager):
    """docstring for PublishedManager"""

    def get_query_set(self):
        today = datetime.today()
        start_date = datetime(today.year, today.month, today.day)
        end_date = datetime(today.year, today.month, today.day + 1)
        return super(TodayManager, self).get_query_set().filter(start__gte=start_date, start__lte=end_date)


class ScheduledManager(models.Manager):
    """docstring for PublishedManager"""

    def get_queryset(self):
        return super(ScheduledManager, self).get_queryset().filter(status="scheduled")


class WaitingManager(models.Manager):
    """docstring for PublishedManager"""

    def get_queryset(self):
        return super(WaitingManager, self).get_queryset().filter(status="waiting")


class SessionManager(models.Manager):
    """docstring for PublishedManager"""

    def get_queryset(self):
        return super(SessionManager, self).get_queryset().filter(status="session")


class DoneManager(models.Manager):
    """docstring for PublishedManager"""

    def get_queryset(self):
        return super(DoneManager, self).get_queryset().filter(status="done")


class Appointment(models.Model):

    # Published = models.Manager()  #object manager
    objects = models.Manager()  # not required
    today = TodayManager()
    scheduled = ScheduledManager()
    waiting = WaitingManager()  # our custom model manager
    session = SessionManager()
    done = DoneManager()

    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('waiting', 'Waiting'),
        ('session', 'Session'),
        ('done', 'Done'),
    )

    id = models.AutoField(primary_key=True)
    appointment_for = models.ForeignKey(PatientName, on_delete=models.CASCADE, null=True, blank=True, default='')
    patient_name = models.CharField(max_length=255)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    contact_no = models.DecimalField(max_digits=15, decimal_places=0)
    dr_name = models.ManyToManyField(User, limit_choices_to={'is_dr': True})
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(default=timezone.now)
    reshadule = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.patient_name

    def get_absolute_url(self):
        return reverse('staff-home',)

    def get_appointmentjs(self):
        appointmentjs = serializer.serialize("json", Appointment.objects.all())

        return appointmentjs


class Like(models.Model):
    post = models.ForeignKey(Appointment, on_delete=models.CASCADE)
