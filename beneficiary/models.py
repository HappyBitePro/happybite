from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from accounts.models import CharityProfile


class Beneficiary(models.Model):
    user = models.ForeignKey(CharityProfile, on_delete=models.CASCADE ,null=True)
    name = models.CharField(max_length=25)
    phone_number = PhoneNumberField(blank=True)
    family_memebers_numbers = models.IntegerField(default=1)
    address = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        super(Beneficiary, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


