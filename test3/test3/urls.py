"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp.views import *
from myapp import views
app_name = 'myapp'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login),
    # url(r'^reg/$', Register, name='reg'),
    url(r'^deo/$', deo),
    url(r'^deo/deo_submit/$', deo_submit),
    url(r'^deo/deo_submit/deo_profile', deo_profile),
    url(r'^hod/$', hod),
    url(r'^hod/hod_vacancy/$', hod_vacancy),
    url(r'^hod/hod_vacancy/succs/$', hod_vacancy_succs),
    url(r'^hod/hod_vacancy/test/$', hod_vacancy_test),
    url(r'^hod/hod_vacancy/test/(?P<vid>[0-9]+)/$', hod_inter_create),
    url(r'^hod/hod_vacancy/test/(?P<vid>[0-9]+)/part2/$', hod_inter_cv, name="inter2"),
    url(r'^hod/hod_vacancy/test/(?P<vid>[0-9]+)/part2/(?P<cv>[0-9]+)$', hod_inter_cv, name="inter2"),
    url(r'^hod/hod_vacancy/test/vacancy/(?P<vid>[0-9]+)/$', hod_view_vacancy),
    url(r'^hod/hod_cv/$', hod_cv),
    url(r'^hod/hod_cv/(?P<NIC>[^/]+)/$', hod_profile),
    url(r'^hod/hod_inter/$', hod_inter),
    url(r'^hod/hod_inter/chs_vacn/$', hod_inter_choose_vacancy),
    url(r'^hod/hod_vacancy/test/part2/$', hod_inter_cv),
    url(r'^hod/hod_inter/hod_inter_overview/$', hod_inter_overview),
    url(r'^hod/hod_inter/hod_succs$', hod_succs),
    url(r'^hod/hod_msg/$', hod_msg),
    url(r'^hod/hod_msg/send/$', hod_send_msg),
    url(r'^hod/hod_msg/send/succs$', hod_msg_succs),
    url(r'^hod/hod_msg/recieve/$', hod_recieve_msg),
    url(r'^sub/$', subv),

]
