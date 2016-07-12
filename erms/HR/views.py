from django.shortcuts import render, redirect
from django.template import RequestContext
from .forms import *


# Create your views here.


def home(request):
    return render(request, 'hr/home.html', {})


def received_cvs(request):
    all_persons = Personal.objects.all()
    context = {
        'all_persons': all_persons,
    }
    return render(request, 'hr/receivedCV.html', context)


def vacancy_cvs(request, vacancy_id):
    all_vacancies = Vacancy.objects.get(id=vacancy_id)
    all_persons = Personal.objects.all()
    context = {
        'all_vacancies': all_vacancies,
        'all_persons': all_persons,
    }
    return render(request, 'hr/vacancyCV.html', context)


def view_cvs(request, person_id):
    all_persons = Personal.objects.get(id=person_id)
    skills = Skill.objects.all()
    tertiary = Personal_Degree.objects.all()
    gce_ol = SubQualification.objects.all()
    experience = Experience.objects.all()
    extra = Extracurricular.objects.all()
    awards = SpecialAchievements.objects.all()
    sub_post = subQul_Post.objects.all()
    post = Post.objects.all()
    exp_post = Exp_Post.objects.all()
    deg_post = Degree_For_Post.objects.all()
    context = {
        'all_persons': all_persons,
        'tertiary': tertiary,
        'gce_ol': gce_ol,
        'experience': experience,
        'extra': extra,
        'awards': awards,
        'sub_post': sub_post,
        'post': post,
        'exp_post': exp_post,
        'deg_post': deg_post,
        'skills': skills,
    }
    return render(request, 'hr/CV_profile.html', context)


def messages(request):
    all_messages = Messages.objects.all()
    context = {
        'all_messages': all_messages,
    }
    return render(request, 'hr/messages.html', context)


def vacancies_view(request):
    all_vacancies = Vacancy.objects.all()
    context = {
        'all_vacancies': all_vacancies,
    }
    return render(request, 'hr/vacancies.html', context)


def send_msg(request):
    context = RequestContext(request)
    if request.method == 'POST':
        msg_form = MessageForm(request.POST)
        if msg_form.is_valid():
            msg_data = msg_form.save(commit=False)
            msg_data.Sender = request.user
            msg_data.SentDate = now()
            msg_data.SentTime = now()
            msg_data.save()
            return redirect('/messages/')
        else:
            print(msg_form.errors)
    else:
        msg_form = MessageForm()
    return render(request, 'hr/sendMsg.html', {'msg_form': msg_form}, context)


# def send_cvs(request, p_id):
#     all_persons = Personal.objects.get(id=p_id)
#     p = Personal.objects.get(id=p_id)
#     p.save()
#     context = RequestContext(request)
#
#     if request.method == 'POST':
#         cv_dept = CvForDept(request.POST)
#         if cv_dept.is_valid():
#             cv_data = cv_dept.save(commit=False)
#             cv_data.save()
#
#             return redirect('/view_cvs/')
#         else:
#             print(cv_dept.errors)
#     else:
#         cv_dept = CvForDept()
#
#     return render(request, 'hr/sendCV.html', {'all_person': all_persons, 'cv_dept': cv_dept}, context)


def create_post(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form1 = NewPost1(request.POST)

        if form1.is_valid():
            post_data = form1.save(commit=False)
            post_data.save()

            return redirect('/addDept/')

        else:
            print(form1.errors)
    else:
        form1 = NewPost1()

    return render(request, 'hr/createPost.html', {'f1': form1}, context)


def add_dept(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form2 = PostDept(request.POST)

        if form2.is_valid():
            post_data = form2.save(commit=False)
            post_data.save()

            return redirect('/degPost/')

        else:
            print(form2.errors)

    else:
        form2 = PostDept()
    return render(request, 'hr/addDept.html', {'f2': form2}, context)


def deg_post(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form5 = DegPost(request.POST)

        if form5.is_valid():
            post_data = form5.save(commit=False)
            post_data.save()

            return redirect('/degPost/')

        else:
            print(form5.errors)

    else:
        form5 = DegPost()
    return render(request, 'hr/degPost.html', {'f5': form5}, context)


def qualifications(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form3 = SubQualif(request.POST)

        if form3.is_valid():
            post_data = form3.save(commit=False)
            post_data.save()

            return redirect('/qualifications/')

        else:
            print(form3.errors)
    else:
        form3 = SubQualif()

    if request.method == 'POST':
        form4 = ProfQualif(request.POST)

        if form4.is_valid():
            post_data = form4.save(commit=False)
            post_data.save()

            return redirect('/successPost/')

        else:
            print(form4.errors)
    else:
        form4 = ProfQualif()

    return render(request, 'hr/qualifications.html', {'f3': form3, 'f4': form4}, context)


def success_post(request):
    return render(request, 'hr/successPost.html', {})

def cvs_for_vacancies(request, vacancy_id, person_id):
    all_vacancies = Vacancy.objects.get(id=vacancy_id)
    all_persons = Personal.objects.get(id=person_id)
    skills = Skill.objects.all()
    tertiary = Personal_Degree.objects.all()
    gce_ol = SubQualification.objects.all()
    experience = Experience.objects.all()
    extra = Extracurricular.objects.all()
    awards = SpecialAchievements.objects.all()
    sub_post = subQul_Post.objects.all()
    post = Post.objects.all()
    exp_post = Exp_Post.objects.all()
    degree_post = Degree_For_Post.objects.all()
    context = {
        'all_vacancies': all_vacancies,
        'all_persons': all_persons,
        'tertiary': tertiary,
        'gce_ol': gce_ol,
        'experience': experience,
        'extra': extra,
        'awards': awards,
        'sub_post': sub_post,
        'post': post,
        'exp_post': exp_post,
        'deg_post': degree_post,
        'skills': skills,
    }
    return render(request, 'hr/vacancyCV_profile.html', context)


def send_cvs(request, p_id):
    all_persons = Personal.objects.get(id=p_id)

    context = RequestContext(request)

    if request.method == 'POST':
        cv_dept = CvForDept(request.POST)
        if cv_dept.is_valid():
            cv_data = cv_dept.save(commit=False)
            cv_data.Personal = Personal.objects.get(id=p_id)
            cv_data.save()

            return redirect('/hr/vacancies/')
        else:
            print(cv_dept.errors)
    else:
        cv_dept = CvForDept()

    return render(request, 'hr/sendCV.html', {'all_person': all_persons, 'cv_dept': cv_dept}, context)


def send_rec_cvs(request, p_id):
    all_persons = Personal.objects.get(id=p_id)

    context = RequestContext(request)

    if request.method == 'POST':
        rec_dept = CvForDept(request.POST)
        if rec_dept.is_valid():
            rec_data = rec_dept.save(commit=False)
            rec_data.Personal = Personal.objects.get(id=p_id)
            rec_data.save()

            return redirect('/hr/received_CVs/')
        else:
            print(rec_dept.errors)
    else:
        rec_dept = CvForDept()
    return render(request,'hr/sendRecCV.html', {'all_person': all_persons, 'rec_dept': rec_dept}, context)
