# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


from ..models import Exam
#Views for Students

def exam_list(request):
	exam = Exam.objects.all()
	
	# try to order students list
	order_by = request.GET.get('order_by', '')
	if order_by in ('name', 'data_time', 'teacher'):
		exam = exam.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			exam = exam.reverse()
	
	#exam page navigation
	exam_per_page = 3     #exam per page

	#if exam count divided with tail we need to raise our number of pages by 1 for the rest students

	if exam.count()%exam_per_page == 0:
		number_of_pages = exam.count() / exam_per_page 
	else:
		number_of_pages = exam.count() / exam_per_page +1
	

	page = request.GET.get('page') #geting number of page
	pages = range(1,number_of_pages+1) #making a list of pages for navigator
	
	try:
		page = int(page) #trying to exclude wrong value for page number
		if (page <= number_of_pages and page > 0): #making a list of group for page we had. Cheking if page in range of pages.
			exam = exam[0+exam_per_page*(page-1):exam_per_page*page]
		else:
			exam = exam[0+exam_per_page*(number_of_pages-1):exam_per_page*number_of_pages]

	except ValueError: #except value not in range of pages
		exam = exam[0:exam_per_page]
		page = 1
	except TypeError: #except not int in url
		exam = exam[0:exam_per_page]
		page =1
	"""
	# paginate students
	paginator = Paginator(exam, 3)
	page = request.GET.get('page')
	try:
		exam = paginator.page(page)
	except PageNotAnInteger:
		# if page is not an integer, deliver first page
		exam = paginator.page(1)
	except EmptyPage:
		# if page is out of range (e.g. 9999), deliver
		# last page of results.
		exam = paginator.page(paginator.num_pages)
	"""
			
	return render(request, 'students/exam_list.html', {'exam': exam, 'page': page, 'pages': pages})