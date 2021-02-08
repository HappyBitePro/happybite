import datetime
from unittest import TestCase
from donation.models import Donation


class Testmodels(TestCase):
    def test_save(self):


        donation = Donation.objects.create(

            Name='dona',
            description='dona',
            Packing_Type='Packed',
            Deliver_Type='Delivery',
            Expiry_Date=datetime.datetime.now(),
            lang=2,
            lat=5
        )
        donation.save()

        self.assertTrue(isinstance(donation, Donation))