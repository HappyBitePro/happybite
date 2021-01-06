from django.urls import path
from . import views, CharityViews, DonorViews

app_name = 'donation'

urlpatterns = [

    path('', views.ViewDonationlist, name='donation_list'),
    path('<str:Slug>', views.ViewDonationDetils, name='donation_detail'),

    path('reserve/<int:id>', CharityViews.ReserveDonation, name='ReserveDonation'),
    path('deleteCharity/<int:id>', CharityViews.DeleteDonationCharity, name='DeleteDonationCharity'),

    path('edit/<int:id>', DonorViews.EditDonationDonor, name='EditDonationDonor'),
    path('deleteDonor/<int:id>', DonorViews.DeleteDonationDonor, name='DeleteDonationDonor'),
    path('add/', DonorViews.AddDonationDonor, name='AddDonationDonor'),

]
