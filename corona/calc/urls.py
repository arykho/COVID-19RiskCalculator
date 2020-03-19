from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^calc/', views.calc_risk, name='calc_risk'),
    url(r'^vaccine/', views.vaccine, name='vaccine'),
    url(r'^treatment/', views.treatment, name='treatment'),
    url(r'^.*$', RedirectView.as_view(url='calc/', permanent=False), name='index')
]