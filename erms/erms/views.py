from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ermsapp.models import *

#login views start#

def login_view(request):
    c={}
    c.update(csrf(request))
    return render_to_response('admin/login.html', c)


def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username.strip(),password=password)
    u=User.objects.get(username=username)
    u1 = Users.objects.get(User=u)
    ur1 = UserRole.objects.get(Role__exact="DEO")
    ur2 = UserRole.objects.get(Role__exact="Admin")
    ur3 = UserRole.objects.get(Role__exact="HOD")
    ur4 = UserRole.objects.get(Role__exact="HR")
    ur5 = UserRole.objects.get(Role__exact="Interviewer")
    if user is not None:
        if user.is_active:
            if  u1.UserRole== ur1:
                auth.login(request,user)
                return HttpResponseRedirect("../../ermsapp/DEO/logedindeo")
            elif u1.UserRole == ur2:
                auth.login(request, user)
                return HttpResponseRedirect("../../accounts/logedinadmin")
            elif u1.UserRole== ur3:
                auth.login(request,user)
                return HttpResponseRedirect("../../hod/")
            elif  u1.UserRole== ur4:
                auth.login(request,user)
                return HttpResponseRedirect("../../hr/hr")
            elif  u1.UserRole== ur5:
                auth.login(request,user)
                return HttpResponseRedirect("../../interviewer/logedin")
            else:
                return HttpResponse('You are not a registered user')

        else:
            context={
                "login_error":"your account is no longer active"
    }
            return render(request, "admin/login.html", context)
    else:
        return HttpResponseRedirect('invalid')


def invalid_view(request):
    context={

        "login_error":"Username or password is incorrect"
    }

    return render(request, "admin/login.html", context)


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('../../accounts/login')


@login_required(login_url='/accounts/login/')
def logedindeo_view(request):
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="DEO"):
        return HttpResponse('You are not a valid user')
    context ={"topic":"Dashboard","user":request.user}

    return  render_to_response('deo/logedin.html',context)


@login_required(login_url='/accounts/login/')
def logedinadmin_view(request):
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="Admin"):
        return HttpResponse('You are not a valid user')
    context ={"topic":"Dashboard","user":request.user}

    return  render_to_response('admin/logedin.html', context)

@login_required(login_url='/accounts/login/')
def logedininterviewer_view(request):
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="Interviewer"):
        return HttpResponse('You are not a valid user')
    context ={"topic":"Dashboard","user":request.user}

    return  render_to_response('Interviewer/logedin.html',context)

@login_required(login_url='/accounts/login/')
def logedinHR_view(request):
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="HR"):
        return HttpResponse('You are not a valid user')
    context ={"topic":"Dashboard","user":request.user}

    return  render_to_response('hr/home.html', context)

@login_required(login_url='/accounts/login/')
def logedinHOD_view(request):
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="HOD"):
        return HttpResponse('You are not a valid user')
    context ={"topic":"Dashboard","user":request.user}

    return  render_to_response('hod/hod.html',context)

#login views end#

#user registratoin views Stert#
#@login_required(login_url='/accounts/login/')
def registration_view(request):
    if request.method=='POST':
        reg_form1= user_form(request.POST)
        reg_form2= profile_form(request.POST,request.FILES)

        if reg_form1.is_valid() and reg_form2.is_valid():
            u1 = reg_form1.save()
            u2= reg_form2.save(commit=False)
            u2.User = u1
            u2.save()
            registration = True
            return render_to_response('admin/UserRegForm.html', {'registered':registration})

        else:
            context={
                'reg_form1': user_form(),
                'reg_form2': profile_form(),
                'completion': 'complete the registration fields before registering',
                'topic': "Register Users"
            }
            return render_to_response('admin/UserRegForm.html', context)

    args = {}
    args.update(csrf(request))

    args['reg_form1'] = user_form()
    args['reg_form2'] = profile_form()
    args['topic'] = "Register User"
    return render_to_response('admin/UserRegForm.html', args)

@login_required(login_url='/accounts/login/')
def registration_success():
    registration = True
    return render_to_response('admin/UserRegForm.html', {'registered':registration})



@login_required(login_url='/accounts/login/')
def degreeType(request):
    if request.POST:
        form1=DegreeType_Form(request.POST)

        if form1.is_valid():
            form1.save()
            return HttpResponse('Done')
        else:
            return HttpResponse('Data Not Entered to the System')
    else:
        form1 = DegreeType_Form()
    args = {}
    args.update(csrf(request))
    args['form1'] = form1
    return render_to_response('deo/degreeType.html', args)

#Post Requirements


def getPostDetail(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        dept = PostForm2(request.POST)
        if post.is_valid() and dept.is_valid():
            post.save()
            d = dept.save(commit=False)
            d.Post = Post.objects.latest("id")
            dept.save()
            pid  = Post.objects.latest("id").id
            return HttpResponseRedirect('/accounts/degreereq/%s/' %pid)
        else:
            return HttpResponse("The Post was not created successfully")
    else:
        post= PostForm()
        dept =  PostForm2()

    return render(request, 'admin/post_form.html', {'PostForm': post, 'PostForm2':dept})


def getDepartment(request):
    if request.POST :
        department = DepartmentForm(request.POST)
        if department.is_valid() :
            department.save()
            return HttpResponse('saved to the db')
    else:
        department= DepartmentForm()

    return render(request, 'admin/dept_form.html', {'DepartmentForm': department})


@login_required(login_url='/accounts/login/')

def Admin_Entry_Deg_Req(request,pid):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="Admin"):
        return HttpResponse('You are not a valid user')
    post = Degree_For_Post.objects.filter(Post = Post.objects.get(id = pid))
    #Permissions
    if request.method == 'POST':
        deo_form = Degree_PostForm(request.POST)
        if deo_form.is_valid():

            d = deo_form.save(commit=False)
            d.Post = Post.Objects.get(id =pid)
            d.save()


            return HttpResponseRedirect('requirements')
        else:
            context={
                'deo_form': deo_form,
                'completion': 'complete all the fields before proceding',
                'topic': 'Degree Requirements for Post',
                'pid':pid,
                'post' : post,
            }
            return render_to_response('admin/degree_for_post.html',context)
    else:
        deo_form = Degree_PostForm()

    args = {}
    args.update(csrf(request))

    args['deo_form'] = deo_form
    args['topic']= 'Degree Requirements for Post'
    args['pid']=pid
    args['post'] = post
    return render_to_response('admin/degree_for_post.html',args)


@login_required(login_url='/accounts/login/')

def Admin_Entry_Exp_Req(request,pid):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="Admin"):
        return HttpResponse('You are not a valid user')
    post  = Exp_Post.objects.filter(Post = Post.objects.get(id = pid))
    #Permissions
    if request.method == 'POST':
        deo_form = Exp_PostForm(request.POST)
        if deo_form.is_valid():
            d = deo_form.save(commit=False)
            d.Post = Post.Objects.get(id =pid)
            d.save()


            return HttpResponseRedirect('requirements')
        else:
            context={
                'deo_form': deo_form,
                'completion': 'complete all the fields before proceding',
                'topic': 'Experience Requirements for Post',
                'pid':pid,
                'post' : post,
            }
            return render_to_response('admin/exp_for_post.html',context)
    else:
        deo_form = Exp_PostForm()

    args = {}
    args.update(csrf(request))

    args['deo_form'] = deo_form
    args['topic']= 'Experience Requirements for Post'
    args['pid']=pid
    args['post']=post
    return render_to_response('admin/exp_for_post.html',args)


def Admin_Entry_SubQual_Req(request,pid):
    #Permisionsi
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="Admin"):
        return HttpResponse('You are not a valid user')
    post = subQul_Post.objects.filter(Post= Post.objects.get(id = pid))
    #Permissions
    if request.method == 'POST':
        deo_form = SubQual_PostForm(request.POST)
        if deo_form.is_valid():

            d = deo_form.save(commit=False)
            d.Post = Post.Objects.get(id =pid)
            d.save()


            return HttpResponseRedirect('requirments')
        else:
            context={
                'deo_form': deo_form,
                'completion': 'complete all the fields before proceding',
                'topic': 'Subject Qualification Requirements for Post',
                'pid':pid,
                'post': post
            }
            return render_to_response('admin/subquall_for_post.html',context)
    else:
        deo_form = SubQual_PostForm()

    args = {}
    args.update(csrf(request))

    args['deo_form'] = deo_form
    args['topic']= 'Subject Qualification Requirements for Post'
    args['pid']=pid
    args['post'] = post
    return render_to_response('admin/subquall_for_post.html',args)


def Admin_Entry_Qual_Req(request,pid):
    #Permisions
    log = Users.objects.get(User = request.user)
    if log.UserRole != UserRole.objects.get(Role__exact="Admin"):
        return HttpResponse('You are not a valid user')
    #Permissions
    qual = Qual_For_Post.objects.filter(Post = pid)
    if request.method == 'POST':
        deo_form = Qual_PostForm(request.POST)
        if deo_form.is_valid():

            d = deo_form.save(commit=False)
            d.Post = Post.objects.get(id = pid)
            d.save()

            return HttpResponseRedirect('requirements')
        else:
            context={
                'deo_form': deo_form,
                'completion': 'complete all the fields before proceding',
                'topic': 'Qualification Requirements for Post',
                'pid':pid,
                'qual' : qual,
            }
            return render_to_response('admin/qual_for_post.html',context)
    else:
        deo_form = Qual_PostForm()

    args = {}
    args.update(csrf(request))

    args['deo_form'] = deo_form
    args['topic']= 'Qualification Requirements for Post'
    args['pid']=pid
    args['qual'] = qual
    return render_to_response('admin/qual_for_post.html',args)


def list_of_Posts1(request):
    context  = {
        'd' : Department.objects.all(),
        }
    return render_to_response('admin/Requirements.html',context)



def list_of_Posts2(request,did):
    context = {
        'd' : Post_Dept.objects.filter(Dept= Department.objects.get(id = did))
    }
    return render_to_response('admin/Requirements.html', context)