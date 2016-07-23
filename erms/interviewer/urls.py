from django.conf.urls import url
from .views import *
from erms.views import logedininterviewer_view

urlpatterns = [
    url(r'^logedin',logedininterviewer_view),
    url(r'^interview_list',Interviewer_Interview_List),
    url(r'^cv_list/(\d+)$',Interviewer_Cv_list),
    url(r'^cv_list/(\d+)/(\d+)$',Interviewer_Cv_list),
    url(r'^cv_profile/(\d+)$',Interviewer_CV_Profile),

]