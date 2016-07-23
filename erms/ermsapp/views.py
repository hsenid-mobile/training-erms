from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from datetime import date
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import Permission
from django.utils.timezone import now
from django.db.models import Q



#ermsapp views start#
@login_required(login_url='/accounts/login/')
def DEO_Entry(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions

    if request.POST:
        deo_form = DEO_EntryForm(request.POST)
        if deo_form.is_valid():
            nic = deo_form.cleaned_data['NIC']
            request.session['nic']  = nic
            check1 = Personal.objects.filter(NIC=nic)
            limit = date.today()-relativedelta(month=3)
            valid = check1.filter(DateRecieved__gte=limit).count()
            if valid == 0:
                request.session['show'] = False
                return HttpResponseRedirect('intermediarycheck')
            else:
                request.session['show'] = True
                return HttpResponseRedirect('intermediarycheck')

        else:
            context={
                'deo_form': deo_form,
                'completion': 'complete all the fields before proceding',
                'topic': 'Varification',
            }
            return render_to_response('deo/deo_entry.html',context)
    else:
        deo_form = DEO_EntryForm()

    args = {}
    args.update(csrf(request))

    args['deo_form'] = deo_form
    args['topic']= 'DEO Entry'
    return render_to_response('deo/deo_entry.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Intermediary(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    nic = request.session['nic']
    show = request.session['show']
    if show:
        completion = "The Person is already within the system You can reffer to the cv details below when feeding the data to the System"
        p = Personal.objects.get(NIC = nic)

        return render_to_response("deo/deo_intermediary2.html",{'completion':completion,'p':p,'url' : '/ermsapp/DEO/cv_profile/',})
    else:
        completion = "The Person is not within the system"

        return render_to_response("deo/deo_intermediary.html",{'completion':completion,'url' : 'personal_info','nic':0})

def DEO_CV_Profile(request,person):
    person = person
    profile = Personal.objects.get(id=person)
    degree = Personal_Degree.objects.filter(Personal=person)
    qual = SubQualification.objects.filter(personal=person)
    skill = Skill.objects.filter(person=person)
    sport = Sports.objects.filter(person=person)
    extra = Extracurricular.objects.filter(person=person)
    experience = Experience.objects.filter(Personal=person)
    special = SpecialAchievements.objects.filter(Person=person)
    context = {
        'pro_form': profile,
        'pro_form_deg':degree,
        'pro_form_qual' : qual,
        'pro_form_skill': skill,
        'pro_form_sport' : sport,
        'pro_form_extra' : extra,
        'pro_form_experience':experience,
        'pro_form_special':special,
            }
    return render(request, 'deo/deo_cv_profile.html', context)



# @login_required(login_url='/accounts/login/')

def DEO_Entry_Personal(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if request.method == 'POST':
        deo_form = DEO_Entry_PersonalForm(request.POST,request.FILES)
        if deo_form.is_valid():

            d = deo_form.save(commit=False)
            d.DateRecieved = now()
            d.save()


            return HttpResponseRedirect('degreechoice')
        else:
            u=Personal.objects.filter(NIC__startswith="93")
            context={
                'deo_form': deo_form,
                'completion': 'complete all the fields before proceding',
                'topic': 'Personal Information',
            }
            return render_to_response('deo/deo_personal.html',context)
    else:
        deo_form = DEO_Entry_PersonalForm()

    args = {}
    args.update(csrf(request))

    args['deo_form'] = deo_form
    args['topic']= 'Personal Information'
    return render_to_response('deo/deo_personal.html',args)


@login_required(login_url='/accounts/login/')
def DEO_DegreeChoice(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if request.POST:
        deo_form1 = DEO_DegreeChoiceForm(request.POST)
        deo_form2 = DEO_Entry_DegreeForm(request.POST)
        if deo_form1.is_valid() and deo_form2.is_valid():
            uni = deo_form1.University
            type = deo_form1.DegreeType
            field = deo_form1.DegreeField
            deg= Degree.objects.get(University__exact=uni,DegreeType__exact=type,DegreeField__exact=field)
            deo = deo_form2.save(commit=False)
            deo.Degree = deg
            deo.save()
            #request.session['deg'] = deg

            return HttpResponseRedirect('degreechoice',deg)


        else:
            context={
                'deo_form': deo_form1,
                'completion': 'complete all the fields before proceding',
                'topic': 'Degree Information',
            }
            return render_to_response('deo/deo_degreechoice.html',context)
    else:
        deo_form1 = DEO_DegreeChoiceForm()
        deo_form2 = DEO_Entry_DegreeForm()

    args = {}
    args.update(csrf(request))

    args['deo_form'] = deo_form1
    args['deo_form1'] = deo_form2
    args['topic']= 'Degree Details'
    return render_to_response('deo/deo_degreechoice.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_OrdinaryQualResult(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if request.POST:
        deo_form_al = DEO_Entry_QualResultForm(request.POST)
        if deo_form_al.is_valid():
            a = deo_form_al
            a.personal = Personal.objects.latest("id")
            a.QName = "Ordinary Level"
            a.save()
            return HttpResponseRedirect('ordinarylevel')
        else:
            return HttpResponse('faild to enter data')
    else:
        deo_form_al = DEO_Entry_QualResultForm()

    args = {}
    args.update(csrf(request))
    args['deo_form_al'] = deo_form_al
    args['topic'] = 'Ordinary Level'

    return render_to_response('deo/deo_ordinaryqualresult.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_Ordinary(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if request.POST:
        deo_form_ol = DEO_Entry_OoAQualification(request.POST)


        if deo_form_ol.is_valid():
            ol1 = deo_form_ol.save(commit=False)
            ol1.personal = Personal.objects.latest("id")
            ol1.QType = QType.objects.get(id=1)
            ol1.QName = "Ordinary Level"
            ol1.save()
            return HttpResponseRedirect("ordinarylevel")
        else:
            context={
                'deo_form_ol1': deo_form_ol,
                'completion': 'complete all the fields before proceding',
                'topic': 'Ordinary Level',
                'subject':'Subject',
            }
            return render_to_response('deo/deo_ordinary.html', context)
    else:
        deo_form_ol1 = DEO_Entry_OoAQualification()

    args = {}
    args.update(csrf(request))
    args['subject'] = "Subject"
    args['deo_form_ol1'] = deo_form_ol1
    args['topic'] = 'Ordinary Level'
    return render_to_response('deo/deo_ordinary.html', args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_AdvancedQualResult(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if request.POST:
        deo_form_al = DEO_Entry_QualResultForm(request.POST)
        if deo_form_al.is_valid():
            a = deo_form_al
            a.personal = Personal.objects.latest("id")
            a.QName = "Advanced Level"
            a.save()
            return HttpResponseRedirect('advancedlevel')
        else:
            return HttpResponse('faild to enter data')
    else:
        deo_form_al = DEO_Entry_QualResultForm()

    args = {}
    args.update(csrf(request))
    args['deo_form_al'] = deo_form_al
    args['topic'] = 'Advanced Level'

    return render_to_response('deo/deo_advancedqualresult.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_Advanced(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if request.POST:
        deo_form_al = DEO_Entry_OoAQualification(request.POST)


        if deo_form_al.is_valid():
            al1  = deo_form_al.save(commit=False)
            al1.QName = "Advanced Level"
            al1.personal = Personal.objects.latest("id")
            al1.QType = QType.objects.get(id=1)
            al1.save()

            return HttpResponseRedirect("advancedlevel",)
        else:
            context={
                'deo_form_ol1': deo_form_al,
                'completion': 'complete all the fields before proceding',
                'topic': 'Advanced Level',
                'subject':'Subject'
            }
            return render_to_response('deo/deo_advanced.html', context)
    else:
        deo_form_al = DEO_Entry_OoAQualification()

    args = {}
    args.update(csrf(request))
    args['subject'] = "Subject"
    args['deo_form_al'] = deo_form_al
    args['topic']= 'Advanced Level'
    return render_to_response('deo/deo_advanced.html', args)



@login_required(login_url='/accounts/login/')
def DEO_Entry_Qualification(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if request.POST:
        deo_form1 = DEO_Entry_QualificationForm(request.POST)
        if deo_form1.is_valid():
            request.session['qul'] = data.QName
            request.session['res'] = data.Result
            request.session['spe'] = data.SpecialNotes
            request.session['qtp'] = data.QType.id

            completion= 'Successfully added previous Qualification data to the system'
            return HttpResponseRedirect('sub_qualification',{'comletion':completion})
        else:
            context={
                'deo_form': deo_form1,
                'completion': 'complete all the fields before proceding',
                'topic': 'Other Qualification',
            }
            return render_to_response('deo/deo_otherqual.html',context)
    else:
        deo_form1 = DEO_Entry_QualificationForm()

        args = {}
        args.update(csrf(request))

        args['deo_form'] = deo_form1
        args['topic']= 'Other Qualification'
        return render_to_response('deo/deo_otherqual.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_SubQualification(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if 'qul' in request.session:
            qul = request.session['qul']
    if request.POST:
        deo_form1 = DEO_Entry_SubQualificationForm(request.POST)
        if deo_form1.is_valid():
            d = deo_form1.save(commit=False)
            d.QName=request.session['qul']
            d.personal=Personal.objects.latest("id")
            d.SpecialNotes=request.session['spe']
            d.QType=QType.objects.get(id=request.session['qtp'])
            data1.save()
            completion= 'Successfully added previous Qualification data to the system'
            return HttpResponseRedirect('sub_qualification',{'comletion':completion,'qul':qul})
        else:

            context={
                'deo_form': deo_form1,
                'completion': 'complete all the fields before proceding',
                'topic': 'Other Qualification',
                'qul': qul
            }
            return render_to_response('deo/deo_otherqual_sub.html',context)
    else:
        deo_form1 = DEO_Entry_SubQualificationForm()

        args = {}
        args.update(csrf(request))

        args['deo_form'] = deo_form1
        args['topic']= 'Subject Results'
        args['qul']= qul
        return render_to_response('deo/deo_otherqual_sub.html',args)

@login_required(login_url='/accounts/login/')
def DEO_Entry_Skills(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if request.POST:
        deo_form1 = DEO_Entry_Skill1(request.POST)
        if deo_form1.is_valid():
            s1 = deo_form1.save(commit=False)
            s1.person = Personal.objects.latest("NIC")
            s1.save()
            completion= 'Successfully added previous Qualification data to the system'
            return HttpResponseRedirect('skills',{'comletion':completion})
        else:

            context={
                'deo_form1': deo_form1,
                'completion': 'complete all the fields before proceding',
                'topic': 'Skills',

            }
            return render_to_response('deo/deo_skills.html',context)
    else:
        deo_form1 = DEO_Entry_Skill1()

        args = {}
        args.update(csrf(request))

        args['deo_form1'] = deo_form1
        args['topic']= 'Skills'
        return render_to_response('deo/deo_skills.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_Extra(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if request.POST:
        deo_form1 = DEO_Entry_ExtraForm1(request.POST)
        if deo_form1.is_valid():
            s1 = deo_form1.save(commit=False)
            s1.person = Personal.objects.latest("id")
            s1.save()
            completion= 'Successfully added previous Extracurricular data to the system'
            return HttpResponseRedirect('extra_info',completion)
        else:

            context={
                'deo_form1': deo_form1,
                'completion': 'complete all the fields before proceding',
                'topic': 'Extracurricular Activities',
            }
            return render_to_response('deo/deo_extra.html',context)
    else:
        deo_form1 = DEO_Entry_ExtraForm1()

        args = {}
        args.update(csrf(request))

        args['deo_form1'] = deo_form1
        args['topic']= 'Extracurricular Activities'
        return render_to_response('deo/deo_extra.html',args)


@login_required(login_url='/accounts/login/')
def DEO_Entry_Sport(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if request.POST:
        deo_form1 = DEO_Entry_SportForm1(request.POST)
        if deo_form1.is_valid():
            s1 = deo_form1.save(commit=False)
            s1.person = Personal.objects.latest("id")
            s1.save()
            completion= 'Successfully added previous Sport data to the system'
            return HttpResponseRedirect('sport_info',completion)
        else:

            context={
                'deo_form1': deo_form1,
                'completion': 'complete all the fields before proceding',
                'topic': 'Sports',
            }
            return render_to_response('deo/deo_sport.html',context)
    else:
        deo_form1 = DEO_Entry_SportForm1()

        args = {}
        args.update(csrf(request))

        args['deo_form1'] = deo_form1
        args['topic']= 'Sports'
        return render_to_response('deo/deo_sport.html',args)


@login_required(login_url='../../accounts/login/')
def DEO_Entry_Experience(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    #Permissions
    if request.POST:
        deo_form = DEO_Entry_ExperienceForm(request.POST)
        if deo_form.is_valid():
            ex = deo_form.save(commit=False)
            ex.Personal = Personal.objects.latest("id")
            ex.save()
            completion = 'Successfully added previous Experience data to the system'
            return HttpResponseRedirect('experience_info',completion)
        else:

            context={
                'deo_form': deo_form,
                'completion': 'complete all the fields before proceding',
                'topic': 'Experience',
            }
            return render_to_response('deo/deo_experience.html',context)
    else:
        deo_form = DEO_Entry_ExperienceForm()
        args = {}
        args.update(csrf(request))
        args['deo_form'] = deo_form
        args['topic']= 'Experience'
        return render_to_response('deo/deo_experience.html',args)



@login_required(login_url='../../accounts/login/')
def DEO_Entry_Special_Ach(request):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    else:
        #Permissions
        if request.POST:
            deo_form = DEO_Enrety_SpecialAchievements(request.POST)
            if deo_form.is_valid():
                ex = deo_form.save(commit=False)
                ex.Person = Personal.objects.latest("id")
                ex.save()
                completion= 'Successfully added previous Experience data to the system'
                return HttpResponseRedirect('spcl_achvmnt_info',completion)
            else:

                context={
                    'deo_form': deo_form,
                    'completion': 'complete all the fields before proceding',
                    'topic': 'Special Achievements',
                }
                return render_to_response('deo/deo_special_achievement.html',context)
        else:
            deo_form = DEO_Enrety_SpecialAchievements()
            args = {}
            args.update(csrf(request))

            args['deo_form'] = deo_form
            args['topic']= 'Special Achievements'
            return render_to_response('deo/deo_special_achievement.html',args)


def success_post(request):
    return render(request, 'deo/successPost.html')