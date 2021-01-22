from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
from django.contrib.auth.models import User


def image_upload(instance,filename):
    
    image_name , extension = filename.split(".")
    return "{0} ,{1}".format(instance.id,extension)

class CharityProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Charity_Slug = models.SlugField(blank=True, null=True)
    Charity_Phone_Number = PhoneNumberField()
    license = models.ImageField(upload_to=image_upload)
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

    # location


    def save(self, *args, **kwargs):
        if not self.Donor_Slug:
            self.Donor_Slug = slugify(self.user)
        super(DonorProfile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)
