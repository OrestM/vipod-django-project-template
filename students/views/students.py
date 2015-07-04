# -*- coding: utf-8 -*-
# новий шмпотр в модулі
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm, ValidationError
from django.views.generic import UpdateView, CreateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from .validation import valid_image_minetype, valid_image_size
from django.contrib.messages import get_messages
from django.contrib import messages
from ..utils import paginate, get_current_group

from ..models import Student, Group

def students_add(request):
	# was form posted?
	if request.method == "POST":
	  
		# was form add button clicked?
		if request.POST.get('add_button') is not None:
	    
			# TODO: varidate input from user
			# errors collection
			errors = {}
			# validate student data will go here
			data = {'middle_name': request.POST.get('middle_name'), 'notes': request.POST.get('notes')}
			
			# validate user input
			first_name = request.POST.get('first_name', '').strip()
			if not first_name:
				errors['first_name'] = u"Ім'я є обов'язковим"
			else:
				data['first_name'] = first_name
				
			last_name = request.POST.get('last_name', '').strip()
			if not last_name:
				errors['last_name'] = u"Прізвище є обов'язковим"
			else:
				data['last_name'] = last_name
				
			birthday = request.POST.get('birthday', '').strip()
			if not birthday:
				errors['birthday'] = u"Дата Народження є обов'язковою"
			else:
				try:
					datetime.strptime(birthday, '%Y-%m-%d')
				except Exeption:
					errors['birthday'] = u"Введіть коректний формат дати (напр. 1994-08-24)"
				else:
					data['birthday'] = birthday
				
			ticket = request.POST.get('ticket', '').strip()
			if not ticket:
				errors['ticket'] = u"№ білета є обов'язковим"
			else:
				data['ticket'] = ticket
				
			student_group = request.POST.get('student_group', '').strip()
			if not student_group:
				errors['student_group'] = u"Оберіть групу для студента"
			else:
				groups = Group.objects.filter(pk=student_group)
				if len(groups) != 1:
					errors['student_group'] = u"Оберіть коректну групу"
				else:
					data['student_group'] = groups[0]
				
			photo = request.FILES.get('photo')
			if photo:
				correct_photo = valid_image_minetype(photo) # image photo
				if correct_image:
					correct_file_size = valid_image_size(photo) # image size
					if correct_file_size:
						data['photo'] = photo
					else:
						errors['photo'] = u"Файл завеликий"
				else:
					errors['photo'] = u"Виберіть фото яке займає менше 2mb"
			
			# message django.contrib.messages 
			storage = get_messages(request)
			for message in storage:
				pass # empty block
			if errors:
			# add errors
				for name_error in errors:
					messages.add_message(request, messages.INFO, errors[name_error])
			# end django.contrib.messages 
			
			# save studentd
			if not errors:
				student = Student(**data)
				student.save()
			
				# redirect user to students list
				return HttpResponseRedirect(u'%s?status_message=Студента %s %s успішно додано!' % (reverse('home'), data['first_name'], data['last_name']))
			else:
				# render from with errors and previous user input
				return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title'), 'errors': errors})
		elif request.POST.get('cancel_button') is not None:
			# redirect to home page on cancel button
			return HttpResponseRedirect(u'%s?status_message=Додавання студента скасовано' % reverse('home'))
	else:
		# initial form render
		return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})

class StudentUpdateForm(ModelForm):
	method = 'update'
	
	class Meta:
		model = Student
		fields =  ['first_name', 'last_name', 'middle_name', 'birthday',  'photo', 'ticket', 'student_group', 'notes', 'id']
		
	def __init__(self, *args, **kwargs):
		super(StudentUpdateForm, self).__init__(*args, **kwargs)
		
		self.helper = FormHelper(self)

		# set form tag attributes
		if 'update' in self.method:
			self.helper.form_action = reverse('students_edit',	kwargs={'pk': kwargs['instance'].id})
		else:		
			self.helper.form_action = reverse('students_add') 		
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
			Submit('cancel_button_add', u'Скасувати', css_class="btn btn-link"),
		)
		
class StudentCreateForm(StudentUpdateForm):
	method = 'create'
	
	def __init__(self, *args, **kwargs):
		super(StudentCreateForm, self).__init__(*args, **kwargs)
		
def students_list(request):

	current_group = get_current_group(request)
	if current_group:
		students = Student.objects.filter(student_group = current_group)
	else:
		#get all students
		students = Student.objects.all()

	#trying to order student list
	if request.path == '/':
		students = students.order_by('last_name')
	order_by=request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name', 'ticket', 'id'): #order by last_name, first_name, ticket, id
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	context= {}
	context = paginate(students, 3, request, {}, var_name = 'students')
	return render(request, 'students/students_list.html', context)
		
class StudentCreateView(CreateView):
	model = Student
	template_name = 'students/students_add.html'
	form_class = StudentCreateForm

	def get_success_url(self):
		return u'%s?status_message=Студента збережено!' % reverse('home')
			
class StudentUpdateView(UpdateView):
	model = Student
	template_name = 'students/students_edit.html'
	form_class = StudentCreateForm
		
	def get_success_url(self):
		return u'%s?status_message=Студента успішно збережено!' % reverse ('home')
		
	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect( u'%s?status_message=Редагування студента відмінено!' % reverse('home'))
		return super(StudentUpdateView, self).post(request, *args, **kwargs)
		
class StudentDeleteView(DeleteView):
	model = Student
	template_name = 'students/students_confirm_delete.html'
	
	def get_success_url(self):
		return u'%s?status_message=Студента успішно видалено!' % reverse ('home')