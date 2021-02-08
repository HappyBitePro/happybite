from django.contrib.auth.models import User
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse

from beneficiary.models import *
from beneficiary.forms import *


class TestBeneficiaryViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.factory = RequestFactory()
        self.bene_all_url = reverse('beneficiary:bene_list')
        self.bene_detiles_url = reverse('beneficiary:bene_detail', args=[1], )
        self.bene_add_url = reverse('beneficiary:add_beneficiary')

        self.ben = Beneficiary.objects.create(name='bene', phone_number='+96279067781', family_memebers_numbers=2,
                                              address='amman', salary=500)
        self.ben.save()

    def test_bene_all_view(self):
        self.client.login(username='test', password='Aa123456!')
        response = self.client.get(self.bene_all_url)

        self.assertEqual(response.status_code, 302)

    def test_bene_detiles_view(self):
        self.client.login(username='test', password='Aa123456!')
        response = self.client.get(self.bene_detiles_url)

        self.assertEqual(response.status_code, 302)

    def test_bene_add_get(self):
        user = User.objects.create_user('test', 'test@test.com', 'Aa123456!')
        user.save()
        self.ben = Beneficiary.objects.create(name='bene', phone_number='+96279067781', family_memebers_numbers=2,
                                              address='amman', salary=500)
        self.ben.save()
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
        response = self.client.get(self.bene_add_url, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_bene_add_post(self):
        user = User.objects.create_user('test', 'test@test.com', 'Aa123456!')
        user.save()
        self.ben = Beneficiary.objects.create(name='bene', phone_number='+96279067781', family_memebers_numbers=2,
                                              address='amman', salary=500)
        self.ben.save()
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
        response = self.client.post(self.bene_add_url, follow=True)

        self.assertEqual(response.status_code, 200)

    def testUpdateProduct(self):
        user = User.objects.create_user('test', 'test@test.com', 'Aa123456!')
        user.save()
        self.ben = Beneficiary.objects.create(name='bene', phone_number='+96279067781', family_memebers_numbers=2,
                                              address='amman', salary=500)
        self.ben.save()
        self.CharityProfile = CharityProfile.objects.create(
            user=user,
            name='tsttest',
            Charity_Slug='test',
            license_image='http://placehold.it/900x400',
            address='Amman',
            Charity_Phone_Number='+962790677851',
        )
        self.CharityProfile.save()

        bene_edit_url = reverse(
            'beneficiary:edit_beneficiary',
            args=[self.ben.id]
        )

        self.client.login(username='test', password='Aa123456!')
        response = self.client.get(bene_edit_url, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_bene.html')
