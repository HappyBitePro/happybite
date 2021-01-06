from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Beneficiary(models.Model):
    name = models.CharField( max_length=25)
    phone_number = PhoneNumberField(blank = True)
    family_memebers_numbers = models.IntegerField(default=1)
    address = models.CharField( max_length=50)
    age = models.IntegerField(default= 0 )
    state = (
        ('single','single'),
        ('married','married'),
    )
    social_state = models.CharField(choices = state , max_length=15)
    JobType = (
        ('unemployed','unemployed'),
        ('employed','employed'),
    )
    work_status = models.CharField(choices = JobType, max_length=15)
    salary = models.IntegerField(default= 0)
    
    
    
    def __str__(self):
        return self.name


