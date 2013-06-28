from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext, render
from datetime import date,datetime,timedelta
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from models import *
from forms import *

def home(request):
	results = {}
	results['contact_form'] = ContactForm()
	
	return render_to_response('index.html',results ,context_instance=RequestContext(request))
	
def about(request):
	results = {}
	return render_to_response('about.html',results ,context_instance=RequestContext(request))

def contact(request):
	results = {}
	return render_to_response('contact.html',results ,context_instance=RequestContext(request))

def products(request):
	results = {}
	return render_to_response('products.html',results ,context_instance=RequestContext(request))

def category(request,category):
	results = {}
	results['category'] = get_object_or_404(Category,pk=category)
	return render_to_response('category.html',results ,context_instance=RequestContext(request))

def subcategory(request,category,subcategory):
	results = {}
	results['category'] = get_object_or_404(Category,pk=category)
	results['subcategory'] = get_object_or_404(SubCategory,pk=subcategory)
	return render_to_response('subcategory.html',results ,context_instance=RequestContext(request))

def product(request,category,subcategory,product):
	results = {}
	results['category'] = get_object_or_404(Category,pk=category)
	results['subcategory'] = get_object_or_404(SubCategory,pk=subcategory)
	results['product'] = get_object_or_404(Product,pk=product)
	return render_to_response('product.html',results ,context_instance=RequestContext(request))
