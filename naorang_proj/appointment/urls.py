from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import (

    AppointmentCreateView,
    AppointmentDetailView,
    AppointmentUpdateView,
    AppointmentDeleteView,
    status_change,
    appointmentcreate,

)

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),

    #path('status/', views.status, name='status'),
    path('appointment/new/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('appointment/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment-update'),
    path('status/', views.status_change, name='status'),
    path('appointment/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment-delete'),
    path('new/',views.appointmentcreate,name='appointment-new' )
]
