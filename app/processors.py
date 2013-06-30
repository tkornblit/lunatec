from django.http import HttpResponse
from django.template import RequestContext
from forms import *
from models import *

def globalz(request):
	return {
				'ip_address': request.META['REMOTE_ADDR'],
				'contact_form' : ContactFormFactory(placeholder=True,exclude_list=['product','phone']),
				'categories' : Category.objects.all(),
				'features_products' : Product.objects.all()[:2]	
		 	 }

