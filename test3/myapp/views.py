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
    cv_count = Personal_Post_Dept.objects.filter().count
    context={
        'msg_count': msg_count,
        'cv_count': cv_count,
        'vcncy_count': vcncy_count,
        'intr_count' : intr_count,
    }
    return render(request, 'hod.html', context)


def hod_post_list(request):
    usr = Users.objects.get(User=request.user)
    post_dept = Post_Dept.objects.filter(Dept=usr.Department)
    return render(request, 'hod_post_list.html', {'post': post_dept})


def hod_vacan_list(request):
    usr = Users.objects.get(User=request.user)
    post_dept = Post_Dept.objects.filter(Dept=usr.Department)
    obj = Vacancy.objects.all()
    return render(request, 'test_vacancy.html', {'obj': obj})


def hod_vacancy(request, vid):
    context = RequestContext(request)
    if request.method == 'POST':
        vacncy_form = VacancyForm(request.POST)
        if vacncy_form.is_valid():
            form = vacncy_form.save(commit=False)
            form.Post_Dept_id = vid
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
    usr = Users.objects.get(User=request.user)
    pdept = Post_Dept.objects.filter(Dept=usr.Department)
    inter = Interview.objects.filter(Department=usr.Department)
    vacan = Vacancy.objects.all()
    return render(request, 'test_vacancy.html', {'vacan': vacan, 'pdept': pdept, 'inter':inter})


def hod_cv(request):
    usr = Users.objects.get(User=request.user)
    post_dept = Post_Dept.objects.filter(Dept=usr.Department)
    return render(request, 'hod_cv.html', {'post': post_dept})


def hod_cv_list(request, post_id):
    post_dept = Post_Dept.objects.get(id=post_id)
    form_cv = Personal_Post_Dept.objects.filter(Post_Dept=post_dept)
    return render(request, 'hod_cv_list.html', {'cv': form_cv})


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
    post = Post_Dept.objects.get(id=obj.Post_Dept_id)
    usr = Users.objects.get(User=request.user)
    if request.method == 'POST':
        inter_form = InterviewForm(request.POST)
        if inter_form.is_valid():
            inter = inter_form.save(commit=False)
            inter.Department = usr.Department
            inter.HOD = request.user
            inter.Post = post.Post
            inter.Vacancy = obj
            inter.InterviewNo=inter.InterviewNo + 1
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
    usr = Users.objects.get(User=request.user)
    inter = Interview.objects.filter(Department=usr.Department)
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
    usr = Users.objects.get(User=request.user)
    inter = Interview.objects.filter(Department=usr.Department)
    return render(request, 'hod_inter_list_cv.html', {'inter': inter})


def hod_pre_cv_list(request, iid):
    inter = Interview.objects.get(id=iid)
    vacan = Vacancy.objects.get(Post_Dept_id=inter.Vacancy.Post_Dept.id)
    usr = Users.objects.get(User=request.user)
    pdept = Post_Dept.objects.get(Dept=usr.Department, Post=vacan.Post_Dept.Post)
    person_dept = Personal_Interview.objects.filter(Interview=inter)
    exp = Exp_Post.objects.filter(Post=pdept.Post)
    xpost = Experience.objects.all()
    return render(request, 'hod_inter_create_3.html', {'xperince': xpost, 'inter': inter, 'exp': exp, 'pdept':pdept, 'person_dept':person_dept})


def hod_inter_cv(request, iid, pid):
    inter = Interview.objects.get(id=iid)
    vacan = Vacancy.objects.get(Post_Dept_id=inter.Vacancy.Post_Dept.id)
    usr = Users.objects.get(User=request.user)
    pdept = Post_Dept.objects.get(Dept=usr.Department, Post=vacan.Post_Dept.Post)
    person_dept = Personal_Interview.objects.filter(Interview=inter)
    exp = Exp_Post.objects.filter(Post=pdept.Post)
    xpost = Experience.objects.all()
    cv_sp = Personal.objects.get(id=pid)
    form = Personal_Interview(Interview=inter, Personal=cv_sp)
    form.save()
    return render(request, 'hod_inter_create_3.html', {'xperince': xpost, 'inter': inter, 'exp': exp, 'pdept':pdept, 'person_dept':person_dept})


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


def hod_pre_inter_vacancy_overview(request):
    usr = Users.objects.get(User=request.user)
    pd = Post_Dept.objects.filter(Dept=usr.Department)
    vacan = Vacancy.objects.all()
    context = {
        'vacan': vacan,
        'pd': pd,
    }
    return render(request, 'hod_pre_inter_vacancy_overview.html', context)


def hod_inter_overview(request, vid):
    usr = Users.objects.get(User=request.user)
    inter_obj = Interview.objects.filter(Vacancy_id=vid, Department=usr.Department)
    context = {
        'inter_obj': inter_obj,
    }
    return render(request, 'hod_inter_overview.html', context)


def hod_inter_view(request, id):
    inter_obj = Interview.objects.get(id=id)
    viewer = Interview_Interviewer.objects.filter(Interview=inter_obj.id)
    cv = Personal_Interview.objects.filter(Interview=inter_obj.id)
    context = RequestContext(request)
    if request.method == 'POST':
        form = HodReviewForm(request.POST)
        if form.is_valid():
            obj = Interview.objects.get(id=id)
            obj.HOD_Review = form.cleaned_data['HOD_Review']
            obj.done = form.cleaned_data['done']
            if obj.done==True:
                obj.Vacancy.NoOfIntDone = obj.Vacancy.NoOfIntDone+1
            obj.save()
            return redirect('/hod/hod_inter/hod_inter_overview/view/%s'%id)
        else:
            print form.errors
    else:
        form = HodReviewForm()
    return render(request, 'hod_inter_view.html', {'inter_obj': inter_obj, 'viewer': viewer, 'cv': cv, 'form': form}, context)


def hod_profile(request, id):
    try:
        profile = Personal.objects.get(id=id)
        exper = Experience.objects.get(Personal=profile)
        context = RequestContext(request)
    except Personal.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'hod_cv_profile.html', {'pro_form': profile, 'exper': exper}, context)


def hod_msg(request):
    return render(request, 'hod_msg.html', {})


def selection(request):
    passes = Personal_Interview.objects.filter(Status_id=1).count()
    fails = Personal_Interview.objects.filter(Status_id=2).count()
    onholds = Personal_Interview.objects.filter(Status_id=3).count()
    return render(request, 'selection.html', {'p': passes, 'f': fails, 'o': onholds})


def selection_interview(request):
    usr = Users.objects.get(User=request.user)
    inter = Interview.objects.filter(Department=usr.Department)
    return render(request, 'selection_interview.html', {'inter': inter})


def selection_cv(request, iid):
    inter = Interview.objects.get(id=iid)
    cv = Personal_Interview.objects.filter(Interview=inter)
    return render(request, 'selection_cv.html', {'personal': cv})


def selection_profile(request, pid):
    cv = Personal_Interview.objects.get(id=pid)
    comment = Personal_Interview_viewer.objects.filter(Personal_Interview=pid)
    if request.method == 'POST':
        form = SelectStatusForm(request.POST)
        if form.is_valid():
            cv_status = Personal_Interview.objects.get(id=pid)
            cv_status.Status = form.cleaned_data['Status']
            cv_status.save()
            return redirect('/hod/selection_profile/%s/'% id)
        else:
            print form.errors
    else:
        form = SelectStatusForm()
    return render(request, 'selection_profile.html', {'comment': comment, 'cv':cv, 'form':form})


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
    context = RequestContext(request)
    if request.method == 'POST':
        sub = ExperienceForm(request.POST)
        if sub.is_valid():
            form = sub.save(commit=False)
            form.save()
            return redirect('/sub/')
        else:
            print sub.errors
    else:
        sub = ExperienceForm()
    return render(request, 'sub.html', {'sub': sub}, context)
