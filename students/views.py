# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#Views for Students

def students_list(request):
	students = (
		{'id': 1,
		 'first_name': u'Корост',
		 'last_name': u'Андрій',
		 'ticket': 2123,
		 'image': 'img/pin.png'},
		{'id': 2,
		 'first_name': u'Корпюк',
		 'last_name': u'Роман',
		 'ticket': 215,
		 'image': 'img/pin.png'},
		{'id': 3,
		 'first_name': u'Гриців',
		 'last_name': u'Віктор',
		 'ticket': 28,
		 'image': 'img/pin.png'},
	)
	return render(request, 'students/students_list.html', {'students': students})
	
def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')
	
def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)
	
def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

#Views for Groups
	
def groups_list(request):
	groups = (
		{'id': 1,
		 'name': u'МтМ-21',
		 'leader': u'Ячмене Олег'},
		{'id': 2,
		 'name': u'МтМ-22',
		 'leader': u'Муха Орест'},
		{'id': 3,
		 'name': u'МтМ-23',
		 'leader': u'Іванов Андрій'},
	)
	return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
	
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)
	
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
	
