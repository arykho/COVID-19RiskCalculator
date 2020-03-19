from django.shortcuts import render
from .forms import CalcRiskForm
from .models import CalcRisk
from math import pow

def calc_risk(request):
    if request.method == "POST":
        calcform = CalcRiskForm(request.POST)
        if calcform.is_valid():
            gender = calcform.data['gender']
            age = calcform.data['age']
            condition = calcform['condition'].value()
            riskfactor = calcRiskFactor(gender, age, condition)
            return render(request, 'calc/calc_risk.html',
                          {'calcform': calcform,
                           'riskfactor': riskfactor})
    
    calcform = CalcRiskForm()
    return render(request, 'calc/calc_risk.html', {'calcform': calcform})

def vaccine(request):
    return render(request, 'calc/vaccine.html', {})
        
def treatment(request):
    return render(request, 'calc/treatment.html', {})

def calcRiskFactor(gender, age, condition):
    diseaseFactor = 1
    comorbities = 0
    counter = 0

        
    for comorbities in condition:
        #===================================================================
        # -------COMORBIDITIES-------
        # 
        # 1) Cardiovascular Disease
        # 2) Diabetes
        # 3) Chronic Respiratory Disease
        # 4) Hypertension
        # 5) Cancer
        # 6) None
        # 
        #===================================================================

        counter += 1
            
        if counter > 1:
            diseaseFactor *= 1.1
                        
        if comorbities == "1":
            diseaseFactor *= 1.105
        elif comorbities == "2":
            diseaseFactor *= 1.073
        elif comorbities == "3":
            diseaseFactor *= 1.063
        elif comorbities == "4":
            diseaseFactor *= 1.06
        elif comorbities == "5":
            diseaseFactor *= 1.056
        elif comorbities == "6":
            diseaseFactor *= 1.009

        
    ageCount = 1;
        
    age = int(age)
    if age > 100:
        age = 100
        
    if age > 27:
        ageCount = pow(1.04, age)+ 0.1 - (0.095*age)
    elif age > 10 and age <= 27:
        ageCount = pow(1.02, age) -1.2
    elif age <= 10:
        ageCount = 0
        
    probability = diseaseFactor * (ageCount);
    
    probabilityFinal = (2*probability)/4.5;
        
    if gender == "1":
        probabilityFinal *= 1.7
    elif gender == "2":
        probabilityFinal *= 2.8
    
    return format(probabilityFinal, ".2f")

