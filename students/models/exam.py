<<<<<<< HEAD
from django.db import models
=======
﻿from django.db import models
>>>>>>> 58be2f64b9e85d2fc89693035b62c5a192cfae8c
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
<<<<<<< HEAD
		return u"%s %s %s" % (self.name, self.teacher, self.group)
=======
		return u"%s %s %s" % (self.name, self.teacher, self.group)
>>>>>>> 58be2f64b9e85d2fc89693035b62c5a192cfae8c
