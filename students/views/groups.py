# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DeleteView

from ..utils import paginate, get_current_group
from ..models import Group	

#Views for Groups	
def groups_list(request):
	
	groups = []
	current_group = get_current_group(request)

	if current_group:
		groups.append(current_group)
	else:
		groups = Group.objects.all()

	#trying to ordergroups
	if request.path == 'groups/':
		groups = groups.order_by('title')
	order_by=request.GET.get('order_by', '')
	if order_by in ('title', 'leader', 'id'): #sorting by title, leader, id
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()

	
	context= {}
	context = paginate(groups, 3, request, context, var_name = 'groups')

	return render(request, 'students/groups_list.html', context)

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
	
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)
	
class GroupDeleteView(DeleteView):
	model = Group
	template_name = 'students/groups_confirm_delete.html'
	
	def get_success_url(self):
		return u'%s?status_message=Студента успішно видалено!' % reverse ('groups')