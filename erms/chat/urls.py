from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Chats, name='chat'),
    url(r'^home/(\d+)/$', views.Home, name='home'),
    url(r'^post/$', views.Post, name='post'),
    url(r'^messages/(\d+)/$', views.Message, name='messages'),
    url(r'^send_messages/$', views.send_msg, name='send_messages'),
    url(r'^send_messages/success/$', views.send_msg_success, name='send_messages_success'),
    ]