import unittest
from unittest import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from accounts.views import *


class TestUrls(TestCase):
    def testLoginView(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def testLogoutView(self):
        url = reverse('accounts:logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

    def testPasswordChangeView(self):
        url = reverse('accounts:password_change')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordChangeView)

    def testPasswordChangeDoneView(self):
        url = reverse('accounts:password_change_done')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordChangeDoneView)

    def testPasswordResetView(self):
        url = reverse('accounts:password_reset')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetView)

    def testPasswordResetDoneView(self):
        url = reverse('accounts:password_reset_done')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetDoneView)

    def testPasswordResetConfirm(self):
        url = reverse('accounts:password_reset_confirm', args=[1, 2])
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetConfirmView)

    def testPasswordResetCompleteView(self):
        url = reverse('accounts:password_reset_complete')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetCompleteView)

    def testSignupView(self):
        url = reverse('accounts:signup')
        self.assertEqual(resolve(url).func, signup)

    def testCharityProfileView(self):
        url = reverse('accounts:CharityProfileView')
        self.assertEqual(resolve(url).func, CharityProfileView)

    def testCharityProfileEditView(self):
        url = reverse('accounts:CharityProfileEdit')
        self.assertEqual(resolve(url).func, CharityProfileEdit)

    def testCharityDonationView(self):
        url = reverse('accounts:CharityDonationView')
        self.assertEqual(resolve(url).func, CharityDonationView)


