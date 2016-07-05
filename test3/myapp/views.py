from django.shortcuts import RequestContext, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import date, datetime
from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.db.models import Q
from .forms import *


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


def interview_view(request, vid):
    context = RequestContext(request)
    vacancy = Vacancy.objects.get(id=vid)
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            form_variable = form.save(commit=False)
            form_variable.save()
            return redirect('/hod/hod_vacancy/test/succs/')
        else:
            print form.errors
    else:
        form = InterviewForm()
    return render(request, 'hod_inter_create.html', {'form': form}, context)


def hod_inter_create(request, vid):
    context = RequestContext(request)
    obj = Vacancy.objects.get(id=vid)
    usr = Users.objects.get(User=request.user)
    if request.method == 'POST':
        inter_form = InterviewForm(request.POST)
        if inter_form.is_valid():
            inter = inter_form.save(commit=False)
            inter.Department = usr.Department
            inter.HOD = request.user
            inter.Vacancy = obj
            inter.InterviewNo = 1
            inter.save()
            return redirect('/hod/hod_vacancy/test/succs/')
        else:
            print inter_form.errors
    else:
        inter_form = InterviewForm()
    return render(request, 'hod_inter_create.html', {'inter_form': inter_form, 'obj': obj, 'vid': vid}, context)


def hod_inter_create_succs(request):
    return render(request, 'hod_inter_create_succs.html', {})


def hod_inter_list_interviewer(request):
    inter = Interview.objects.all()
    return render(request, 'hod_inter_list_inter.html', {'inter': inter})


def hod_pre_interviwer_list(request, iid):
    inter = Interview.objects.get(id=iid)
    a = UserRole.objects.get(Role="Interviewer")
    viewer = Users.objects.filter(UserRole=a.id)
    return render(request, 'hod_inter_create_2.html', {'viewer': viewer, 'inter': inter, 'a':a})


def hod_inter_interviewer_2(request, iid, pid):
    inter = Interview.objects.get(id=iid)
    a = UserRole.objects.get(Role="Interviewer")
    viewer = Users.objects.filter(UserRole=a.id)
    usr_id = Users.objects.get(id=pid)
    usr = User.objects.get(id=usr_id.User_id)
    inter_id = inter
    person_id = usr
    form = Interview_Interviewer(Interview=inter_id, Interviewer=person_id)
    form.save()
    return render(request, 'hod_inter_create_2.html', {'viewer': viewer, 'inter': inter})


def hod_inter_list_cv(request):
    inter = Interview.objects.all()
    return render(request, 'hod_inter_list_cv.html', {'inter': inter})


def hod_pre_cv_list(request, iid):
    inter = Interview.objects.get(id=iid)
    cv = Personal.objects.all()
    return render(request, 'hod_inter_create_3.html', {'cv': cv, 'inter': inter})


def hod_inter_cv(request, iid, pid):
    context = RequestContext(request)
    inter = Interview.objects.get(id=iid)
    cv = Personal.objects.all()
    cv_sp = Personal.objects.get(id=pid)
    form = Personal_Interview(Interview=inter, Personal=cv_sp)
    form.save()
    # if request.method == 'POST':
    #     qual = subQul_Post.objects.get(Post=inter.Post)
    #     sub =  SubQualification.objects.filter(QName__contains=qual.QName)
    #     ex_post = Exp_Post.objects.get(Post=inter.Post)
    #     exp = Experience.objects.filter(Post__contains=ex_post.Post).filter(Duration__contains=ex_post.Duration)
    #     p = Personal_Interview_viewer.objects.filter(Q(CV_Status.objects.get(id=1))|Q(CV_Status.objects.get(id=3))) #1 means pass, 2 means failed , 3 means on hold
    #     y = Interview.objects.filter(InterviewNo=1)
    #     return redirect('/hod/hod_vacancy/test/part2/inter_list/(\d+)/(\d+)/')
    return render(request, 'hod_inter_create_3.html', {'cv': cv, 'inter': inter}, context)


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


def hod_inter_view(request, id):
    inter_obj = Interview.objects.get(id=id)
    viewer = Interview_Interviewer.objects.filter(Interview=inter_obj.id)
    cv = Personal_Interview.objects.filter(Interview=inter_obj.id)
    context = RequestContext(request)
    if request.method == 'POST':
        form = InterReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('/hod/hod_inter/hod_inter_overview/view/(\d+)/')
        else:
            print form.errors
    else:
        form = InterReviewForm()
    return render(request, 'hod_inter_view.html', {'inter_obj': inter_obj, 'viewer': viewer, 'cv': cv, 'form': form}, context)


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


def send_msg(request):
    context = RequestContext(request)
    if request.method == 'POST':
        msg_form = MessageForm(request.POST)
        if msg_form.is_valid():
            msgData = msg_form.save(commit=False)
            msgData.Send = request.user
            msgData.SentDate = now()
            msgData.SentTime = now()
            msgData.save()
            return redirect('/int/send_msg')
        else:
            print(msg_form.errors)
    else:
        msg_form = MessageForm()
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
    usr = request.user
    if request.user.is_authenticated():
        msg = Messages.objects.filter(Recieve=usr.id)
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
