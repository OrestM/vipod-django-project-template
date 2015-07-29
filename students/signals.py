# -*- coding: utf-8 -*-
import logging

from django.core.signals import request_started
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Student, Group, Exam

@receiver(request_started)
def my_callback(sender, **kwargs):
	print("request_started")
		
@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
	"""	Writes information about newly added or updated student info log file """
	logger = logging.getLogger(__name__)
	
	student = kwargs['instance']
	if kwargs['created']:
		logger.info("Student added: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
	else:
		logger.info("Student updated: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
		
@receiver(post_delete, sender=Student)
def log_student_delete_event(sender, **kwargs):
	"""	Writes information about newly delete student info log file """
	logger = logging.getLogger(__name__)
	
	student = kwargs['instance']
	logger.info("Student delete: %s %s (ID: %d)", student.first_name, student.last_name, student.id)

@receiver(post_save, sender=Group)
def log_group_updated_added_event(sender, **kwargs):
	"""	Writes information about newly added or updated group info log file """
	logger = logging.getLogger(__name__)
	
	group = kwargs['instance']
	if kwargs['created']:
		logger.info("Group added: %s %s (ID: %d)", group.title, group.leader, group.id)
	else:
		logger.info("Group updated: %s %s (ID: %d)", group.title, group.leader, group.id)
		
@receiver(post_delete, sender=Group)
def log_group_delete_event(sender, **kwargs):
	"""	Writes information about newly delete group info log file """
	logger = logging.getLogger(__name__)
	
	group = kwargs['instance']
	logger.info("Group delete: %s %s (ID: %d)", group.title, group.leader, group.id)
	
@receiver(post_save, sender=Exam)
def log_exam_updated_added_event(sender, **kwargs):
	"""	Writes information about newly added or updated exam info log file """
	logger = logging.getLogger(__name__)
	
	exam = kwargs['instance']
	if kwargs['created']:
		logger.info("Exam added: %s %s %s (ID: %d)", exam.name, exam.teacher, exam.group, exam.id)
	else:
		logger.info("Exam updated: %s %s %s (ID: %d)", exam.name, exam.teacher, exam.group, exam.id)
		
@receiver(post_delete, sender=Exam)
def log_exam_delete_event(sender, **kwargs):
	"""	Writes information about newly delete exam info log file """
	logger = logging.getLogger(__name__)
	
	exam = kwargs['instance']
	logger.info("Exam delete: %s %s %s (ID: %d)", exam.name, exam.teacher, exam.group, exam.id)