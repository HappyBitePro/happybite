
from .models import Donation
from django.shortcuts import redirect, get_object_or_404

from .models import CharityProfile




def ReserveDonation(request, id):
    charity = get_object_or_404(CharityProfile, user=request.user)
    donation = get_object_or_404(Donation, id=id)
    donation.charity = charity
    donation.Available = False
    donation.save()
    return redirect('donation:donation_list')

def DeleteDonationCharity(request , id ):
    charity = get_object_or_404(CharityProfile, user=request.user)
    donation = get_object_or_404(Donation, id=id)
    donation.charity=None
    donation.Available=True
    donation.save()
    return redirect('accounts:CharityProfileView')
