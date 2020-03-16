from django.shortcuts import render
from .forms import CalcRiskForm
from .models import CalcRisk

def calc_risk(request):
    if request.method == "POST":
        calcform = CalcRiskForm(request.POST)
        if calcform.is_valid():
            gender = calcform.data['gender']
            age = calcform.data['age']
            condition = calcform['condition'].value()
            return render(request, 'calc/calc_risk.html',
                          {'calcform': calcform,
                           'riskfactor': '20%'})
    
    calcform = CalcRiskForm()
    return render(request, 'calc/calc_risk.html', {'calcform': calcform})
        