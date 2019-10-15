from django.db import models

# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length=255, unique=True)
	price = models.IntegerField()
	src = models.CharField(max_length=255, null=True, blank=True)
	src_2 = models.CharField(max_length=255, null=True, blank=True)
	src_3 = models.CharField(max_length=255, null=True, blank=True)
	src_4 = models.CharField(max_length=255, null=True, blank=True)
	src_5 = models.CharField(max_length=255, null=True, blank=True)


	def __str__(self):
		return f'{self.name} at {self.price}' 


class Description(models.Model):
	pass



