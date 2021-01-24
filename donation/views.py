from django.shortcuts import render

from .forms import DonationForm
from .models import Donation
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import CharityProfile, DonorProfile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def ViewDonationlist(request):
    donation_list = Donation.objects.filter(Available=True)

    context = {
        'donations': donation_list,
    }
    return render(request, 'donation/donation_list.html', context)

@login_required
def ViewDonationDetils(request, id):
    donation_detail = Donation.objects.get(id=id)
    context = {
        'donation': donation_detail,
    }
    return render(request, 'donation/donation_detail.html', context)


def mapDonation(request, id):
    donationPlace = Donation.objects.get(id=id)
    return render(request, 'maps/map.html', {'card': donationPlace})
