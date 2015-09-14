"""
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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView, TemplateView

#from students.views.contact_admin import ContactView
from students.views.students import StudentUpdateView, StudentCreateView, StudentDeleteView
from students.views.groups import GroupAddView, GroupDeleteView, GroupUpdateView
from students.views.journal import JournalView
from students.views.exam import ExamCreateView, ExamUpdateView, ExamDeleteView
from django.http import HttpResponse, HttpResponseRedirect

from .settings import MEDIA_ROOT, DEBUG

js_info_dict = {
	'packages': ('students',),	
}

urlpatterns = patterns('',
	# Students urls
	url(r'^$', 'students.views.students.students_list', name='home'),
	url(r'^students/add/$', login_required(StudentCreateView.as_view()), name='students_add'),
	url(r'^students/(?P<pk>\d+)/edit/$', login_required(StudentUpdateView.as_view()), name='students_edit'),
	url(r'^students/(?P<pk>\d+)/delete/$', login_required(StudentDeleteView.as_view()), name='students_delete'),
	
	
	#Groups urls
	url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
	url(r'^groups/add/$', login_required(GroupAddView.as_view()), name='groups_add'),
	url(r'^groups/(?P<pk>\d+)/edit/$', login_required(GroupUpdateView.as_view()), name='groups_edit'),
	url(r'^groups/(?P<pk>\d+)/delete/$', login_required(GroupDeleteView.as_view()), name='groups_delete'),
	
	#Journal
	url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),
	
	
	#Exam
	url(r'^exam/$', 'students.views.exam.exam_list', name='exam'),
	url(r'^exam/add/$', login_required(ExamCreateView.as_view()), name='exam_add'),
	url(r'^exam/(?P<pk>\d+)/edit/$', login_required(ExamUpdateView.as_view()), name='exam_edit'),
	url(r'^exam/(?P<pk>\d+)/delete/$', login_required(ExamDeleteView.as_view()), name='exam_delete'),
		
	# Contact Admin Form
	url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin'),
	#url(r'^contact-admin/$', ContactView.as_view(), name='contact_admin'),
	#url(r'^', ContactView.as_view(), name='email-sent'),
		
	# User Related urls
	url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),	
	url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
	url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
	url(r'^users/', include('registration.backends.simple.urls', namespace='users')),
	
	# Social Auth Related urls
	url('^social/', include('social.apps.django_app.urls', namespace='social')),
	
	url(r'^jsi18n\.js$', 'django.views.i18n.javascript_catalog', js_info_dict),
	
	url(r'^admin/', include(admin.site.urls)),
	
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
