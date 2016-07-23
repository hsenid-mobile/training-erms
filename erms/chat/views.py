from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.shortcuts import RequestContext, redirect
from ermsapp.models import User, Messages, Users
from chat.forms import *
from django.utils.timezone import now

# Create your views here.
def Chats(request):
    chats1 = Messages.objects.filter(Reciever=request.user).distinct('Sender')
    chats2 = Messages.objects.filter(Sender = request.user).distinct('Reciever')
    #chatsender = chats.Sender.distinct()
    #chatreciever = chats.Reciever.distinct()
    #allchats =
    
    context = {
        #'chats' : Messages.objects.filter(Q(Reciever=request.user) | Q(Sender = request.user)),
        'senders':chats1,
        'recievers': chats2,
        'topic' : "Chats"
        }
    return render_to_response('messages/chats.html', context)

def Home(request,partner):
    c = Messages.objects.filter(Reciever=request.user,Sender = partner).distinct("Sender")
    d = Messages.objects.filter(Sender=request.user, Reciever = partner).distinct("Reciever")
    return render(request, "messages/home.html", {'home': 'active', 'chat': c })

def Post(request,reciever):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Messages(Sender=request.user,Reciever = reciever, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')


def Message(request,reciever):
    c = Messages.objects.filter(Sender=request.user,Reciever = reciever)
    return render(request, 'alpha/messages.html', {'chat': c})


def send_msg(request):
    context = RequestContext(request)
    if request.method == 'POST':
        msg_form = MessageForm(request.POST)
        if msg_form.is_valid():
            msgData = msg_form.save(commit=False)
            msgData.Sender = request.user
            msgData.SentDate = now()
            msgData.SentTime = now()
            msgData.save()
            return redirect('/messages/send_messages/success/')
        else:
            print(msg_form.errors)
    else:
        msg_form = MessageForm()
    return render_to_response('messages/send_messages.html', {'msg_form': msg_form}, context)


def send_msg_success(request):
    return render(request, 'messages/msg_success.html', {})