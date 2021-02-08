import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from donation.forms import *


class Testbene_form(TestCase):
    def test_valid_form(self):
        form = DonationForm(
            data={

                'Name': 'test',
                'description': 'sacascasc',
                'Packing_Type': 'Packed',
                'Deliver_Type': 'Delivery',
                'Expiry_Date': '2',
                'family_memebers_numbers': datetime.datetime.now(),
                'lang': '2',
                'lat': '2',
            })
        self.assertFalse(form.is_valid())

    def test_invalid_form(self):
        form = DonationForm(
            data={
                'Name': 'xxx',
                'description': 'xxx',
                'Packing_Type': 'xxx',
                'Deliver_Type': 'xxx',
                'Expiry_Date': 'xxx',
                'family_memebers_numbers': 'xxx',
                'lang': 'xxx',
                'lat': 'xxx',
            })
        self.assertFalse(form.is_valid())
