from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError
from django.views.generic import UpdateView, CreateView, DeleteView
from django.utils.translation import ugettext as _

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import FormActions, PrependedText

from .validation import valid_image_minetype, valid_image_size
from django.contrib.messages import get_messages
from django.contrib import messages
from ..utils import paginate, get_current_group

from ..models import Student, Group

def students_list(request):
	# check if we need to show only one group of students
	current_group = get_current_group(request)
	if current_group:
		students = Student.objects.filter(student_group = current_group)
	else:
		# otherwise show all students
		students = Student.objects.all()

	# try to order student list
	order_by = request.GET.get('order_by', 'last_name')
	if order_by in ('last_name', 'first_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()
			
	# apply pagination, 3 students per page
	context = paginate(students, 3, request, {}, var_name='students')
	
	return render(request, 'students/students_list.html', context)
	
class StudentUpdateForm(ModelForm):	
	class Meta:
		model = Student
		fields =  ['first_name', 'last_name', 'middle_name', 'birthday',  'photo', 'ticket', 'student_group', 'notes', 'id']
		
	def __init__(self, *args, **kwargs):
		super(StudentUpdateForm, self).__init__(*args, **kwargs)
		
		self.helper = FormHelper(self)

		# set form tag attributes
		self.helper.form_action = reverse('students_edit', kwargs={'pk': kwargs['instance'].id})		
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		
		# set form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

 		# add buttons
		self.helper.layout = Layout(
			Field('first_name', css_class='input-sm-10'),
			Field('last_name', css_class='input-sm-10'),
			Field('middle_name', css_class='input-sm-10'),
			PrependedText('birthday', '<span class="glyphicon glyphicon-calendar"></span>', active=True, css_class='date'),			
			Field('photo', css_class='input-sm-10'),
			Field('ticket', css_class='input-sm-10'),
			Field('student_group', css_class='input-sm-10'),
			Field('notes',rows=3),				
			FormActions(Submit('add_button',u'Зберегти',css_class="btn btn-primary"),
			Submit('cancel_button',u'Скасувати',css_class="btn btn-link"))
		)

class StudentCreateForm(ModelForm):
	
	class Meta:
		model = Student
		fields =  ['first_name', 'last_name', 'middle_name', 'birthday',  'photo', 'ticket', 'student_group', 'notes', 'id']
		
	def __init__(self, *args, **kwargs):
		super(StudentCreateForm, self).__init__(*args, **kwargs)
			
		self.helper = FormHelper(self)

		# set form tag attributes
		self.helper.form_action = reverse('students_add')		
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		# set form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'
		
 		# add buttons
		self.helper.layout = Layout(
			Field('first_name', css_class='input-sm=10'),
			Field('last_name', css_class='input-sm-10'),
			Field('middle_name', css_class='input-sm-10'),
			PrependedText('birthday', '<span class="glyphicon glyphicon-calendar"></span>', active=True, css_class='date'),
			Field('photo', css_class='input-sm-10'),
			Field('ticket', css_class='input-sm-10'),
			Field('student_group', css_class='input-sm-10'),
			Field('notes',rows=3),
			FormActions(Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
			Submit('cancel_button', u'Скасувати', css_class="btn btn-link"))
		)

class StudentCreateView(CreateView):
	model = Student
	template_name = 'students/students_add.html'
	form_class = StudentCreateForm
		
	def get_success_url(self):
		return u'%s?status_message=%s' % (reverse('home'), _(u"Student added successfully!"))

class StudentUpdateView(UpdateView):
	model = Student
	template_name = 'students/students_edit.html'
	form_class = StudentUpdateForm
	
	def get_success_url(self):
		return u'%s?status_message=%s' % (reverse('home'), _(u"Student updated successfully!"))
		
	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('home'), _(u"Student update canceled!")))
		else:
			return super(StudentUpdateView, self).post(request, *args, **kwargs)
			
	"""
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(StudentUpdateView, self).dispatch(*args, **kwargs)
	"""
		
class StudentDeleteView(DeleteView):
	model = Student
	template_name = 'students/students_confirm_delete.html'
	
	def get_success_url(self):
		return u'%s?status_message=%s' % (reverse('home'),
            _(u"Student deleted successfully!"))
			
	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('home'), _(u"Student delete canceled!")))