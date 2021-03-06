from django.contrib import admin
from django.urls import path , include
from . import views

#we must add the app name after using the urls in the temaplate
app_name = 'beneficiary'

urlpatterns = [
    path('',views.all_beneficiary, name = 'bene_list') ,
    path('<int:id>',views.beneficiary_detail, name = 'bene_detail') ,
    path('add',views.add_beneficiary, name = 'add_beneficiary') ,
    path('edit_bene/<int:id>',views.edit_beneficiary, name = 'edit_beneficiary') ,
    path('del_bene/<int:id>',views.delete_beneficiary, name = 'delete_beneficiary') ,
]