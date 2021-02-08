from django.contrib.auth import views as auth_views
from django.urls import include, path , reverse_lazy
from django.views.decorators.csrf import csrf_exempt


from . import views
from . import api

app_name = 'accounts'

urlpatterns = [


    path('signup', views.signup, name='signup'),

    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # path('signup', views.CharitySignup, name='CharitySignup'),
    path('CharityProfile', views.CharityProfileView, name='CharityProfileView'),
    path('CharityProfile/edit', views.CharityProfileEdit, name='CharityProfileEdit'),
    path('CharityDonation', views.CharityDonationView, name='CharityDonationView'),

    # path('DonorDonation', views.DonorDonationView, name='DonorDonation'),
    #
    # path('donorProfile', views.DonorProfileView, name='DonorProfileView'),
    # path('donorProfile/edit', views.DonorProfileEdit, name='DonorProfileEdit'),






    path('api/signup', api.signup_user, name='signup_user'),  #
    path('api/login', api.CustomObtainAuthToken.as_view(), name='apilogin'),  #
    path('api/donorprofileupdate/<int:id>', api.donor_profile_update_api, name='donorprofileedit'),  #
    path('api/userupdate/<int:id>', api.user_update, name='userupdate'),
    path('api/donorprofile/<int:id>', api.donor_profile_api, name='donorprofileapi'),  #
    path('api/userprofile/<int:id>', api.user_profile, name='userprofile'),  #
    path('api/donordonation/<int:id>', api.donor_donation_api, name='donordonation'), #




]
