from .models import Donation
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import CharityProfile ,DonorProfile

@login_required
def ReserveDonation(request, id):
    charity = get_object_or_404(CharityProfile, user=request.user)
    donation = get_object_or_404(Donation, id=id)
    donation.charity = charity
    donation.Available = False
    donation.save()
    return redirect('donation:donation_list')

@login_required
def donor_donation_profile(request ,id):
    donation = get_object_or_404(Donation, id=id)
    donor = DonorProfile.objects.get(id=donation.donor.id)
    return render(request, 'donation/DonorDonationProfile.html', {'donor': donor, })

@login_required
def DeleteDonationCharity(request, id):
    charity = get_object_or_404(CharityProfile, user=request.user)
    donation = get_object_or_404(Donation, id=id)
    donation.charity = None
    donation.Available = True
    donation.save()
    return redirect('accounts:CharityDonationView')
