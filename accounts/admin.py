from django.contrib import admin

# Register your models here.
from .models import DonorProfile , CharityProfile


admin.site.register(DonorProfile)
admin.site.register(CharityProfile)