<<<<<<< HEAD
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StudentsAppConfig(AppConfig):
    name = 'students'
    verbose_name = _(u"Students Database")

    def ready(self):
        from students import signals
=======
﻿# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class StudentAppConfig(AppConfig):
	name = 'students'
	verbose_name = _(u'Base Student')
	
	def ready(self):
		from students import signals
>>>>>>> 58be2f64b9e85d2fc89693035b62c5a192cfae8c
