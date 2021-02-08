from unittest import TestCase

from beneficiary.models import Beneficiary


class TestOffer(TestCase):
    def test_save(self):
        bene = Beneficiary.objects.create(name='bene', phone_number='+96279067781', family_memebers_numbers=2,
                                              address='amman', salary=500)
        bene.save()

        self.assertTrue(isinstance(bene, Beneficiary))