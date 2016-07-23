
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,Http404
from interviewer.forms import *
from ermsapp.models import *
from django.shortcuts import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
# Create your views here.


def Interviewer_Interview_List(request):
    context = {
            'int': Interview_Interviewer.objects.filter(Interviewer=request.user,Interview__Date__gte=now()),
            'topic': 'Interviews',

        }
    return render_to_response('Interviewer/interview_list.html',context)


def Interviewer_Cv_list(request,iid):
    request.session['iid'] = iid
    if request.POST:
        interviewer_form = Review_Form(request.POST)
        if interviewer_form.is_valid():
            a = Interview.objects.get(id=iid)  # .update(Interviewer_Review = rvw_form.cleaned_data['Interviewer_Review'])
            a.Interviewer_Review = interviewer_form.cleaned_data['Interviewer_Review']
            a.save()
            return HttpResponseRedirect('interviewer/interview_list')
        else:
            print(interviewer_form.errors)
    else:
        interviewer_form = Review_Form()
        context = {
            'int':Personal_Interview.objects.filter(Interview = iid),
            'topic': 'List of CVs',
            'interviewer_form': interviewer_form,
            'iid':iid,
        }
        return render_to_response('Interviewer/cv_list.html',context)


def Interviewer_CV_Profile(request,person):
    profile = Personal.objects.get(id=person)
    degree = Personal_Degree.objects.filter(Personal=person)
    qual = SubQualification.objects.filter(personal=person)
    skill = Skill.objects.filter(person=person)
    sport = Sports.objects.filter(person=person)
    extra = Extracurricular.objects.filter(person=person)
    experience = Experience.objects.filter(Personal=person)
    special = SpecialAchievements.objects.filter(Person=person)
    if request.method == 'POST':
        intvw = Evaluation_Form(request.POST)
        if intvw.is_valid():
            evl = intvw.save(commit=False)
            evl.Interviewers = request.user
            evl.save()

            return HttpResponseRedirect('cv_list/',)
        else:
            return HttpResponse('error')
    else:
        intvw = Evaluation_Form()
        context = {
            'hod_form': intvw,
            'pro_form': profile,
            'pro_form_deg':degree,
            'pro_form_qual' : qual,
            'pro_form_skill': skill,
            'pro_form_sport' : sport,
            'pro_form_extra' : extra,
            'pro_form_experience':experience,
            'pro_form_special':special,
            'intvw':intvw,
            'person': person,
            'topic':'Cv Profile',
            }
        return render(request, 'Interviewer/cv_profile.html', context)

