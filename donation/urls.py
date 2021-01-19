from django.urls import path
from . import views, CharityViews, DonorViews
from . import api
app_name = 'donation'

urlpatterns = [

    path('', views.ViewDonationlist, name='donation_list'),
    path('<int:id>', views.ViewDonationDetils, name='donation_detail'),

    path('reserve/<int:id>', CharityViews.ReserveDonation, name='ReserveDonation'),
    path('deleteCharity/<int:id>', CharityViews.DeleteDonationCharity, name='DeleteDonationCharity'),

    path('edit/<int:id>', DonorViews.EditDonationDonor, name='EditDonationDonor'),
    path('deleteDonor/<int:id>', DonorViews.DeleteDonationDonor, name='DeleteDonationDonor'),
    path('add/', DonorViews.AddDonationDonor, name='AddDonationDonor'),



    path('api/add', api.donation_add_api, name='donation_add'),
    path('api/update/<int:id>', api.donation_update_api, name='donation_update'),
    path('api/<int:id>', api.donation_details_api, name='donation_details'),
    path('api/delete/<int:id>', api.donation_delete_api, name='donation_delete'),
]
