from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import *
from accounts.forms import SignupForm
from donation.models import *


class TestSignUpView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.signupurl = reverse('accounts:signup')


    def test_form_valid(self):
        form_data = {
            'username': 'test',
            'password1': 'Aa123456!',
            'password2': 'Aa123456!',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@gmail.com',

        }

        form = SignupForm(form_data)
        self.assertTrue(form.is_valid())

    def test_get(self):
        response = self.client.get(self.signupurl)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Signup.html')


class TestCharityProfileViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        user = User.objects.create_user('test', 'test@test.com', 'Aa123456!')
        user.save()

        self.user = user
        self.CharityProfile = CharityProfile.objects.create(
            user=self.user,
            name='tsttest',
            Charity_Slug='test',
            license_image='http://placehold.it/900x400',
            address='Amman',
            Charity_Phone_Number='+962790677851',
        )
        self.CharityProfile.save()

        self.CharityProfile_url = reverse('accounts:CharityProfileView')
        self.charity_profile_edit_url = reverse('accounts:CharityProfileEdit')
        self.charity_donation_url = reverse('accounts:CharityDonationView')

    def test_charity_profile_view(self):
        self.client.login(username='test', password='Aa123456!')
        response = self.client.get(self.CharityProfile_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'charityprofile.html')

    def test_charity_profile_edit_view(self):
        self.client.login(username='test', password='Aa123456!')
        response = self.client.get(self.charity_profile_edit_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, '404.html')

    def test_charity_donation_view(self):
        self.client.login(username='test', password='Aa123456!')
        response = self.client.get(self.charity_donation_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, '404.html')
