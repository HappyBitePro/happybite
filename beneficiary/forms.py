from django import forms
from .models import Beneficiary


class bene_form(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields= '__all__'
        exclude = ('Slug', 'user')
