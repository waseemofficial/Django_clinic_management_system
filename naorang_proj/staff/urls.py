from django.urls import path
from django.contrib.auth import views as auth_views

from staff import views as user_views

from appointment.views import (
    AppointmentListView,

)


urlpatterns = [
    path('staff', AppointmentListView.as_view(), name='staff-home'),
    path('', auth_views.LoginView.as_view(template_name='staff/login.html'), name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('register', user_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='staff/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='staff/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='staff/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='staff/password_reset_confirm.html'), name='password_reset_confirm'),
]
