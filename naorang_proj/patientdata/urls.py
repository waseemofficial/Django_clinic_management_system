from django.urls import path
from . import views
from .views import PatienthistoryDetailView, PatientHistoryListView, patientdata, PatienthistoryUpdateView, patientvitals_create, patientvitals_update, patientvitals_delete, patienthistory_update, patientsystemic_create, patientsystemic_update, patientsystemic_delete, patientobstetric_update, patientgeneral_update, patientinvestigations_update, patientprovisional_update, patientdiagnosis_update, patientadvice_update, patientadvice_create, patientsystemic_delete
from django.conf.urls import url, include

urlpatterns = [
    #path('', PatientHistoryListView.as_view(), name='patient-data'),

    #path('patienthistory/<int:pk>/update2/', PatienthistoryUpdateView.as_view(), name='patientdata-update2'),
    #path('patienthistory1/<int:pk>/detail', PatienthistoryDetailView.as_view(), name='patienthistory-detail'),

    path('patientvitals/', views.patientvitals_list, name='patientvitals_list'),
    # ajax popup
    path('patientvitals/<int:pk>/create/', views.patientvitals_create, name='patientvitals_create'),
    path('patientvitals/<int:pk>/update/', views.patientvitals_update, name='patientvitals_update'),
    path('patientvitals/<int:pk>/delete/', views.patientvitals_delete, name='patientvitals_delete'),
    path('patienthistory/<int:pk>/update/', views.patienthistory_update, name='patienthistory_update'),
    path('patientsystemic/<int:pk>/create/', views.patientsystemic_create, name='patientsystemic_create'),
    path('patientsystemic/<int:pk>/update/', views.patientsystemic_update, name='patientsystemic_update'),
    path('patientsystemic/<int:pk>/delete/', views.patientsystemic_delete, name='patientsystemic_delete'),
    path('patientobstetric/<int:pk>/update/', views.patientobstetric_update, name='patientobstetric_update'),
    path('patientgeneral/<int:pk>/update/', views.patientgeneral_update, name='patientgeneral_update'),
    path('patientinvestigations/<int:pk>/update/', views.patientinvestigations_update, name='patientinvestigations_update'),
    path('patientprovisional/<int:pk>/update/', views.patientprovisional_update, name='patientprovisional_update'),
    path('patientdiagnosis/<int:pk>/update/', views.patientdiagnosis_update, name='patientdiagnosis_update'),
    path('patientadvice/<int:pk>/update/', views.patientadvice_update, name='patientadvice_update'),
    path('patientadvice/<int:pk>/create/', views.patientadvice_create, name='patientadvice_create'),
    path('patientadvice/<int:pk>/delete/', views.patientadvice_delete, name='patientadvice_delete'),

    #path('patienthistory1/<int:pk>/update1/', views.patienthistory_update1, name='patienthistory-update1'),

    #path('gynaec/', views.patientgynaec, name='patient-gynaec'),
    #path('history/', views.patienthistory, name='patient-history'),

]
