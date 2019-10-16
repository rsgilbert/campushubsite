from django.db import models

# Create your models here.

class SearchHistory(models.Model):
	seachword = models.CharField(max_length=255)
	time = models.DateTimeField(auto_now=True)


	def __str__(self):
		return f'{ self.seachword } on { self.time.date() }'

