from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views
from . import api
app_name = 'accounts'


urlpatterns = [





    path('signup', views.signup, name='signup'),




    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #path('signup', views.CharitySignup, name='CharitySignup'),
    path('CharityProfile', views.CharityProfileView, name='CharityProfileView'),
    path('CharityProfile/edit',views.CharityProfileEdit , name='CharityProfileEdit'),
    path('CharityDonation', views.CharityDonationView, name='mydonations'),


    path('DonorDonation', views.DonorDonationView, name='DonorDonation'),



    path('donorProfile', views.DonorProfileView, name='DonorProfileView'),
    path('donorProfile/edit',views.DonorProfileEdit , name='DonorProfileEdit'),





    #path('api/donorprofile/<int:id>', api.donor_profile_api, name='donorprofileapi'),
    #path('api/donordonation/<int:id>', api.donor_donation_api, name='donorprofileapi'),

    #path('api/donorprofile/edit/<int:id>', api.donor_profile_edit_api, name='donorprofileedit'),

]
