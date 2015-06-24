# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.views.generic import DeleteView, UpdateView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..utils import paginate, get_current_group
from ..models import Group	

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
	
class GroupUpdateForm(ModelForm):
	class Meta:
		model = Group
		fields =  ['title', 'leader', 'notes']
		
	def __init__(self, *args, **kwargs):
		super(GroupUpdateForm, self).__init__(*args, **kwargs)
		
		self.helper = FormHelper(self)

		# set form tag attributes
		self.helper.form_action = reverse('groups_edit',	kwargs={'pk': kwargs['instance'].id})
				
 		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		# set form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'
		
 		# add buttons
		self.helper.layout[-1] = FormActions(
			Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
			Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
		)


def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
	
class GroupUpdateView(UpdateView):
	model = Group
	template_name = 'students/groups_edit.html'
	form_class = GroupUpdateForm
		
	def get_success_url(self):
		return u'%s?status_message=Групу успішно збережено!' % reverse('groups')
		
	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect( u'%s?status_message=Редагування групи відмінено!' % reverse('groups'))
		return super(GroupUpdateView, self).post(request, *args, **kwargs)
	
class GroupDeleteView(DeleteView):
	model = Group
	template_name = 'students/groups_confirm_delete.html'
	
	def get_success_url(self):
		return u'%s?status_message=Студента успішно видалено!' % reverse ('groups')