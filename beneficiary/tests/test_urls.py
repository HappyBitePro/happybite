import unittest
from unittest import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from beneficiary.views import *


class TestUrls(TestCase):
    def test_all_beneficiary_View(self):
        url = reverse('beneficiary:bene_list')
        self.assertEqual(resolve(url).func, all_beneficiary)
    def test_beneficiary_detail_View(self):
        url = reverse('beneficiary:bene_detail' ,args=[1],)
        self.assertEqual(resolve(url).func, beneficiary_detail)

    def test_beneficiary_add_View(self):
        url = reverse('beneficiary:add_beneficiary')
        self.assertEqual(resolve(url).func, add_beneficiary)
    def test_beneficiary_edit_View(self):
        url = reverse('beneficiary:edit_beneficiary',args=[1],)
        self.assertEqual(resolve(url).func, edit_beneficiary)

    def test_beneficiary_delete_View(self):
        url = reverse('beneficiary:delete_beneficiary',args=[1],)
        self.assertEqual(resolve(url).func, delete_beneficiary)


