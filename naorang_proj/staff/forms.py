from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from staff.models import Profile, User
from appointment.models import Appointment
BIRTH_YEAR_CHOICES = range(1950, 2020)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'date_of_birth']
