from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import RequestContext, redirect
from django.views import generic
from django.views.generic import View
from datetime import date, datetime
from .forms import *

#  Login method
# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return render(request, 'hod.html', {})
#             else:
#                 return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
#         else:
#             return render(request, 'login.html', {'error_message': 'Invalid login'})
#     return render(request, 'login.html', {})
#

# class LoginView(View):
#     loginForm = LoginForm()
#     template_name = 'login.html'

    # display blank form
    # def get(self, request):
    #     form = self.loginForm(None)
    #     return render(request, self.template_name, {'form': form})

    # post data in
    # def post(self, request):
    #     form = self.loginForm(request.POST)
    #     a = User.objects.all()
        # if form.is_valid():
        #     user = form.save(commit=False)
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        #     user.set_password(password)
        #     user.save()
        # returns User objects if credentials are correct
        # user = authenticate(username=a.username, password=a.password)
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         return redirect('/hod/')
    # return render(request, self.template_name, {'form': form})


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def hod(request):
    intr_count = Interview.objects.filter().count()
    vcncy_count = Vacancy.objects.filter().count()
    msg_count = Messages.objects.filter().count()
    cv_count = Personal.objects.filter().count
    context={
        'msg_count': msg_count,
        'cv_count': cv_count,
        'vcncy_count': vcncy_count,
        'intr_count' : intr_count,
    }
    return render(request, 'hod.html', context)


def hod_vacancy(request):
    context = RequestContext(request)
    if request.method == 'POST':
        vacncy_form = VacancyForm(request.POST)
        if vacncy_form.is_valid():
            form = vacncy_form.save(commit=False)
            form.save()
            return redirect('/hod/hod_vacancy/succs/')
        else:
            print vacncy_form.errors
    else:
        vacncy_form = VacancyForm()
    return render(request, 'hod_vacancy.html', {'v_form': vacncy_form}, context)


def hod_vacancy_succs(request):
    return render(request, 'hod_vacancy_succs.html', {})


def hod_vacancy_test(request):
    obj = Vacancy.objects.all()
    return render(request, 'test_vacancy.html', {'obj': obj})


def hod_auto_filter(request):
    return render()


def hod_cv(request):
    form = Personal.objects.all()
    # form2 = Degree.objects.all()
    return render(request, 'hod_cv.html', {'form_cv': form})


def hod_inter(request):
    return render(request, 'hod_inter.html', {})


def hod_inter_choose_vacancy(request):
    vacancy = Vacancy.objects.all()
    context = {
        'Vacn': vacancy,
    }
    return render(request, 'hod_inter_choose_vacancy.html',  context)


def hod_view_vacancy(request, ID):
    obj = Vacancy.objects.get(id=ID)
    return render(request, 'hod_view_vacancy.html', {'obj': obj})


def hod_inter_create(request, vid):
    context = RequestContext(request)
    obj = Vacancy.objects.get(id=vid)
    if request.method == 'POST':
        inter_form = InterviewForm(request.POST)
        if inter_form.is_valid():
            inter = inter_form.save(commit=False)
            inter.save()
            return redirect('/hod/hod_vacancy/test/(?P<vid>[0-9]+)/part2/')
        else:
            print inter_form.errors
    else:
        inter_form = InterviewForm()
    return render(request, 'hod_inter_create.html', {'inter_form': inter_form, 'obj': obj}, context)


def hod_inter_interviewer(request, vid):
    context = RequestContext(request)
    # x =
    if request.method == 'POST':
        inter_form_2 = InterviewForm2(request.POST)
        if inter_form_2.is_valid():
            inter = inter_form_2.save(commit=False)
            inter.save()
            return redirect('/hod/hod_vacancy/test/(?P<vid>[0-9]+)/part2/(?P<cid>[0-9]+)')
        else:
            print inter_form_2.errors
    else:
        inter_form_2 = InterviewForm2()

    return render(request, 'hod_inter_create_2.html', {'inter_form_2': inter_form_2 }, context)


def hod_inter_cv(request, vid, iid, pid):
    context = RequestContext(request)
    person_cv = Personal.objects.all(id=cv)
    if request.method == 'POST':
        cv_form = PersonInterForm(request.POST)
        if cv_form.is_valid():
            h_cv = cv_form.save(commit=False)
            h_cv.personal = pid
            h_cv.Interview = iid
            h_cv.save()
            return redirect('/hod/hod_vacancy/test/(?P<vid>[0-9]+)/part2/(?P<iid>[0-9]+)/(?P<pid>[0-9]+)')
        else:
            print cv_form.errors
    else:
        cv_form = InterviewForm2()

    return render(request, 'hod_inter_create_3.html', {'cv_form': cv_form}, context)


def hod_view_inter(request, ID):
    vacan = Vacancy.objects.get(id=ID)
    cv = Personal.objects.all()
    inter_form_2 = InterviewForm2(request.POST)
    try:
        selected_cv = Personal.objects.get(id=request.POST['cv'])
    except (KeyError, Personal.DoesNotExist):
        return render(request, 'hod_inter_create_2.html', {'error': "Person does not exist"})
    else:
        selected_cv.is_selected = True
        selected_cv.save()
        return render(request, 'hod_inter_create_2.html', {'inter_form_2': inter_form_2, 'cv': cv, 'vacan':vacan})


def hod_succs(request):
    return render(request, 'hod_succs.html', {})


def hod_inter_overview(request):
    inter_obj = Interview.objects.all()
    context={
        'inter_obj': inter_obj,
    }
    return render(request, 'hod_inter_overview.html', context)


def hod_profile(request, NIC):
    try:
        profile = Personal.objects.get(NIC=NIC)
        context = RequestContext(request)
        if request.method == 'POST':
            hod = HodReviewForm(request.POST, request.FILES)
            if hod.is_valid():
                review = hod.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('')
            else:
                print hod.errors
        else:
            hod = HodReviewForm()
    except Personal.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'hod_cv_profile.html', {'hod_form': hod, 'pro_form': profile}, context)


def hod_msg(request):
    return render(request, 'hod_msg.html', {})


def hod_send_msg(request):
    context = RequestContext(request)
    if request.method == 'POST':
        msg_form = HodMessageForm(request.POST)
        if request.user.is_authenticated():
            if msg_form.is_valid():
                msg = msg_form.save(commit=False)
                msg.user = request.user
                msg.save()
                return redirect('/hod/hod_msg/send')
            else:
                print msg_form.errors
    else:
        msg_form = HodMessageForm()
    return render(request, 'hod_send_msg.html', {'msg_form': msg_form}, context)


def hod_msg_succs(request):
    msg_obj = Messages()
    if request.user.is_authenticated():
        username = request.user.username
        msg_obj.Sende = username
        msg_obj.SentDate = date.today()
        msg_obj.SentTime = datetime.time()
        dsc = True
        context = {
            'dsc': dsc,
        }
    else:
        error = 'User authentication error'
        context = {
            'error': error,
        }
    return render(request, 'hod_msg_succs.html', context)


def hod_recieve_msg(request):
    usr = request.user.username
    if request.user.is_authenticated():
        msg = Messages.objects.get(Recieve=usr)
        context = {
            'msg': msg,
        }
    else:
        error = 'User is not Authenticated one.'
        context = {
            'error': error,
        }
    return render(request, 'hod_recieve_msg.html', context)


def deo(request):
    context = RequestContext(request)
    if request.method == 'POST':
        deoForm = PersonForm(request.POST)
        if deoForm.is_valid():
            data = deoForm.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('/deo/deo_submit/')
        else:
            print deoForm.errors
    else:
        deoForm = PersonForm()
    return render(request, 'deo.html', {'deoForm': deoForm}, context)


def deo_submit(request):
    return render(request, 'deo_submit.html', {})


def deo_profile(request):
    profile_form = Personal.objects.all()
    return render(request, 'deo_profile.html', {'profile_form': profile_form})


def date_time(request):
    year = datetime.today()
    return render(request, 'date_time.html', {'year':year})


def subv(request):
    if request.method == 'POST':
        sub = SubForm(request.POST)
        if sub.is_valid():
            form = sub.save(commit=False)
            form.save()
            return redirect('/sub/')
        else:
            print sub.errors
    else:
        sub = SubForm()
    return render(request, 'sub.html', {'sub': sub})
