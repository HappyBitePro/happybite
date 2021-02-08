from django.contrib.auth.models import User
from django.test import TestCase
from accounts.forms import *



class TestSignupForm(TestCase):
    def test_valid_form(self):
        form = SignupForm(
            data={
                'username': 'charitytest1',
                'password1': 'Aa123456!',
                'password2': 'Aa123456!',
                'email': 'testch@gmail.com',

            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = SignupForm(data={})

        self.assertFalse(form.is_valid())


class TestCharityProfileForm(TestCase):
    def test_valid_form(self):
        form = CharityProfileForm(
            data={
                'address': 'irbid',
                'name': 'testcharity',
                'Charity_Phone_Number': '+962790677816',
                'license_image': 'http://placehold.it/900x400'
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = CharityProfileForm(data={})
        self.assertFalse(form.is_valid())


class TestCharityUserForm(TestCase):
    def test_valid_form(self):
        form = CharityUserForm(
            data={
                'username': 'testname',
                'email': 'testemail@gmail.com',
                'first_name': 'testf',
                'last_name': 'test2',
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = CharityUserForm(data={
            'username': 'xxx',
            'email': 'xxx',
            'first_name': 'xxx',
            'last_name': 'xxx',
        })
        self.assertFalse(form.is_valid())


class TestDonorUserForm(TestCase):
    def test_valid_form(self):
        form = DonorUserForm(
            data={
                'username': 'testname',
                'email': 'testemail@gmail.com',
                'first_name': 'testf',
                'last_name': 'test2',
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = DonorUserForm(data={
            'username': 'xxx',
            'email': 'xxx',
            'first_name': 'xxx',
            'last_name': 'xxx',
        })
        self.assertFalse(form.is_valid())



