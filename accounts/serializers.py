from rest_framework import serializers
from .models import *
from donation.models import Donation


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorProfile
        fields = '__all__'


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['Name', 'Food_Type', 'Packing_Type', 'Deliver_Type', 'Expiry_Date']


class DonorUserForm(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class DonorProfileForm(serializers.ModelSerializer):
    class Meta:
        model = DonorProfile
        fields = ['id','Donar_Employment_Type', 'Donor_Phone_Number']
