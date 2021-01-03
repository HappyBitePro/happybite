from django.shortcuts import render
from .models import Donation

# Create your views here.






def donation_list(request):
    donation_list = Donation.objects.filter(Available = True)

    context ={
        'donations' : donation_list ,
    }
    return render(request ,'donation/donation_list.html' ,context )





def donation_detail(request , Slug):
    donation_detail = Donation.objects.filter(Slug=Slug)

    context ={
        'donation' : donation_detail ,
    }
    return render(request ,'donation/donation_detail.html' ,context )

def add ():
    pass



def edit ():
    pass


def delete():
    pass# from donar