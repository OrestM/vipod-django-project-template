<<<<<<< HEAD
# -*- coding: utf-8 -*-
from django.db import models
=======
﻿from django.db import models
>>>>>>> 58be2f64b9e85d2fc89693035b62c5a192cfae8c
from django.utils.translation import ugettext_lazy as _

class MonthJournal(models.Model):
	# add to class model monthjournal
	class Meta:
		verbose_name = _(u"Monthly Journal")
		verbose_name_plural = _(u"Monthly Journals")
	
	# field peg student
	student  = models.ForeignKey('Student',
		verbose_name=_(u"Student"),
		blank=False,
		unique_for_month='date') # add new attribute which works coupled with date
			
	# we only need year and month, so always set day to first day of the month
	date = models.DateField(
		verbose_name=_(u"Date"),
		blank=False)
	"""		
	# list of days, each says whether was presence or not
	present_day1 = models.BooleanField(default=False)
	present_day2 = models.BooleanField(default=False) 
	present_day3 = models.BooleanField(default=False) 
	present_day4 = models.BooleanField(default=False) 
	present_day5 = models.BooleanField(default=False) 
	present_day6 = models.BooleanField(default=False)
	present_day7 = models.BooleanField(default=False) 
	present_day8 = models.BooleanField(default=False) 
	present_day9 = models.BooleanField(default=False) 
	present_day10 = models.BooleanField(default=False) 
	present_day11 = models.BooleanField(default=False) 
	present_day12 = models.BooleanField(default=False) 
	present_day13 = models.BooleanField(default=False) 
	present_day14 = models.BooleanField(default=False) 	
	present_day15 = models.BooleanField(default=False) 
	present_day16 = models.BooleanField(default=False) 
	present_day17 = models.BooleanField(default=False) 
	present_day18 = models.BooleanField(default=False) 
	present_day19 = models.BooleanField(default=False) 
	present_day20 = models.BooleanField(default=False) 
	present_day21 = models.BooleanField(default=False)
	present_day22 = models.BooleanField(default=False)
	present_day23 = models.BooleanField(default=False)
	present_day24 = models.BooleanField(default=False)
	present_day25 = models.BooleanField(default=False)
	present_day26 = models.BooleanField(default=False)
	present_day27 = models.BooleanField(default=False)
	present_day28 = models.BooleanField(default=False)
	present_day29 = models.BooleanField(default=False)
	present_day30 = models.BooleanField(default=False)
	present_day31 = models.BooleanField(default=False)
	"""
	day = locals()
	for field_number in range(1,32):
<<<<<<< HEAD
		day['present_day'+str(field_number)]=models.BooleanField(verbose_name = u'День '+str(field_number),
		default=False)	
	
	def __unicode__(self):
		return u'%s: %d, %d' % (self.student.last_name, self.date.month, self.date.year)
=======
		day['present_day'+str(field_number)]=models.BooleanField(verbose_name = u'День '+str(field_number), 
		default=False)	
	
	def __unicode__(self):
		return u'%s: %d, %d' % (self.student.last_name, self.date.month, self.date.year)
>>>>>>> 58be2f64b9e85d2fc89693035b62c5a192cfae8c
