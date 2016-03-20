from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registration(models.Model):
	user_kind=(
		('Student','Student'),
		('Teacher','Teacher')
	)
	email = models.EmailField()
	full_name = models.CharField(max_length=30)
	user_type = models.CharField(max_length=7,
                                      choices=user_kind,
                                      default='Student')
	create_time = models.DateTimeField(auto_now=False,	auto_now_add=True)
	is_validated = models.BooleanField()
	update_time = models.DateTimeField(auto_now=True,	auto_now_add=False)
	def __unicode__(self):
		return self.email
