__author__ = 'Robin'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout/$', views.logout_page),
    url(r'^register/$', views.register_page),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^park', views.park_page),
    url(r'^contact$', views.contact_page),
    url(r'', views.main_page, name='main_page'),

]
