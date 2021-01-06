from django.shortcuts import redirect, render
from .models import Beneficiary
from .form import bene_form

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
    
    if request.method == "POST": 
        form = bene_form(request.POST) 
        if form.is_valid :
            myform = form.save(commit=False) #dont  save
            myform.save()
            return redirect('beneficiary:bene_list')
            
    else : 
        form = bene_form()

    
    return render(request , 'add_bene.html' , {'form' : form } )


