# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.views.generic import UpdateView, CreateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import FormActions, PrependedText

from django.contrib.messages import get_messages
from django.contrib import messages
from ..utils import paginate, get_current_group

from ..models import Exam

def exam_list(request):
	# check if we need to show only one group of exam
	group = get_current_group(request)
	if group:
		exam = Exam.objects.filter(group = group)
	else:
		# otherwise show all students
		exam = Exam.objects.all()

	# try to order exam list
	order_by = request.GET.get('order_by', '')
	if order_by in ('name', 'teacher', 'data_time' ,'group'):
		exam = exam.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			exam = exam.reverse()
			
	# apply pagination, 3 exam per page
	context = paginate(exam, 3, request, {}, var_name='exam')
	
	return render(request, 'students/exam_list.html', context)

class BaseExamFormView(object):

    def get_success_url(self):
        return u'%s?status_message=Зміни успішно збережено!' \
            % reverse('exam')

    def post(self, request, *args, **kwargs):
        # handle cancel button
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('exam') + u'?status_message=Зміни скасовано.')
        else:
            return super(BaseExamFormView, self).post(request, *args, **kwargs)
	
class ExamForm(ModelForm):
    class Meta:
		model = Exam
		fields = ['name', 'teacher', 'data_time', 'group']
		
    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # add form or edit form
        if kwargs['instance'] is None:
            add_form = True
        else:
            add_form = False

        # set form tag attributes
        if add_form:
            self.helper.form_action = reverse('exam_add')
        else:
            self.helper.form_action = reverse('exam_edit', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        if add_form:
            submit = Submit('add_button', u'Додати',
                css_class="btn btn-primary")
        else:
            submit = Submit('save_button', u'Зберегти',
                css_class="btn btn-primary")
        self.helper.layout = Layout(
			Field('name', css_class='input-sm-10'),
			Field('teacher', css_class='input-sm-10'),
			PrependedText('data_time', '<span class="glyphicon glyphicon-calendar"></span>', active=True, css_class='date'),
			Field('group', css_class='input-sm-10'),
			FormActions(submit,Submit('cancel_button', u'Скасувати', css_class="btn btn-link"))
		)
	
class ExamCreateView(BaseExamFormView, CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'students/exam_add.html'
	
class ExamUpdateView(BaseExamFormView, UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'students/exam_edit.html'
	
class ExamDeleteView(BaseExamFormView, DeleteView):
	model = Exam
	template_name = 'students/exam_confirm_delete.html'