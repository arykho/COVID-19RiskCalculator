from django import forms

from .models import CalcRisk

class CalcRiskForm(forms.ModelForm):
    genderChoices = [('1','Female'),('2','Male')]
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=genderChoices))
    age = forms.CharField(label = "Age", max_length = 10)

    conditionChoices = [('1','Cardiovascular Disease'),
                        ('2','Diabetes'),
                        ('3', 'Chronic respiratory disease'),
                        ('4', 'Hypertension'),
                        ('5', 'Cancer'),
                        ('6', 'None'),]
    
    condition=forms.CharField(label='Comorbities', required=False,
                              widget=forms.CheckboxSelectMultiple(choices=conditionChoices))

    class Meta:
        model = CalcRisk
        fields = ()