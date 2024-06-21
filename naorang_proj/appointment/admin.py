from django.contrib import admin

from .models import Appointment, Like


class Status(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'appointment_for', 'staff', 'title', 'status')


admin.site.register(Like)
admin.site.register(Appointment, Status)
