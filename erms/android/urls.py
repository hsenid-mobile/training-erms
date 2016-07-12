from django.conf.urls import url,include
from android.api import api

urlpatterns = [
url(r'^api/',include(api.urls)),
        ]