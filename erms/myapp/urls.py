from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from myapp.views import *
import myapp
from myapp import views
app_name = 'myapp'


urlpatterns = [
    url(r'^$', hod),
    url(r'^selection_inter/', selection_interview),
    url(r'^selection_cv/(\d+)/', selection_cv),
    url(r'^selection_profile/(\d+)/', selection_profile),
    url(r'^post_list/$', hod_post_list),
    url(r'^hod_vacancy/(\d+)/$', hod_vacancy),
    url(r'^hod_vacancy/succs/$', hod_vacancy_succs),
    url(r'^hod_vacancy/test/$', hod_vacancy_test),
    url(r'^hod_vacancy/test2/(\d+)/$', hod_inter2_create),
    url(r'^hod_vacancy/test2/succs/$', hod_inter2_create_succs),
    url(r'^hod_vacancy/test2/part2/inter_list/(\d+)/(\d+)/$', hod_pre_interviwer_list2, name="inter12"),
    url(r'^hod_vacancy/test2/part2/inter_list/(\d+)/(\d+)/(\d+)/$', hod_inter2_interviewer_2, name="inter22"),
    url(r'^hod_vacancy/test/part2/vacancy_list_cv/$', hod_vacancy_list_cv),
    url(r'^hod_vacancy/test/part2/inter_list_cv/(\d+)', hod_inter_list_cv),
    url(r'^hod_vacancy/test2/part2/inter_list_cv/(\d+)/(\d+)/$', hod_pre_cv_list2, name="cv12"),
    url(r'^hod_vacancy/test/part2/inter_list_cv/(\d+)/(\d+)/$', hod_inter_cv, name="cv2"),
    url(r'^hod_vacancy/test2/part2/inter_list_cv/(\d+)/(\d+)/$', hod_inter2_cv, name="cv22"),
    url(r'^hod_recruit_previous/',hod_recruit_previous),
    url(r'^hod_recruit1_previous/(\d+)',hod_recruit1_previous),
    url(r'^hod_recruit_previous_overview/(\d+)',hod_recruit_previous_overview),
    url(r'^hod_recruit/',hod_recruit),
    url(r'^hod_recruit1/(\d+)',hod_recruit1),
    url(r'^hod_recruit_cv/(\d+)',hod_recruit2),
    url(r'^hod_recruit3/(\d+)/(\d+)', hod_recruit3),
    url(r'^hod_interviewdone/(\d+)', interview_done),
    url(r'^hod_vacancy/test/vacancy/(?P<ID>[0-9]+)/$', hod_view_vacancy),
    url(r'^hod_cv/$', hod_cv),
    url(r'^hod_cv/(\d+)/$', hod_profile),
    url(r'^hod_cv/cv_list/(\d+)/', hod_cv_list),
    url(r'^hod_inter/$', hod_inter),
    url(r'^hod_inter/chs_vacn/$', hod_inter_choose_vacancy),
    url(r'^hod_inter/hod_inter_overview/$', hod_inter_overview),
    url(r'^hod_inter/hod_inter_overview/view/(\d+)', hod_inter_view),
    #url(r'^hod/hod_inter/hod_inter_overview/view/up/(\d+)', hod_inter_view_select),
    url(r'^hod_inter/hod_succs$', hod_succs),
    url(r'^hod_msg/$', hod_msg),
    url(r'^sub/$', subv),

]