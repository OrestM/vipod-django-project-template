# -*- coding: utf-8 -*-
from django.contrib import admin
from models.students import Student
from models.groups import Group
from models.journal import Journal
from models.exam import Exam

from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

def make_copy(modeladmin, request, queryset):
	for query in queryset:
		# add fields which neeed to save
		type_query = Student(last_name = obj.last_name, first_name = obj.first_name, middle_name = obj.middle_name,
			birthday = obj.birthday, photo = obj.photo, ticket = obj.ticket, student_group = obj.student_group,
			notes = obj.notes)
        # method save
		type_query.save()
make_copy.short_description = u"Скопіювати обраного студента"

class StudentFormAdmin(ModelForm):
	def clean_student_group(self):
		""" Check if student is leader in any group 
		
		If yes, then ensure it's the same as selected group. """
		# get group where current student is a leader
		groups = Group.objects.filter(leader=self.instance)
		if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
			raise ValidationError(u'Студент є старостою іншої групи.', code='invalid')
		return self.cleaned_data['student_group']

class StudentAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name', 'ticket', 'student_group']
	list_display_links = ['last_name', 'first_name']
	list_editable = ['student_group']
	ordering = ['last_name']
	list_filter = ['student_group']
	list_per_page = 10
	search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']
	form = StudentFormAdmin
	# add our function
	actions = [make_copy]
		
	def view_on_site(self, obj):
		return reverse('students_edit', kwargs={'pk': obj.id})
		
class GroupAdmin(admin.ModelAdmin):
	list_display = ['title', 'leader', 'notes']
	list_display_links = ['title']
	list_editable = ['leader']
	ordering = ['title']
	list_filter = ['leader']
	list_per_page = 10	
	search_fields = ['title', 'leader', 'notes']
	
	def view_on_site(self, obj):
		return reverse('groups_edit', kwargs={obj.id})
	
		
# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Journal)
admin.site.register(Exam)