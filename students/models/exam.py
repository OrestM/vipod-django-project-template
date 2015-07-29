# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Exam(models.Model):
	
	class Meta(object):
		verbose_name = _(u"Exam")
		verbose_name_plural = _(u"Exams")
	
	name=models.CharField(
		max_length=256,
		blank=False,
		verbose_name=_(u"Name of the subject"))
		
	data_time=models.DateField(
		blank=False,
		verbose_name=_(u"data and time"),
		null=True)
		
	teacher=models.CharField(
		max_length=256,
		blank=False,
		verbose_name=_(u"Teacher"),
		default='')
		
	group = models.ForeignKey('Group',
		verbose_name=_(u"Group"),
		blank=False,
		null=True,
		on_delete=models.PROTECT)
		
	def __unicode__(self):
		return u"%s %s %s" % (self.name, self.teacher, self.group)