from django.urls import path
from patientreg import views
from .views import (
    PatientregCreateView,
    PatientregDetailView,
    PatientallListView,
    patientall,
    PatientregUpdateView,
    patientprofile
)


urlpatterns = [
    path('patientall', PatientallListView.as_view(), name='patient_all'),
    path('patient/<int:pk>/', views.patientprofile, name='patient-profile'),
    #path('patient_search/', views.patient_search, name='patient_search'),

    path('patient/new/', PatientregCreateView.as_view(), name='patientname-create'),
    path('<int:pk>/', PatientregDetailView.as_view(), name='patientreg-detail'),

    path('<int:pk>/update/', PatientregUpdateView.as_view(), name='patientreg-update'),

]
