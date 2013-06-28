#!/usr/bin/python


import sys
sys.path.append('/dat/projects/lunatec/lunatec')

import codecs
import settings
from django.core.management import setup_environ
setup_environ(settings)
from app.models import *

f = codecs.open("files/lunatec.tsv","r",encoding="utf-8")

map = {}


for n,line in enumerate(f.readlines()):
	if n == 0:
		continue
	if len(line) > 6:
		l = line.strip("\n").split("\t")
		category= l[0]
		sub = l[1]
		belt = l[2]
		short_description = l[3]
		long_description = l[4]
		image = "images/belts/"+str(l[5].replace(" ","_").lower())+".jpg"

		if Category.objects.filter(name=category):
			cat = Category.objects.get(name=category)
		else:
			cat = Category.objects.create(name=category)

		if SubCategory.objects.filter(name=sub):
			sub = SubCategory.objects.get(name=sub)
		else:
			sub = SubCategory.objects.create(name=sub,category=cat)

		Product.objects.create(name=belt,category=cat,sub_category=sub,short_description=short_description,long_description=long_description,image=image)


		

		


