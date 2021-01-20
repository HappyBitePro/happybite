from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


class CharityProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Charity_Slug = models.SlugField(blank=True, null=True)
    Charity_Phone_Number = PhoneNumberField()

    # Charity_Location
    # Charity_license img

    def save(self, *args, **kwargs):
        if not self.Charity_Slug:
            self.Charity_Slug = slugify(self.user)
        super(CharityProfile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)


class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    Donor_Slug = models.SlugField(blank=True, null=True)

    Donar_Employment_Type = models.CharField(max_length=30)
    Donor_Phone_Number = PhoneNumberField()
    address = models.CharField(max_length=30)
    # location

    def save(self, *args, **kwargs):
        self.id = self.user.id
        if not self.Donor_Slug:
            self.Donor_Slug = slugify(self.user)
        super(DonorProfile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)





@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



