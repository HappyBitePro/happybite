from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CharityProfile , DonorProfile


user_type = (
    ('Donor', 'Donor'),
    ('Charity', 'Charity'),
)



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'

        ]




class CharityUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= fields = ['username','first_name','last_name','email']


class CharityProfileForm(forms.ModelForm):
    class Meta:
        model = CharityProfile
        fields = '__all__'
        exclude = ('Charity_Slug','user')



class DonorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email']


class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields = "__all__"