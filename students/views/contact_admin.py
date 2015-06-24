# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.messages import get_messages

from studentsdb.settings import ADMIN_EMAIL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.views.generic.edit import FormView

class ContactForm(forms.Form):
	from_email = forms.EmailField(label=u"Ваша Емейл Адреса")
	subject = forms.CharField(label=u"Заголовок листа", max_length=128)
	message = forms.CharField(label=u"Текст повідомлення", widget=forms.Textarea)
	
	def send_email(self):
		pass
	
	def __init__(self, *args, **kwargs):
		# call original initializator
		super(ContactForm, self).__init__(*args, **kwargs)
		
		#this helper object allows us to customize form
		self.helper = FormHelper()
		
		# form tag attributes
		self.helper.form_class = 'form-horizontal'
		self.helper.form_method = 'post'
		self.helper.form_action = reverse('contact_admin')
		
		# twitter bootstrap styles
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'
		
		# form buttons
		self.helper.add_input(Submit('send_button', u'Надіслати'))
	
class ContactView(FormView):
	template_name = 'contact_admin/form.html'
	form_class = ContactForm
	success_url = '/email-sent/'
	
	def form_valid(self, form):
		"""This method is called for valid data"""
		from_email = form.cleaned_data['from_email']
		subject = form.cleaned_data['subject'] 
		message = form.cleaned_data['message'] 
		
		send_mail(from_email, subject, message, ['admin@studentsdb.com'])		
		storage = get_messages(self.request)
		for message in storage:
   			pass
		messages.add_message(self.request, messages.INFO, u'Повідомлення відправлено.')
		return super(ContactView, self).form_valid(form)