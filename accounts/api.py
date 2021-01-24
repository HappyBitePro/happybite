from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView

from .models import *
from donation.models import Donation
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404



@api_view(['GET'])
#@permission_classes((IsAuthenticated,))
def donor_profile_api(request, id):
    Donor_Profile = DonorProfile.objects.get(id=id)
    data = Donor_Profile_Serializer(Donor_Profile, many=False).data
    return Response(data)

@api_view(['GET'])
#@permission_classes((IsAuthenticated,))
def donor_donation_api(request, id):
    donar = get_object_or_404(DonorProfile, id=id)
    donar_Donation = Donation.objects.filter(donor_id=donar.id)
    data = Donation_Serializer(donar_Donation, many=True).data
    return Response(data)

@api_view(['PUT'])
#@permission_classes((IsAuthenticated,))
def donor_profile_update_api(request, id):
    try:
        Donor_Profile = DonorProfile.objects.get(id=id)
    except DonorProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer_profile_user = Donor_Profile_Serializer(Donor_Profile, data=request.data)
        data = {}
        if serializer_profile_user.is_valid():
            serializer_profile_user.save()
            data["response"] = "donor profile updated"

            return Response(data=data)
        return Response(serializer_profile_user.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
#@permission_classes((IsAuthenticated,))
def user_profile(request, id):
    users = User.objects.get(id=id)
    data = Donor_User_Serializer(users, many=False).data
    return Response(data)

@api_view(['PUT'])
#@permission_classes((IsAuthenticated,))
def user_update(request,id):
    try:
        users = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        ser = Donor_User_Serializer(users, data=request.data)
        data = {}
        if ser.is_valid():
            ser.save()
            data['response'] = "user profile updated"
            return Response(data=data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup_user(request):
    if request.method == 'POST':
        serializer = Signup_Serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["response"] = "successful"
            data['email'] = user.email
            data['username'] = user.username
            data['first_name'] = user.first_name#we not work
            data['last_name'] = user.last_name
            DonorProfile.objects.create(user=user)
            token =Token.objects.get(user=user).key
            data['token'] = token
            data['id'] = user.id



        else:
            data = serializer.errors
        return Response(data)
