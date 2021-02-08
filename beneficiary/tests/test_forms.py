from django.contrib.auth.models import User
from django.test import TestCase
from beneficiary.forms import *


class Testbene_form(TestCase):
    def test_valid_form(self):
        form = bene_form(
            data={
                'user': 'test',
                'name': 'testemail@gmail.com',
                'phone_number': '+962795379588',
                'address': 'amman',
                'salary': '500',
                'family_memebers_numbers': '2',
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = bene_form(
            data={
                'user': 'xxx',
                'name': 'xxx',
                'phone_number': 'xxx',
                'address': 'xxx',
                'salary': 'xxx',
                'family_memebers_numbers': 'xxx',
        })
        self.assertFalse(form.is_valid())
