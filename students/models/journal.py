# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Journal(models.Model):
	class Meta(object):
		verbose_name =_(u"Exam")
		verbose_name_plural = _(u"Exams")
		
	first_name=models.CharField(
		max_length=256,
		blank=False,
		verbose_name=_(u"First Name"))
		
	last_name=models.CharField(
		max_length=256,
		blank=False,
		verbose_name=_(u"Last Name"))

	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)