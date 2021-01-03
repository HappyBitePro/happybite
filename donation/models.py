from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
from accounts.models import CharityProfile , DonorProfile


# Create your models here.

Packing_Type = (
    ('Packed','Packed'),
    ('Not Packed','Not Packed'),
)

Deliver_Type = (
    (' Delivery',' Delivery'),
    ('No Delivery','No Delivery'),
)


class Donation(models.Model):
    donor         = models.ForeignKey( DonorProfile , on_delete=models.CASCADE,blank=True,null=True)
    charity       = models.ForeignKey( CharityProfile , on_delete=models.CASCADE ,blank=True,null=True)
    Name          = models.CharField(max_length=20,)
    Slug          = models.SlugField(blank=True, null=True)
    Food_Type     = models.CharField(max_length=20,)
    Packing_Type  = models.CharField(max_length=15 , choices=Packing_Type)
    Deliver_Type  = models.CharField(max_length=15 , choices=Deliver_Type)
    Donate_Date   = models.DateTimeField(blank=True, default = datetime.datetime.now)
    Expiry_Date   = models.DateTimeField()
    Available     = models.BooleanField(default=True)





    def save(self, *args, **kwargs):
      if not self.Slug:
          self.Slug = slugify(self.Name)
      super(Donation , self).save(*args , **kwargs)

    def __str__(self):
        return self.Name