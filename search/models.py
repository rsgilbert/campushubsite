from django.db import models

# Create your models here.

class SearchHistory(models.Model):
	seachword = models.CharField(max_length=255)

	def __str__(self):
		return self.seachword
