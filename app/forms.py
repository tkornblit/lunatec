from django import forms
from app.models import *
from datetime import *
from django.forms.extras.widgets import *
from django.forms.widgets import *
from django.contrib.localflavor.us.forms import USPhoneNumberField
from django.forms import ModelForm
from django.contrib.admin import widgets
from django.forms.models import inlineformset_factory
from django.core.mail import send_mail,EmailMessage,get_connection
from django.template.loader import render_to_string
from django.contrib.auth.hashers import (check_password, make_password, is_password_usable, UNUSABLE_PASSWORD)


def ContactFormFactory(exclude_list=[],placeholder=False,*args,**kwargs):

	class ContactForm(ModelForm):
		def __init__(self,*args,**kwargs):
			super(ContactForm,self).__init__(*args,**kwargs)
			if 'product' in self.fields:
				self.fields['product'].choices= self.product_choices()

			if placeholder:
				for name,field in self.fields.items():
					label = name.replace("_"," ").title()
					field.widget.attrs['placeholder'] = label

		def save(self):
			super(ContactForm,self).save()
			self.send_email()

		def send_email(self):
			from_email = "tkornblit@tkornblit.com"
			to = [self.instance.email]
			subject = "LunaTec Contact Inquiry"
			body = render_to_string('emails/contact.html',{'contact' : self.instance})
	#		connection = get_connection(username="noreply@bookyourlooknyc.com",password="laramie",fail_silently=False)
	#		email = EmailMessage(subject,body,from_email,to,connection=connection)
			email = EmailMessage(subject,body,from_email,to)
			email.content_subtype = "html"
			email.send()

		def product_choices(self):
			categories = []
			for category in Category.objects.all():
				products = [(product.id,product.name) for product in category.products.all()]
				new_category = (category.name,products)
				categories.append(new_category)
			return categories
			
		class Meta:
			model = Contact
			exclude = exclude_list
			widgets = {
				"first_name" : TextInput(attrs={"data-bind" : "value: first_name" }) ,
				"last_name" : TextInput(attrs={"data-bind" : "value: last_name" }) ,
				"product" : Select(attrs={"data-bind": "value:product", "dir" : "rtl" }) ,
				"email" : TextInput(attrs={"data-bind" : "value : email"}) ,
				"phone" : TextInput(attrs={"data-bind" : "value : phone"}) ,
				"message" : Textarea(attrs={'cols': 30, 'rows': 3,"data-bind" : "value:message"})
			}

	return ContactForm

