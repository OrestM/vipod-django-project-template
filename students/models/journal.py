# -*- coding: utf-8 -*-

from django.db import models

class Journal(models.Model):

	class Meta(object):
		verbose_name = u"Журнал"
		
	first_name=models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім'я")
		
	last_name=models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Прізвище")

	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)