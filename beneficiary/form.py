from django import forms
from .models import Beneficiary

#form is used to pass data to the model from the user
#forms.modelform cuz we have a model
class bene_form(forms.ModelForm):
    class Meta:
        model = Beneficiary #the model name
        #model columns that we want to view in form
        fields = ['name','phone_number','family_memebers_numbers','address','work_status','salary']