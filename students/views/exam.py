# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from ..utils import paginate, get_current_group
from ..models import Exam
#Views for Students

def exam_list(request):
	group = get_current_group(request)

	if group:
		exam = Exam.objects.filter(group = group)
	else:
		exam = Exam.objects.all()

	# try to order group list
	order_by = request.GET.get('order_by', '')
	if order_by in ('name', 'data_time', 'teacher'):
		exam = exam.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			exam = exam.reverse()
			
	context = paginate(exam, 3, request, {}, var_name = 'exam')
	
	return render(request, 'students/exam_list.html', context)