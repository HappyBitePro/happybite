#from rest_framework import status

from .models import DonorProfile
from donation.models import Donation
from .serializers import *
#from rest_framework.response import Response
#from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

'''
@api_view(['GET'])
def donor_profile_api(request, id):
    Donor_Profile = DonorProfile.objects.get(id=id)
    data = DonorSerializer(Donor_Profile, many=False).data
    return Response({'data': data})


@api_view(['GET'])
def donor_donation_api(request, id):
    donar = get_object_or_404(DonorProfile, id=id)
    donar_Donation = Donation.objects.filter(donor_id=donar.id)
    data = DonationSerializer(donar_Donation, many=True).data
    return Response({'data': data})


@api_view(['GET', 'POST'])
def donor_profile_edit_api(request, id):
    Donor_Profile = DonorProfile.objects.get(user=request.user)
    if request.method == 'GUT':
        userform = User.objects.get(id=request.user.id)
        profileform = DonorProfile.objects.get(id=id)
        serializer_user = DonorUserForm(userform, many=False).data
        serializer_profile_user = DonorProfileForm(profileform, many=False).data

        return Response({'serializer_profile_user': serializer_profile_user, 'serializer_user': serializer_user})
    elif request.method == 'POST':
        userform = User.objects.get(id=request.user.id)
        profileform = DonorProfile.objects.get(id=id)
        serializer_user = DonorUserForm(userform, many=False).data
        serializer_profile_user = DonorProfileForm(profileform, many=False).data

        if serializer_user.is_valid() and serializer_profile_user.is_valid():
            serializer_user.save()
            serializer_profile_user.save()
            return Response({'serializer_profile_user': serializer_profile_user, 'serializer_user': serializer_user})
    else:
        userform = User.objects.get(id=request.user.id)
        profileform = DonorProfile.objects.get(id=id)
        serializer_user = DonorUserForm(userform, many=False).data
        serializer_profile_user = DonorProfileForm(profileform, many=False).data

    return Response({'serializer_profile_user': serializer_profile_user, 'serializer_user': serializer_user}) '''
