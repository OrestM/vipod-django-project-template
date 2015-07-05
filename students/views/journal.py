# -*- coding: utf-8 -*-

from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr

from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView

from ..models import MonthJournal, Student
from ..utils import paginate

class JournalView(TemplateView):
	template_name = 'students/journal.html'
	
	def get_context_data(self, **kwargs):
		# get context data from TemplateView class
		context = super(JournalView, self).get_context_data(**kwargs)
		
		# check if we need to display some specific month
		if self.request.GET.get('month'):
			month = datetime.strptime(self.request.GET['month'], '%Y-%m-%d').date()
		else:
			# otherwise just displaying current month data
			today = datetime.today()
			month = date(today.year, today.month, 1)
		
		# calculate current, previous and next month detalis;
		# we need this for month navigation element in template_name
		next_month = month + relativedelta(month=1)
		prev_month = month - relativedelta(month=1)
		context['prev_month'] = prev_month.strftime('%Y-%m-%d')
		context['next_month'] = next_month.strftime('%Y-%m-%d')
		context['year'] = month.year
		context['month_verbose'] = month.strftime('%B')
		
		# we'll use this variable in students pagination
		context['cur_month'] = month.strftime('%Y-%m-%d')
		
		# prepare variable for template to generate
		# journal table header elements
		myear, mmonth = month.year, month.month
		number_of_days = monthrange(myear, mmonth)[1]
		context['month_header'] = [{'day': d,
			'verbose': day_abbr[weekday(myear, mmonth, d)][:2]}
			for d in range(1, number_of_days+1)]
			
		# get all students from database
		queryset = Student.objects.order_by('last_name')
		
		# url to update student presence, for from post
		update_url = reverse('journal')
		
		# go over all students and collect data about presence
		# during selected month
		students = []
		for student in queryset:
			# try to get journal objects by month selected
			# during selected month
			try:
				journal = MonthJournal.objects.get(student=student, date=month)
			except Exception:			
				journal = None
				
			# fill in days presence list for current student
			days = []
			for day in range(1, 31):
				days.append({
					'day': day,
					'present': True,
					'date': date(2014, 7, day).strftime(
						'%Y-%m-%d'),
				})
			
		# prepare metadata for current student
		students.append({
			'fullname': u'%s %s' % (student.last_name, student.first_name),
			'days': days,
			'id': student.id,
			'update_url': update_url,
		})
		
		# apply pagination, 10 students per page
		context = paginate(students, 10, self.request, context, var_name='students')
		
		# finaly return updated context with paginated students
		return context