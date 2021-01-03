from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class CharityProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Charity_Slug = models.SlugField(blank=True, null=True)
    Charity_Phone_Number = PhoneNumberField()

    # Charity_Location
    # Charity_license img
    #  Charity_Donations_list = models.ForeignKey( Donation , on_delete=models.CASCADE , blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.Charity_Slug:
            self.Charity_Slug = slugify(self.user)
        super(CharityProfile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)


class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    Donor_Slug = models.SlugField(blank=True, null=True)

    Donar_Employmenr_Type = models.CharField(max_length=30)
    Donor_Phone_Number = PhoneNumberField()

    # location
    # Donor_Donations_list = models.ForeignKey( Donation , on_delete=models.CASCADE , blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.Donor_Slug:
            self.Donor_Slug = slugify(self.user)
        super(DonorProfile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)
