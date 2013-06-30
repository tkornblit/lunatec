from django.db import models
from django.template.defaultfilters import slugify
from random import randrange


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

	def image(self):
		products = self.products.all()
		if products.count() == 0:
			return None
		else:
			index = randrange(0,products.count())
			product = products[index]
			return product.image

class SubCategory(models.Model):
	category = models.ForeignKey("Category",related_name="subcategories")
	name = models.CharField(max_length=50)
	description = models.TextField(null=True,blank=True)
	def __unicode__(self):
		return "%s" % (self.name)

	def image(self):
		products = self.products.all()
		if products.count() == 0:
			return None
		else:
			index = randrange(0,products.count())
			product = products[index]
			return product.image
		

class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	product = models.ForeignKey("Product",null=True,blank=True)
	email = models.EmailField(max_length=75)
	phone = models.CharField(max_length=75,null=True,blank=True)
	message = models.TextField()

