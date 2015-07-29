# -*- coding: utf-8 -*-
import logging

from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
#from django.contrib import messages
#from django.contrib.messages import get_messages

from studentsdb.settings import ADMIN_EMAIL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

#from django.views.generic.edit import FormView

class ContactForm(forms.Form):	
	#def send_email(self):
	#	pass
	
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
	
	from_email = forms.EmailField(
	label=_(u"Ваша Емейл Адреса"))
	
	subject = forms.CharField(
	label=_(u"Заголовок листа"),
	max_length=128)
	
	message = forms.CharField(
	label=_(u"Текст повідомлення"), 
	widget=forms.Textarea)

def contact_admin(request):
    # check if form was posted
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)

        # check whether user data is valid:
        if form.is_valid():
            # send email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = _(u"An error occured during email transfer. Please, "
                    "try again later.")
                logger = logging.getLogger(__name__)
                logger.exception(message)
            else:
                message = _(u"Message sent successfully!")

            # redirect to same contact page with success message
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('contact_admin'), message))

    # if there was not POST render blank form
    else:
        form = ContactForm()

    return render(request, 'contact_admin/form.html', {'form': form})
"""	
class ContactView(FormView):
	template_name = 'contact_admin/form.html'
	form_class = ContactForm
	success_url = '/email-sent/'
	
	def form_valid(self, form):
		# This method is called for valid data
		from_email = form.cleaned_data['from_email']
		subject = form.cleaned_data['subject'] 
		message = form.cleaned_data['message'] 
		
		send_mail(from_email, subject, message, ['admin@studentsdb.com'])		
		storage = get_messages(self.request)
		for message in storage:
   			pass
		messages.add_message(self.request, messages.INFO, u'Повідомлення відправлено.')
		return super(ContactView, self).form_valid(form)
"""