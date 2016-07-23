
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from tastypie.resources import ModelResource
from ermsapp.models import Interview_Interviewer,Interview,Personal,Messages,Personal_Interview_viewer,Personal_Interview, \
    Vacancy, Post_Dept, Post
from django.contrib.auth.models import User
from tastypie.api import Api

class UserResource(ModelResource):
    class Meta:

     queryset = User.objects.all()
     resource_name = 'User'
     excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
     filtering = {
         'username': ALL
     }

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'Post'
        fields = ['Post']

class Post_DeptResource(ModelResource):
    Post = fields.ForeignKey(PostResource,'Post',full=True)

    class Meta:
        queryset = Post_Dept.objects.all()
        resource_name = 'Post_Dept'
        fields = ['Post']

class VacancyResource(ModelResource):
    Post_Dept = fields.ForeignKey(Post_DeptResource,'Post_Dept',full=True)
    class Meta:

        queryset = Vacancy.objects.all()
        resource_name = 'Vacancy'
        fields = ['Post_Dept']

class InterviewResource(ModelResource):
    Vacancy = fields.ForeignKey(VacancyResource,'Vacancy',full=True)

    class Meta:

        queryset = Interview.objects.all()
        resource_name = 'Interview'
        fields = ['Time','Date','id']
        filtering = {
            'id':ALL
        }

class Interview_InterviewerResource(ModelResource):
    InterviewerColumn = fields.ForeignKey(UserResource,'Interviewer')
    InterviewColumn = fields.ForeignKey(InterviewResource,'Interview',full=True)

    class Meta:
        queryset =Interview_Interviewer.objects.all()
        resource_name = 'Interview_Interviewer'
        filtering={
           'User': ALL_WITH_RELATIONS,
           'InterviewerColumn': ALL_WITH_RELATIONS,
        }

class PersonalResource(ModelResource):
    class Meta:
        queryset = Personal.objects.all()
        resource_name = 'Personal'
        fields = ['NIC','FullName','DOB','Nationality','AddressLine1','AddressLine2','AddressLine3','ContactNum','Email','FacebookProf','LinkedInProf','Objective','SpecialNotes']
        filtering = {
            'NIC':ALL
        }

class Personal_InterviewResource(ModelResource):
    InterviewColumn = fields.ForeignKey(InterviewResource, 'Interview')
    PersonalColumn = fields.ForeignKey(PersonalResource, 'Personal', full=True)

    class Meta:
        queryset = Personal_Interview.objects.all()
        resource_name = 'Personal_Interview'
        filtering = {
            'Interview':ALL_WITH_RELATIONS,
            'InterviewColumn':ALL_WITH_RELATIONS
        }

class Personal_Interview_viewerResource(ModelResource):
    InterviewerColumn = fields.ForeignKey(UserResource,'Interviewer')
    Personal_InterviewColumn = fields.ForeignKey(Personal_InterviewResource,'Personal_Interview')

    class Meta:
        queryset = Personal_Interview_viewer.objects.all()
        resource_name = 'Personal_Interview_viewer'
        authorization = Authorization()
        always_return_data = True


api = Api(api_name='andro')

api.register(UserResource())
api.register(InterviewResource())
api.register(Interview_InterviewerResource())
api.register(Personal_InterviewResource())
api.register(PersonalResource())
api.register(Personal_Interview_viewerResource())