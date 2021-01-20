from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
from accounts.models import CharityProfile, DonorProfile

# Create your models here.

Packing_Type = (
    ('Packed', 'Packed'),
    ('Not Packed', 'Not Packed'),
)

Deliver_Type = (
    ('Delivery', 'Delivery'),
    ('No Delivery', 'No Delivery'),
)


class Donation(models.Model):
    donor = models.ForeignKey(DonorProfile, on_delete=models.CASCADE, blank=True, null=True)
    charity = models.ForeignKey(CharityProfile, on_delete=models.CASCADE, blank=True, null=True)
    Name = models.CharField(max_length=20, )  # 18 len type _food
    Slug = models.SlugField(blank=True, null=True)
    Food_Type = models.CharField(max_length=20, )  # descriptions 100
    Packing_Type = models.CharField(max_length=15, choices=Packing_Type)
    Deliver_Type = models.CharField(max_length=15, choices=Deliver_Type)
    Donate_Date = models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False)
    Expiry_Date = models.DateTimeField()
    Available = models.BooleanField(default=True)

    lang = models.FloatField(max_length=15,null=True)
    lat = models.FloatField(max_length=15,null=True)

    def save(self, *args, **kwargs):
        if not self.Slug:
            self.Slug = slugify(self.Name)
        super(Donation, self).save(*args, **kwargs)

    def __str__(self):
        self.expiry_date_delete
        return self.Name

    @property
    def expiry_date_delete(self):
        if self.Expiry_Date.date() <= datetime.datetime.now().date():
            self.delete()
