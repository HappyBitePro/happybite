from django.contrib.auth.models import User
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse

from donation.models import *
from donation.forms import *


class TestdonationViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.factory = RequestFactory()
        self.donation_all_url = reverse('donation:donation_list')
        self.donation_map_url = reverse('donation:map', args=[1], )
        self.donation_reserve_url = reverse('donation:ReserveDonation', args=[1], )
        self.donation_detiles_url = reverse('donation:donation_detail', args=[1], )
        self.donor_donation_url = reverse('donation:donor_donation_profile', args=[1], )
        # self.bene_add_url = reverse('beneficiary:add_beneficiary')

        self.donation = Donation.objects.create(Name='dona',
                                                description='dona',
                                                Packing_Type='Packed',
                                                Deliver_Type='Delivery',
                                                Expiry_Date=datetime.datetime.now(),
                                                lang=2,
                                                lat=5)
        self.donation.save()

    def test_ViewDonationlist(self):
        self.client.login(username='test', password='Aa123456!')
        response = self.client.get(self.donation_all_url)

        self.assertEqual(response.status_code, 302)

    def test_ViewDonationDetils(self):
        self.client.login(username='test', password='Aa123456!')
        response = self.client.get(self.donation_detiles_url)

        self.assertEqual(response.status_code, 302)

    def test_mapDonation(self):
        self.client.login(username='test', password='Aa123456!')
        response = self.client.get(self.donation_map_url)

        self.assertEqual(response.status_code, 200)

    def test_ReserveDonation(self):
        user = User.objects.create_user('test', 'test@test.com', 'Aa123456!')
        user.save()
        self.donation = Donation.objects.create(Name='dona',
                                                description='dona',
                                                Packing_Type='Packed',
                                                Deliver_Type='Delivery',
                                                Expiry_Date=datetime.datetime.now(),
                                                lang=2,
                                                lat=5)
        self.donation.save()
        self.CharityProfile = CharityProfile.objects.create(
            user=user,
            name='tsttest',
            Charity_Slug='test',
            license_image='http://placehold.it/900x400',
            address='Amman',
            Charity_Phone_Number='+962790677851',
        )
        self.CharityProfile.save()

        self.client.login(username='test', password='Aa123456!')
        response = self.client.get(self.donation_reserve_url, follow=True)

        self.assertEqual(response.status_code, 200)
