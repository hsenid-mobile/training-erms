from django.conf.urls import url
from HR import views
from erms.views import logedinHR_view


urlpatterns = [
    url(r'^hr/$', views.home, name='home'),
    url(r'^received_CVs/$', views.received_cvs, name='received_CVs'),
    url(r'^view_cvs/(?P<person_id>[0-9]+)/$', views.view_cvs, name='view_cvs'),
    url(r'^new_post/$', views.create_post, name='new_post'),
    url(r'^addDept/$', views.add_dept, name='addDept'),
    url(r'^degPost/$', views.deg_post, name='degPost'),
    url(r'^qualifications/$', views.qualifications, name='qualifications'),
    url(r'^successPost/$', views.success_post, name='successPost'),
    url(r'^messages/$', views.messages, name='messages'),
    url(r'^vacancies/$', views.vacancies_view, name='vacancies'),
    url(r'^vacancy_cvs/(?P<vacancy_id>[0-9]+)/$', views.vacancy_cvs, name='vacancy_cvs'),
    url(r'^vacancy_cvs/(?P<vacancy_id>[0-9]+)/(?P<person_id>[0-9]+)/$', views.cvs_for_vacancies,name='cvsForVacancies'),
    url(r'^new_message/$', views.send_msg, name='new_message'),
    url(r'^send_cvs/(?P<p_id>[0-9]+)/$', views.send_cvs, name='sendCV'),
    url(r'^send_rec_cvs/(?P<p_id>[0-9]+)/$', views.send_rec_cvs, name='sendRecCV'),

]
