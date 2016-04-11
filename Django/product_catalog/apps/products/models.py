from __future__ import unicode_literals
from django.db import models

class Product(models.Model):
	manufacturer = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	date_added = models.DateField()
	description = models.TextField()