"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, include, url
from django.contrib import admin

from students.views.contact_admin import ContactView
from students.views.students import StudentUpdateView, StudentCreateView, StudentDeleteView
from students.views.groups import GroupAddView, GroupDeleteView, GroupUpdateView
from students.views.journal import JournalView
from django.http import HttpResponse, HttpResponseRedirect

urlpatterns = patterns('',
	# Students urls
	url(r'^$', 'students.views.students.students_list', name='home'),
	url(r'^students/add/$', StudentCreateView.as_view(), name='students_add'),
	url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
	url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),
	
	
	#Groups urls
	url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
	url(r'^groups/add/$', GroupAddView.as_view(), name='groups_add'),
	url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='groups_edit'),
	url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='groups_delete'),
	
	#Journal
	url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),
	
	
	#Exam
	url(r'^exam/$', 'students.views.exam.exam_list', name='exam'),
	
    url(r'^admin/', include(admin.site.urls)),
	
	# Contact Admin Form
	url(r'^contact-admin/$', ContactView.as_view(), name='contact_admin'),
	url(r'^', ContactView.as_view(), name='email-sent'),
	
	
	#This if forgot password
	url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
	url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
	url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
)

from .settings import MEDIA_ROOT, DEBUG

if DEBUG:
	#serve files from media folder
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}))		