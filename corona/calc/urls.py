from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.calc_risk, name='calc_risk'),
]