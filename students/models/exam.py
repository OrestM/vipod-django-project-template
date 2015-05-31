# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Exam(models.Model):
	
	class Meta(object):
		verbose_name = u"Іспит"
		verbose_name_plural = u"Іспити"
	
	name=models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Назва Предмету")
		
	data_time=models.DateField(
		blank=False,
		verbose_name=u"Дата і Час")
		
	teacher=models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Викладач",
		default='')
		
	group = models.ForeignKey('Group',
		verbose_name=u"Група",
		blank=False,
		null=True,
		on_delete=models.PROTECT)
		
	
	def __unicode__(self):
		return u"%s %s %s" % (self.name, self.data_time, self.teacher)