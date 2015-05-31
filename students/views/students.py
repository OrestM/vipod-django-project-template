# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


from ..models import Student
#Views for Students

def students_list(request):
	students = Student.objects.all()
	
	# try to order students list
	order_by = request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()
	
	#student page navigation
	student_per_page = 3     #students per page

	#if students count divided with tail we need to raise our number of pages by 1 for the rest students

	if students.count()%student_per_page == 0:
		number_of_pages = students.count() / student_per_page 
	else:
		number_of_pages = students.count() / student_per_page +1
	

	page = request.GET.get('page') #geting number of page
	pages = range(1,number_of_pages+1) #making a list of pages for navigator
	
	try:
		page = int(page) #trying to exclude wrong value for page number
		if (page <= number_of_pages and page > 0): #making a list of student for page we had. Cheking if page in range of pages.
			students = students[0+student_per_page*(page-1):student_per_page*page]
		else:
			students = students[0+student_per_page*(number_of_pages-1):student_per_page*number_of_pages]

	except ValueError: #except value not in range of pages
		students = students[0:student_per_page]
		page = 1
	except TypeError: #except not int in url
		students = students[0:student_per_page]
		page =1

	"""
	#paginate students with paginator
	paginator = Paginator(students, 3)
	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		students = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver
	# last page of results.
		students = paginator.page(paginator.num_pages)
	"""
	return render(request, 'students/students_list.html', {'students':students, 'page':page, 'pages':pages})
	
def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')
	
def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)
	
def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)