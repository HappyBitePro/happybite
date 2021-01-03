from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CharityProfile , DonorProfile


user_type = (
    ('Donor', 'Donor'),
    ('Charity', 'Charity'),
)



class SignupForm(UserCreationForm):
    typee= forms.ChoiceField(choices=user_type)
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'typee'
        ]









class CharityUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= '__all__'


class CharityProfileForm(forms.ModelForm):
    class Meta:
        model = CharityProfile
        fields = '__all__'



class mydonations(forms.ModelForm):
    class Meta:
        model = CharityProfile
        fields = '__all__'









class DonorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email']


class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields = "__all__"