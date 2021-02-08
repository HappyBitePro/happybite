from django.shortcuts import get_object_or_404, redirect, render
from .models import Beneficiary
from .forms import bene_form
from accounts.models import CharityProfile
from django.contrib.auth.decorators import login_required


@login_required
def all_beneficiary(request):
    charity = get_object_or_404(CharityProfile, user=request.user)
    bene_list = Beneficiary.objects.filter(user_id=charity.id)
    ben = bene_form()
    if request.method == 'POST':
        add_beneficiary(request)
    context = {'bene_list': bene_list,
               'ben': ben
               }
    return render(request, 'bene_list.html', context)


@login_required
def beneficiary_detail(request, id):
    bene_detail = Beneficiary.objects.get(id=id)
    context = {
        'bene_detail': bene_detail,

    }
    return render(request, 'bene_detail.html', context)


@login_required
def add_beneficiary(request):
    charity = get_object_or_404(CharityProfile, user=request.user)

    if request.method == 'POST':
        ben = bene_form(request.POST, request.FILES)
        if ben.is_valid():
            ben = ben.save(commit=False)
            ben.user = charity
            ben.save()
            return redirect('beneficiary:add_beneficiary')
    else:
        ben = bene_form()
    context = {
        'ben': ben,

    }
    return render(request, 'add_bene.html', context)


@login_required
def edit_beneficiary(request, id):
    bene = get_object_or_404(Beneficiary, id=id)
    if request.method == 'POST':
        form = bene_form(request.POST, instance=bene)
        if form.is_valid():
            new_form = form
            new_form.save()
            return redirect('beneficiary:bene_list')
    else:
        form = bene_form(instance=bene)
    return render(request, 'edit_bene.html', {'form': form, 'bene': bene})


@login_required
def delete_beneficiary(request, id):
    get_object_or_404(Beneficiary, id=id).delete()
    return redirect('beneficiary:bene_list')
