from django.shortcuts import get_object_or_404, redirect, render
from .models import Beneficiary
from .form import bene_form
from accounts.models import CharityProfile


def all_beneficiary(request):
    
    bene_list = CharityProfile.objects.filter(user = request.user)
    

    context = {
        
        'bene_list' : bene_list , 
    }
    
    return render(request , 'bene_list.html',context)

def beneficiary_detail(request,id):
    
    bene_detail = Beneficiary.objects.get(id=id)
   
    context = {
        # job the name of view in the template
        'bene_detail' : bene_detail ,
        
        }
    #render : renders the database results with the templates
    return render(request , 'bene_detail.html' , context)

def add_beneficiary(request):
    if request.method == "POST": 
        form = bene_form(request.POST) 
        if form.is_valid() :
            myform = form.save(commit=False) #dont  save
            #myform.user = request.user
            #myform.save()
            return redirect('beneficiary:bene_list')
            
    else : 
        form = bene_form()
    
    return render(request , 'add_bene.html' , {'form' : form } )


def edit_beneficiary(request,id):
      bene_profile = get_object_or_404(Beneficiary,id = id) 
      if request.method == 'POST' :
          form = bene_form(request.POST, instance=bene_profile) 
          if form.is_valid(): 
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('beneficiary:bene_list')
      else : 
        form = bene_form(instance=bene_profile) 

      return render(request , 'add_bene.html',{'form':form })

def delete_beneficiary(request,id):
    bene = Beneficiary.objects.get(Beneficiary , id = id )
    bene.delete()
    return render ('beneficiary:bene_list')
    