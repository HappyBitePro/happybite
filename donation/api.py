from django.contrib.auth import authenticate
from rest_framework import status

from accounts.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


@api_view(['POST'])
#@permission_classes((IsAuthenticated,))
def donation_add_api(request):
    acc =request.user
    donation = Donation()

    if request.method == 'POST':

        ser = Donation_Add_Serializer(donation, data=request.data)

        ser.donor = acc
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
#@permission_classes((IsAuthenticated,))
def donation_details_api(request, id):
    donation = Donation.objects.get(id=id)
    data = Donation_Serializer(donation, many=False).data
    return Response(data)


@api_view(['PUT'])
#@permission_classes((IsAuthenticated,))
def donation_update_api(request, id):
    try:
        donation = Donation.objects.get(id=id)
    except Donation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = Donation_Update_Serializer(donation, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "donation data updated"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def donation_delete_api(request, id):
    try:
        donation = Donation.objects.get(id=id)
    except Donation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        operation = donation.delete()
        data = {}
        if operation:
            data["success"] = "deleted"
        else:
            data["failure"] = "failed"
        return Response(data=data)
