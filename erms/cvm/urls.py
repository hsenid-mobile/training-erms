from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^add/$', 'cvm.views.addCVs', name='addcv')
                       )