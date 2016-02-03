from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from .forms import PersonInfoForm, EducationForm, LoginForm, SampleModeForm
from myapp.models import SampleMode


def login(request):
    form = LoginForm()
    title_head = "Welcome"
    context = {
        "form":form,
        "title_head" : title_head,
    }
    return render(request, "login.html", context)

def sampleMode(request):
    form = SampleModeForm()

    title = "Person Info"
    context = {
        "form_sample" : form,
        "title_sample" : title,
    }
    return render(request, "deo_index.html", context)

def post(reuqest):
    query_results = SampleMode.objects.all()
    context = {
        "query_results" : query_results,
    }
    return render(reuqest, "post.html", context)

def deo(request):
    title= "Data Entry page"
    form = PersonInfoForm()
    form2 = EducationForm()
    context={
        "Temp_title" : title,
        "formPI" : form,
        "form2" : form2,
    }
    return render(request, "deo.html", context)

# def login_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         # Correct password, and the user is marked "active"
#         login(request, user)
#         # Redirect to a success page.
#         # return HttpResponseRedirect("login")
#         return HttpResponseRedirect(redirct_to="login")
#     else:
#         # Show an error page
#         return HttpResponseRedirect("error")

def error(request):
    return render(request, "error_page.html", {})

# def deo(request):
#     form = PersonInfoForm()
#     context={
#         "form" : form,
#     }
#     return render(request, "deo.html", context)

def deoHome(request):
    title= "Data Entry page"
    form = PersonInfoForm()
    context={
        "Temp_title" : title,
        "formPI" : form,
    }
    return render(request ,"deoHome.html", context)
