<<<<<<< HEAD
from django.db import models
=======
﻿from django.db import models
>>>>>>> 58be2f64b9e85d2fc89693035b62c5a192cfae8c
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
<<<<<<< HEAD
		return u"%s %s" % (self.first_name, self.last_name)
=======
		return u"%s %s" % (self.first_name, self.last_name)
>>>>>>> 58be2f64b9e85d2fc89693035b62c5a192cfae8c
