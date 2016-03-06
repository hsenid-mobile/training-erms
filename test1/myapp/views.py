from django.shortcuts import render
from .models import PersonInfo, LogMode
from .forms import LogForm

# Database display
def display(request):
    form = PersonInfo.objects.all()
    context = {
        'form' : form,
    }
    return render(request, 'display.html', context)

def home(request):
    loginForm = LogForm()
    context = {
        'loginForm' : loginForm,
    }
    return render(request, 'home.html', context)
