# -*- coding: utf-8 -*-
import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Student

@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
	"""	Writes informarion about newly added or updated studenr info log file """
	logger = logging.getLogger(__name__)
	
	student = kwargs['instance']
	if kwargs['created']:
		logger.info("Student added: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
	else:
		logger.info("Student updated: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
		
@receiver(post_delete, sender=Student)
def log_student_delete_event(sender, **kwargs):
	"""	Writes informarion about newly added or updated studenr info log file """
	logger = logging.getLogger(__name__)
	
	student = kwargs['instance']
	logger.info("Student delete: %s %s (ID: %d)", student.first_name, student.last_name, student.id)