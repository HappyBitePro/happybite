from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import SignupForm, CharityUserForm, CharityProfileForm, mydonations, DonorUserForm, DonorProfileForm
from .models import CharityProfile, DonorProfile
from donation.models import Donation


# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            if form.cleaned_data['typee'] == 'Charity':
                user = authenticate(username=username, password=password)
                CharityProfile.objects.create(user=user)
                login(request, user)
                return redirect('accounts:CharityProfileView')

            elif form.cleaned_data['typee'] == 'Donor':
                user = authenticate(username=username, password=password)
                DonorProfile.objects.create(user=user)
                login(request, user)
                return redirect('accounts:DonorProfileView')

            else:
                raise Http404("Poll does not exist")
    else:
        form = SignupForm()
    return render(request, 'Signup.html', {'form': form})


def CharityProfileView(request):
    Charity_Profile = CharityProfile.objects.get(user=request.user)
    donation = Donation.objects.filter(charity_id=Charity_Profile.id)
    return render(request, 'charityprofile.html', {'profile': Charity_Profile , 'donation': donation})


def CharityProfileEdit(request):
    Charity_Profile = CharityProfile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = CharityUserForm(request.POST, instance=request.user)
        profileform = CharityProfileForm(request.POST, request.FILES, instance=Charity_Profile)
        if CharityUserForm.is_valid() and CharityProfileForm.is_valid():
            CharityUserForm.save()
            myprofile = CharityProfileForm.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('registration:profile'))

    else:
        userform = CharityUserForm(instance=request.user)
        profileform = CharityProfileForm(instance=Charity_Profile)

    return render(request, 'registration/profile_edit.html',
                  {'userform': CharityUserForm, 'profileform': CharityProfileForm})


def CharityDonationView(request):
    y = Donation.objects.filter(charity_id=request.user.id)
    x = CharityProfile.objects.all()
    return render(request, 'mydonations.html', {'x': x, 'y': y})


def DonorProfileView(request):
    Donor_Profile = DonorProfile.objects.get(user=request.user)
    return render(request, 'donorprofile.html', {'profile': DonorProfile})


def DonorProfileEdit(request):
    Donor_Profile = DonorProfile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = DonorUserForm(request.POST, instance=request.user)
        profileform = DonorProfileForm(request.POST, request.FILES, instance=Donor_Profile)
        if DonorUserForm.is_valid() and DonorProfileForm.is_valid():
            DonorUserForm.save()
            myprofile = DonorProfileForm.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('registration:profile'))

    else:
        userform = DonorUserForm(instance=request.user)
        profileform = DonorProfileForm(instance=Donor_Profile)

    return render(request, 'registration/profile_edit.html',
                  {'userform': DonorUserForm, 'profileform': DonorProfileForm})


def DonorDonationView(request):
    print(request.user.id)
    donar = get_object_or_404(DonorProfile, user=request.user)
    donar_Donation = Donation.objects.filter(donor_id=donar.id)

    return render(
        request,
        'donordonation.html',
        {
            'donar':donar ,
            'donar_Donation':donar_Donation ,
        } )
