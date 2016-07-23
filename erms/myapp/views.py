from django.shortcuts import RequestContext, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import date, datetime
from django.shortcuts import render,render_to_response
from django.conf import settings
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.db.models import Q
from .forms import *



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
    return render(request, 'hod/hod.html', context)


def hod_post_list(request):
    usr = Users.objects.get(User=request.user)
    post_dept = Post_Dept.objects.filter(Dept=usr.Department)
    return render(request, 'hod/hod_post_list.html', {'post': post_dept})


def hod_vacan_list(request):
    usr = Users.objects.get(User=request.user)
    post_dept = Post_Dept.objects.filter(Dept=usr.Department)
    obj = Vacancy.objects.all()
    return render(request, 'hod/test_vacancy.html', {'obj': obj})


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
            print(vacncy_form.errors)
    else:
        vacncy_form = VacancyForm()
    return render(request, 'hod/hod_vacancy.html', {'v_form': vacncy_form}, context)


def hod_vacancy_succs(request):
    return render(request, 'hod/hod_vacancy_succs.html', {})


def hod_vacancy_test(request):
    obj = Vacancy.objects.all()
    return render(request, 'hod/test_vacancy.html', {'obj': obj})




def hod_auto_filter(request):
    return render()


def hod_cv(request):
    usr = Users.objects.get(User=request.user)
    post_dept = Post_Dept.objects.filter(Dept=usr.Department)
    return render(request, 'hod/hod_cv.html', {'post': post_dept})


def hod_cv_list(request, post_id):
    form_cv = Personal_Post_Dept.objects.filter(DeptPost= Post_Dept.objects.get(id = post_id))
    count = form_cv.count()
    return render(request, 'hod/hod_cv_list.html', {'cv': form_cv})


def hod_inter(request):
    return render(request, 'hod/hod_inter.html', {})


def hod_inter_choose_vacancy(request):
    vacancy = Vacancy.objects.all()
    context = {
        'Vacn': vacancy,
    }
    return render(request, 'hod/hod_inter_choose_vacancy.html', context)


def hod_view_vacancy(request, ID):
    obj = Vacancy.objects.get(id=ID)
    obj1  = Interview.objects.filter(Vacancy=obj)
    return render(request, 'hod/hod_view_vacancy.html', {'obj': obj, obj1:obj})


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
            print(form.errors)
    else:
        form = InterviewForm()
    return render(request, 'hod/hod_inter_create.html', {'form': form}, context)




#######################################################################################################



def hod_inter2_create(request, vid):
    context = RequestContext(request)
    obj = Vacancy.objects.get(id=vid)
    usr = Users.objects.get(User=request.user)
    noOfInt = obj.Post_Dept.Post.NoOfInterviews
    intNo = int(obj.CurrentInt or 0)
    iid = obj.CurrentIntId.id
    if intNo <= noOfInt:
        if request.method == 'POST':
            inter_form = InterviewForm(request.POST)
            if inter_form.is_valid():
                inter = inter_form.save(commit=False)
                inter.Department = usr.Department
                inter.HOD = request.user
                inter.Vacancy = obj
                inter.Post = obj.Post_Dept.Post
                inter.InterviewNo = int(intNo or 0) + 1
                inter_form.Post = Vacancy.objects.get(id = vid).Post_Dept.Post
                inter.save()
                v = Vacancy.objects.get(id=vid)
                v.CurrentInt = int(v.CurrentInt or 0) + 1
                v.CurrentIntId = inter
                v.save()
                request.session['intP'] = int(iid or 0)
                request.session['intN'] = Interview.objects.latest('id').id
                return redirect('/hod/hod_vacancy/test2/succs/')
            else:
                print(inter_form.errors)
        else:
            inter_form = InterviewForm()
        return render(request, 'hod/hod_inter2_create.html', {'inter_form': inter_form, 'obj': obj, 'vid': vid, 'iid':iid}, context)
    else:

        return HttpResponseRedirect('hod/hod_recruit2/%s' %iid)



def hod_inter2_create_succs(request):
    piid = request.session['intP']
    niid = request.session['intN']
    return render(request, 'hod/hod_inter2_create_succs.html', {'piid':piid, 'niid':niid})



def hod_pre_interviwer_list2(request, niid,piid):
    inter = Interview.objects.get(id=niid)
    a = UserRole.objects.get(Role="Interviewer")
    viewer = Users.objects.filter(UserRole=a.id)
    piid = int(piid or 0 )
    return render(request, 'hod/hod_inter2_create_2.html', {'viewer': viewer, 'inter': inter, 'a':a,'piid':piid})



def hod_inter2_interviewer_2(request, piid,niid, pid):
    piid = int(piid or 0)
    inter = Interview.objects.get(id=niid)
    a = UserRole.objects.get(Role="Interviewer")
    viewer = Users.objects.filter(UserRole=a.id)
    usr_id = Users.objects.get(id=pid)
    usr = User.objects.get(id=usr_id.User_id)
    inter_id = inter
    person_id = usr
    form = Interview_Interviewer(Interview=inter_id, Interviewer=person_id)
    form.save()
    return render(request, 'hod/hod_inter2_create_2.html', {'viewer': viewer, 'inter': inter,'piid':piid})

def hod_vacancy_list_cv(request,vid):
    usr = Users.objects.get(User=request.user)
    inter = Vacancy.objects.get(Post_Dept__Dept=usr.Department,done=False)
    return render(request, 'hod/hod_vacancy_list_cv.html', {'inter': inter})


def hod_inter_list_cv(request,vid):
    usr = Users.objects.get(User=request.user)
    inter = Interview.objects.filter(done=False,Vacancy=Vacancy.objects.get(id = vid))
    return render(request, 'hod/hod_inter_list_cv.html', {'inter': inter})


def hod_pre_cv_list2(request, piid,niid):
    inter = Interview.objects.get(id=niid)
    usr = Users.objects.get(User=request.user)
    post = Post_Dept.objects.get(Post=inter.Post_id)
    cv = Personal_Interview.objects.filter(id = piid,Status=CV_Status.objects.get(Status="Pass"))
    return render(request, 'hod/hod_inter2_create_3.html', {'cv': cv, 'inter': inter,'piid':piid})


def hod_inter_cv(request, iid, pid):
    context = RequestContext(request)
    inter = Interview.objects.get(id=iid)
    post = Post.objects.get(id=inter.Post_id)
    usr = Users.objects.get(User=request.user)
    post = Post_Dept.objects.get(Post=inter.Post_id)
    cv = Personal_Post_Dept.objects.filter(DeptPost=post)
    # cv_sp = Personal_Post_Dept.objects.get(id=pid)
    form = Personal_Interview(Interview=inter, Personal=Personal.objects.get(id=pid))
    form.save()
    return render(request, 'hod/hod_inter_create_3.html', {'cv': cv, 'inter': inter}, context)


def hod_inter2_cv(request, piid,niid, pid):
    context = RequestContext(request)
    inter = Interview.objects.get(id=niid)
    post = Post.objects.get(id=inter.Post_id)
    usr = Users.objects.get(User=request.user)
    post = Post_Dept.objects.get(Post=inter.Post_id)
    cv = Personal_Interview.objects.filter(id = piid,Status=CV_Status.objects.get(Status="Pass"))
    # cv_sp = Personal_Post_Dept.objects.get(id=pid)
    form = Personal_Interview(Interview=inter, Personal=Personal.objects.get(id=pid))
    form.save()
    return render(request, 'hod/hod_inter2_create_3.html', {'cv': cv, 'inter': inter,'piid':piid}, context)

####################################################################################################################


def hod_recruit(request):
    dept = Users.objects.get(User=request.user).Department
    vacancies = Vacancy.objects.filter(done=False,Post_Dept__Dept=dept)
    return render_to_response('hod/ongoing_vacancies.html',{'vacancies':vacancies})


def hod_recruit1(request,vid):
    interview = Interview.objects.filter(Vacancy=Vacancy.objects.get(id = vid))
    request.session['pos'] = 0
    return render_to_response('hod/ongoing_interviews.html', {'interview': interview})


def hod_recruit2(request,iid):
    cv = Personal_Interview.objects.filter(Interview=Interview.objects.get(id=iid))
    noOfInt = Interview.objects.get(id=iid).Vacancy.Post_Dept.Post.NoOfInterviews
    intNo = Interview.objects.get(id=iid).InterviewNo
    if intNo < noOfInt:
        status_form = SelectStatusForm()
        return render_to_response('hod/ongoing_cvs.html', {'form':status_form,'cv': cv, 'eve': "", 'rec': "hidden", 'iid': iid})
    else:
        return render_to_response('hod/ongoing_cvs.html', {'cv': cv, 'rec': "", 'eve': "hidden",'iid':iid})


def hod_recruit3(request,iid,pid):
    cv = Personal_Interview.objects.get(Interview=Interview.objects.get(id=iid))
    noOfInt = Interview.objects.get(id = iid).Vacancy.Post_Dept.Post.NoOfInterviews
    intNo = Interview.objects.get(id = iid).InterviewNo
    if intNo < noOfInt:
        if request.POST:
            status_form = SelectStatusForm(request.POST)
            if status_form.is_valid():
                p = Personal_Interview.objects.get(Interview=Interview.objects.get(id = iid),Personal=Personal.objects.get(id = pid))
                p.Status = status_form.cleaned_data['Status']
                p.save()
                return render_to_response('hod/ongoing_cvs.html',{'form':status_form,'cv':cv,'eve':"",'rec':"hidden",'iid':iid})
            else:
                return render_to_response('hod/ongoing_cvs.html',{'form':status_form,'cv':cv,'eve':"",'rec':"hidden",'iid':iid,'report':"Previous assignment was not done properly"})


    else:
        a = request.session['pos']
        a = a+1
        request.session['pos'] = a
        possitions = Interview.objects.get(id = iid).Vacancy.NoOfPossitions
        if a < possitions:
            p = Personal.objects.get(id = pid)
            p.RecruitedPost = Interview.objects.get(id = iid).Vacancy.Post_Dept.Post.Post
            p.save()
            rec  = Recruited_Personal(Vacancy = Interview.objects.get(id = iid).Vacancy,Personal = p)
            rec.save()
            return render_to_response('hod/ongoing_cvs.html',{'cv':cv,'rec':"",'eve':"hidden",'iid':iid})
        else:
            p = Personal.objects.get(id=pid)
            p.RecruitedPost = Interview.objects.get(id=iid).Vacancy.Post_Dept.Post.Post
            p.save()
            rec = Recruited_Personal(Vacancy=Interview.objects.get(id=iid).Vacancy, Personal=p)
            rec.save()
            v = Interview.objects.get(id = iid).Vacancy
            v.done = True
            v.save()

            return render_to_response('hod/vacancy_done.html')


def hod_recruit_previous(request):
    dept = Users.objects.get(User=request.user).Department
    vacancies = Vacancy.objects.filter(done=True,Post_Dept__Dept=dept)
    return render_to_response('hod/previous_vacancies.html',{'vacancies':vacancies})


def hod_recruit1_previous(request,vid):
    interview = Interview.objects.filter(Vacancy=Vacancy.objects.get(id = vid))
    return render_to_response('hod/previous_interviews.html', {'interview': interview})


def hod_recruit_previous_overview(request,iid):
    inter_obj = Interview.objects.get(id=iid)
    viewer = Interview_Interviewer.objects.filter(Interview=inter_obj.id)
    return render(request, 'hod/hod_privous_overview.html', {'inter_obj': inter_obj, 'viewer': viewer})


def interview_done(request,iid):
    int = Interview.objects.get(id = iid)
    int.done =True
    int.save()
    v = Interview.objects.get(id = iid).Vacancy
    v.NoOfIntDone = int(v.NoOfIntDone or 0) + 1
    v.save()
    return render_to_response('hod/interview_done.html',{'iid':iid,'int':int})



def hod_view_inter(request, ID):
    vacan = Vacancy.objects.get(id=ID)
    cv = Personal.objects.all()
    inter_form_2 = InterviewForm2(request.POST)
    try:
        selected_cv = Personal.objects.get(id=request.POST['cv'])
    except (KeyError, Personal.DoesNotExist):
        return render(request, 'hod/hod_inter_create_2.html', {'error': "Person does not exist"})
    else:
        selected_cv.is_selected = True
        selected_cv.save()
        return render(request, 'hod/hod_inter_create_2.html', {'inter_form_2': inter_form_2, 'cv': cv, 'vacan':vacan})


def hod_succs(request):
    return render(request, 'hod/hod_succs.html', {})


def hod_inter_overview(request):
    inter_obj = Vacancy.objects.filter(Post_Dept__Dept=Users.objects.get(User = request.user).Department)
    context = {
        'vacancies': inter_obj,
    }
    return render(request, 'hod/previous_vacancies.html', context)


def hod_inter_view(request,id):
    inter_obj = Interview.objects.get(id=id)
    viewer = Interview_Interviewer.objects.filter(Interview=inter_obj.id)
    cv = Personal_Interview.objects.filter(Interview=inter_obj.id)
    context = RequestContext(request)
    if request.method == 'POST':
        form = HodReviewForm(request.POST)
        if form.is_valid():
            obj = Interview.objects.get(id=id)
            obj.HOD_Review = form.cleaned_data['HOD_Review']
            obj.save()
            return redirect('/hod/hod_inter/hod_inter_overview/view/%s'%id)
        else:
            print(form.errors)
    else:
        form = HodReviewForm()
    return render(request, 'hod/hod_inter_view.html', {'inter_obj': inter_obj, 'viewer': viewer, 'cv': cv, 'form': form}, context)


def hod_profile(request, id):
    try:
        profile = Personal.objects.get(id=id)
        context = RequestContext(request)
        if request.method == 'POST':
            hod = HodReviewForm(request.POST, request.FILES)
            if hod.is_valid():
                review = hod.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('')
            else:
                print(hod.errors)
        else:
            hod = HodReviewForm()
    except Personal.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'hod/hod_cv_profile.html', {'hod_form': hod, 'pro_form': profile}, context)


def hod_msg(request):
    return render(request, 'hod/hod_msg.html', {})


def selection_interview(request):
    usr = Users.objects.get(User=request.user)
    inter = Interview.objects.filter(Department=usr.Department)
    return render(request, 'hod/selection_interview.html', {'inter': inter})


def selection_cv(request, iid):
    inter = Interview.objects.get(id=iid)
    cv = Personal_Interview.objects.filter(Interview=inter)
    return render(request, 'hod/selection_cv.html', {'personal': cv})


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
            print(form.errors)
    else:
        form = SelectStatusForm()
    return render(request, 'hod/selection_profile.html', {'comment': comment, 'cv':cv, 'form':form})


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
            print(deoForm.errors)
    else:
        deoForm = PersonForm()
    return render(request, 'hod/deo.html', {'deoForm': deoForm}, context)


def deo_submit(request):
    return render(request, 'hod/deo_submit.html', {})


def deo_profile(request):
    profile_form = Personal.objects.all()
    return render(request, 'hod/deo_profile.html', {'profile_form': profile_form})


def date_time(request):
    year = datetime.today()
    return render(request, 'hod/date_time.html', {'year':year})


def subv(request):
    if request.method == 'POST':
        sub = SubForm(request.POST)
        if sub.is_valid():
            form = sub.save(commit=False)
            form.save()
            return redirect('/sub/')
        else:
            print(sub.errors)
    else:
        sub = SubForm()
    return render(request, 'hod/sub.html', {'sub': sub})
