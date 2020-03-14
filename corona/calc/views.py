from django.shortcuts import render
from .forms import CalcRiskForm
from .models import CalcRisk

def calc_risk(request):
    calcform = CalcRiskForm()
    return render(request, 'calc/calc_risk.html', {'calcform': calcform})