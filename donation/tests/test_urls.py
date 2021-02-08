import unittest
from unittest import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from donation.views import *
from donation.CharityViews import *


class TestUrls(TestCase):
    def test_donation_list_View(self):
        url = reverse('donation:donation_list')
        self.assertEqual(resolve(url).func, ViewDonationlist)
    def test_donation_detail_View(self):
        url = reverse('donation:donation_detail' ,args=[1],)
        self.assertEqual(resolve(url).func, ViewDonationDetils)

    def test_reserve_donation_View(self):
        url = reverse('donation:ReserveDonation',args=[1],)
        self.assertEqual(resolve(url).func, ReserveDonation)
    def test_delete_donation_View(self):
        url = reverse('donation:DeleteDonationCharity',args=[1],)
        self.assertEqual(resolve(url).func, DeleteDonationCharity)

    def test_donor_donations_View(self):
        url = reverse('donation:donor_donation_profile',args=[1],)
        self.assertEqual(resolve(url).func, donor_donation_profile)

    def test_map_donations_View(self):
        url = reverse('donation:map',args=[1],)
        self.assertEqual(resolve(url).func, mapDonation)


