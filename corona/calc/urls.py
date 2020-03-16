from django.urls import path
from . import views

urlpatterns = [
    path('', views.calc_risk, name='calc_risk'),
]