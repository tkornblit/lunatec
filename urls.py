from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'app.views.home', name='home'),
	url(r'^products/$', 'app.views.products', name='products'),
	url(r'^products/(?P<category>[0-9]+)/$', 'app.views.category', name='category'),
	url(r'^products/(?P<category>[0-9]+)/(?P<subcategory>[0-9]+)/$', 'app.views.subcategory', name='subcategory'),
	url(r'^products/(?P<category>[0-9]+)/(?P<subcategory>[0-9]+)/(?P<product>[0-9]+)/$', 'app.views.product', name='product'),
	url(r'^about/$', 'app.views.about', name='about'),
	url(r'^contact/$', 'app.views.contact', name='contact'),


	#ajax
	url(r'^ajax/contact/','app.ajax.contact',name='ajax_contact'),


	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
   (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT, 'show_indexes' : True}),
   (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_ROOT, 'show_indexes' : True}),
)   

urlpatterns += staticfiles_urlpatterns()

