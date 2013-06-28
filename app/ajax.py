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
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson as json

@csrf_exempt
def contact(request):
	form = ContactForm(request.POST)
	if form.is_valid():
		form.save()
		return HttpResponse(json.dumps({'success':True}), mimetype="application/json")
	else:
		errors = [{"field":k,"value":v[0]} for k,v in form.errors.items()]
		return HttpResponse(json.dumps({'success': False, 'errors' : errors}), mimetype="application/json")

