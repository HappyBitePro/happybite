from .forms import DonationForm
from .models import Donation
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import DonorProfile


def AddDonationDonor(request):
    donor = get_object_or_404(DonorProfile, user=request.user)

    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.donor = donor
            form.save()
            return redirect('donation:donation_list')
    else:
        form = DonationForm()
        return render(request, 'donation/AddDonation.html', {'form': form})


def EditDonationDonor(request, id):
    donor = get_object_or_404(DonorProfile, user=request.user)
    donation = get_object_or_404(Donation, id=id)
    if request.method == 'POST':  # to know if user click on add note button
        form = DonationForm(request.POST, instance=donation)

        if form.is_valid():  # to save form in db ## i write this code becuse give the user evry thing to input it (user , slug ...)
            new_form = form
            new_form.save()
            return redirect('donation:donation_list')

    else:
        form = DonationForm(instance=donation)

    context = {
        'form': form
    }
    return render(request, 'donation/AddDonation.html', context)


def DeleteDonationDonor(request, id):
    donor = get_object_or_404(DonorProfile, user=request.user)
    donation = get_object_or_404(Donation, id=id).delete()
    return redirect('accounts:DonorDonation')
