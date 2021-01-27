from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class Donation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'Name', 'description', 'Packing_Type', 'Deliver_Type', 'Expiry_Date' ]


class Donation_Add_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['donor', 'Name', 'description', 'Packing_Type', 'Deliver_Type', 'Expiry_Date','lang','lat']



class Donation_Update_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['Name', 'description', 'Packing_Type', 'Deliver_Type', 'Expiry_Date','lang','lat']
