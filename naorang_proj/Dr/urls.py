from django.urls import path
#from .views import drhome
from .views import dr
from . import views
urlpatterns = [
    path('', views.dr, name='dr-home'),

]
