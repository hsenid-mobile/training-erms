from django.contrib import admin

# Register your models here.
# from .forms import InfoBasicForm
# from .forms import CreateUserForm
from .models import InfoBasic
from .models import CreateUser


# class InfoAdmin(admin.ModelAdmin):
#         list_display = ['First_name', 'pub_date', 'updated']

admin.site.register(InfoBasic)

# class UserAdmin(admin.ModelAdmin):
#      form = CreateUserForm,

admin.site.register(CreateUser)
