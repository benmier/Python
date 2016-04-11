from __future__ import unicode_literals

from django.db import models

class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQueryset(self.model, using=self._db)
	def active(self):
		return self.get_queryset().active()
	def featured(self):
		return self.get_queryset().featured()

class ProductQueryset(models.query.QuerySet):
	def active(self): # have each function return a QuerySet
		return self.filter(is_active=True)
	def featured(self): # have each function return a QuerySet
		return self.filter(is_featured=True)

class Product(models.Model): 
	name = models.CharField(max_length=60)
	description = models.TextField()
	is_active = models.BooleanField(default=False)
	is_featured = models.BooleanField(default=False)
	created_at = models.DateTimeField()
	objects = ProductManager()
	def __str__(self):
		return self.name
