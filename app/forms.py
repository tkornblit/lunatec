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


class ContactForm(ModelForm):
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

	class Meta:
		model = Contact
		exclude = ('product','phone')
		widgets = {
			"first_name" : TextInput(attrs={"placeholder" : "First Name", "data-bind" : "value: first_name" }) ,
			"last_name" : TextInput(attrs={"placeholder" : "Last Name", "data-bind" : "value: last_name" }) ,
			"email" : TextInput(attrs={"placeholder" : "E-mail", "data-bind" : "value : email"}) ,
			"notes" : Textarea(attrs={'cols': 30, 'rows': 3, "placeholder" : "Message", "data-bind" : "value:notes"})
		}
