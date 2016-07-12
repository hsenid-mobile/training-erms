from django.conf.urls import url
from .views import *
from erms.views import *

urlpatterns = [
    url(r'^DEO/logedin', logedindeo_view),
    url(r'^DEO/entry',DEO_Entry),
    url(r'^DEO/personal_info',DEO_Entry_Personal),
    url(r'^DEO/degreechoice',DEO_DegreeChoice),
    url(r'^DEO/intermediarycheck',DEO_Intermediary),
    url(r'^DEO/cv_profile/(\d+)',DEO_CV_Profile),
    url(r'^DEO/ordinarylevel',DEO_Entry_Ordinary),
    url(r'^DEO/advancedlevel',DEO_Entry_Advanced),
    url(r'^DEO/advancedqualresult',DEO_Entry_AdvancedQualResult),
    url(r'^DEO/ordinaryqualresult',DEO_Entry_OrdinaryQualResult),
    # url(r'^DEO/degreetype',degreeType),
    url(r'^DEO/qualification',DEO_Entry_Qualification),
    url(r'^DEO/sub_qualification',DEO_Entry_SubQualification),
    url(r'^DEO/skills',DEO_Entry_Skills),
    url(r'^DEO/extra_info',DEO_Entry_Extra),
    url(r'^DEO/sport_info',DEO_Entry_Sport),
    url(r'^DEO/experience_info',DEO_Entry_Experience),
    url(r'^DEO/spcl_achvmnt_info',DEO_Entry_Special_Ach),
    url(r'^DEO/intermediary',DEO_Intermediary),
    url(r'^DEO/success', success_post),


]