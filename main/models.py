from django.db import models

# Create your models here.
class Todo(models.Model):
	""" Defines a basic todo element """
	title = models.CharField(max_length=250)
	status = models.BooleanField(default=False)

	def __str__(self):
		""" Provide a default toString """
		return self.title