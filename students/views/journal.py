# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from ..models import Journal
from ..models import Group
from ..models import Student

def journal_list(request):
	groups = Group.objects.all()
	
	students = Student.objects.all()
	
	journal = Journal.objects.all()
	
	journal = (
		{'day_of_weak': u'Пн',
		 'day': 1},
		{'day_of_weak': u'Вт',
		 'day': 2},
		{'day_of_weak': u'Ср',
		 'day': 3},
		{'day_of_weak': u'Чт',
		 'day': 4},
		{'day_of_weak': u'Пт',
		 'day': 5},
		{'day_of_weak': u'Сб',
		 'day': 6},
		{'day_of_weak': u'Нд',
		 'day': 7},
		{'day_of_weak': u'Пн',
		 'day': 8},
		{'day_of_weak': u'Вт',
		 'day': 9},
		{'day_of_weak': u'Ср',
		 'day': 10},
		{'day_of_weak': u'Чт',
		 'day': 11},
		{'day_of_weak': u'Пт',
		 'day': 12},
		{'day_of_weak': u'Сб',
		 'day': 13},
		{'day_of_weak': u'Нд',
		 'day': 14},
		{'day_of_weak': u'Пн',
		 'day': 15},
		{'day_of_weak': u'Вт',
		 'day': 16},
		{'day_of_weak': u'Ср',
		 'day': 17},
		{'day_of_weak': u'Чт',
		 'day': 18},
		{'day_of_weak': u'Пт',
		 'day': 19},
		{'day_of_weak': u'Сб',
		 'day': 20},
		{'day_of_weak': u'Нд',
		 'day': 21},
		{'day_of_weak': u'Пн',
		 'day': 22},
		{'day_of_weak': u'Вт',
		 'day': 23},
		{'day_of_weak': u'Ср',
		 'day': 24},
		{'day_of_weak': u'Чт',
		 'day': 25},
		{'day_of_weak': u'Пт',
		 'day': 26},
		{'day_of_weak': u'Сб',
		 'day': 27},
		{'day_of_weak': u'Нд',
		 'day': 28},
		{'day_of_weak': u'Пн',
		 'day': 29},
		{'day_of_weak': u'Вт',
		 'day': 30},
		{'day_of_weak': u'Ср',
		 'day': 31},
	)
	return render(request, 'students/journal_list.html', {'groups': groups, 'students': students, 'journal': journal})