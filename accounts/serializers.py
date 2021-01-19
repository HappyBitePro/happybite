from django.contrib.auth.models import User
from rest_framework import serializers

from .models import DonorProfile
from donation.models import Donation


# class Donor_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = DonorProfile
#         fields = '__all__'


class Donation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'charity', 'Name', 'Food_Type', 'Packing_Type', 'Deliver_Type', 'Expiry_Date','Available']


class Donor_User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']


class Donor_Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DonorProfile
        fields = ['Donar_Employment_Type', 'Donor_Phone_Number']


class Signup_Serializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'first_name', 'last_name']
        extra_kwargs = {
            "password": {'write_only': True}
        }

    def save(self):
        user = User(

            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"password": "password must match."})
        user.set_password(password)
        user.save()
        return user
