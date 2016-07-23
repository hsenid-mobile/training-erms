from django.shortcuts import render
from .models import *
    # , Basic_Info
from .forms import *

# Database display
# def display(request):
#     form = Person_Info.objects.all()
#     # form2 = Basic_Info.objects.all()
#     context = {
#         'form' : form,
#         # 'form2' : form2,
#     }
#     return render(request, 'display.html', context)

def login(request):
    loginForm = LoginForm()
    context = {
        'loginForm':loginForm,
    }
    return render(request, 'login.html', context)

def hod(request):
    return render(request, 'hod.html', {})

def hod_cv(request):
    form = Person.objects.all()
    context={
        'form_cv':form,
    }
    return render(request, 'hod_cv.html', context)

def deo(request):
    deoForm = Interview_Form()
    context = {
        'deoForm':deoForm,
    }
    return render(request, 'deo.html', context)

def hod_inter(request):
    Inter_form = Person.Objects.all()
    context = {
        'inter_form' : Inter_form,
    }
    return  render(request, 'hod_inter.html', context)