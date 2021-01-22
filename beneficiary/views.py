from django.shortcuts import get_object_or_404, redirect, render
from .models import Beneficiary
from .form import bene_form
from accounts.models import CharityProfile

def all_beneficiary(request):
      
    bene_list = Beneficiary.objects.all()
    

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
    bene = get_object_or_404(CharityProfile , user = request.user)

    if request.method == "POST": 
        form = bene_form(request.POST) 
        if form.is_valid() :
            myform = form.save(commit=False) #dont  save
            myform.save()
            return redirect('beneficiary:bene_list')
            
    else : 
        form = bene_form()
    
        return render(request , 'add_bene.html' , {'form' : form } )


def edit_beneficiary(request,id):
      bene = get_object_or_404(Beneficiary,id=id) 
      if request.method == 'POST' :
          form = bene_form(request.POST, instance=bene) 
          if form.is_valid(): 
            new_form = form
            new_form.save()
            return redirect('beneficiary:bene_list')
      else : 
        form = bene_form(instance=bene) 

      return render(request , 'add_bene.html',{'form':form })

def delete_beneficiary(request,id):
    pass