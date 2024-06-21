from django import forms
from .models import Appointment
from django.contrib.admin import widgets
#from .widgets import XDSoftDateTimePickerInput


class AppointmentForm(forms.ModelForm):
    patient_name = forms.CharField(label='Patient Name', widget=forms.TextInput(attrs={"placeholder": "----Enter Patient Name----"}), required=False)
    start = forms.DateTimeField(label='Appointment Date/Time', input_formats=['%d/%m/%Y %H:%M'], required=False)

    class Meta:
        model = Appointment
        fields = ('appointment_for', 'patient_name', 'start', 'end', 'title', 'content', 'status', 'contact_no', 'dr_name', 'reshadule')

    # def __init__(self, *args, **kwargs):
     #   super(AppointmentForm, self).__init__(*args, **kwargs)
      #  self.fields['date'].widget = widgets.AdminDateWidget()
      #  self.fields['start'].widget = widgets.AdminTimeWidget()
      #  self.fields['end'].widget = widgets.AdminTimeWidget()
