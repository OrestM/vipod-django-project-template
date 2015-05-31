# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


from ..models import Group	

#Views for Groups	
def groups_list(request):
	groups = Group.objects.all()
	
	# try to order groups list
	order_by = request.GET.get('order_by', '')
	if order_by in ('title', 'leader'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()
	
	#groups page navigation
	group_per_page = 3     #groups per page

	#if groups count divided with tail we need to raise our number of pages by 1 for the rest students

	if groups.count()%group_per_page == 0:
		number_of_pages = groups.count() / group_per_page 
	else:
		number_of_pages = groups.count() / group_per_page +1
	

	page = request.GET.get('page') #geting number of page
	pages = range(1,number_of_pages+1) #making a list of pages for navigator
	
	try:
		page = int(page) #trying to exclude wrong value for page number
		if (page <= number_of_pages and page > 0): #making a list of group for page we had. Cheking if page in range of pages.
			groups = groups[0+group_per_page*(page-1):group_per_page*page]
		else:
			groups = groups[0+group_per_page*(number_of_pages-1):group_per_page*number_of_pages]

	except ValueError: #except value not in range of pages
		groups = groups[0:group_per_page]
		page = 1
	except TypeError: #except not int in url
		groups = groups[0:group_per_page]
		page =1
	"""
	# paginate groups
	paginator = Paginator(groups, 3)
	page = request.GET.get('page')
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
		# if page is not an integer, deliver first page
		groups = paginator.page(1)
	except EmptyPage:
		# if page is out of range (e.g. 9999), deliver
		# last page of results.
		groups = paginator.page(paginator.num_pages)
	"""
	return render(request, 'students/groups_list.html', {'groups': groups, 'page':page, 'pages':pages})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
	
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)
	
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)