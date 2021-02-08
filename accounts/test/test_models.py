from unittest import TestCase
from accounts.models import CharityProfile, DonorProfile
from django.contrib.auth.models import User


class TestCharityProfile(TestCase):
    def test_save(self):
        user = User.objects.create_user('testuser', 'test@gmail.com', 'Aa123456!')
        user.save()

        chaity = CharityProfile.objects.create(
            user=user,
            name='testch',
            Charity_Phone_Number='+962795865955',
            address='amman',
            license_image='http://placehold.it/900x400',
        )
        chaity.save()

        self.assertTrue(isinstance(chaity, CharityProfile))


class TestDonorProfile(TestCase):
    def test_save(self):
        user = User.objects.create_user('test', 'test@gmail.com', 'Aa123456!')
        user.save()

        donor = DonorProfile.objects.create(
            user=user,
            Donar_Employment_Type='resturant',
            Donor_Phone_Number='+962795865955',
            address='Amman',

        )
        donor.save()

        self.assertTrue(isinstance(donor, DonorProfile))
