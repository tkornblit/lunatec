from django.db import models
from django.template.defaultfilters import slugify


class Product(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey("Category",related_name="products")
	sub_category = models.ForeignKey("SubCategory",related_name="products")
	short_description = models.CharField(max_length=100,null=True,blank=True)
	long_description = models.TextField(null=True,blank=True)
	image = models.ImageField(upload_to='images/belts/')
	def __unicode__(self):
		return "%s" % (self.name)

class Category(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(null=True,blank=True)
	image = models.ImageField(upload_to='images/categories/')
	def __unicode__(self):
		return "%s" % (self.name)

class SubCategory(models.Model):
	category = models.ForeignKey("Category",related_name="subcategories")
	name = models.CharField(max_length=50)
	description = models.TextField(null=True,blank=True)
	def __unicode__(self):
		return "%s" % (self.name)

class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	product = models.ForeignKey("Product",null=True,blank=True)
	email = models.EmailField(max_length=75)
	phone = models.CharField(max_length=75)
	notes = models.TextField()

