from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Basic_Website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$|Index.html','Webapp.views.index',name='base'),
	url(r'Booking.html','Webapp.views.booking',name='booking'),
	url(r'Gallery.html','Webapp.views.gallery',name='gallery'),
	url(r'Currency.html','Webapp.views.currency',name='currency'),
	url(r'rpg.html','Webapp.views.textgen',name='textgen'),
	url(r'formulas.html','Webapp.views.formulas',name='formulas'),
	url(r'test','Webapp.views.get_name',name='get_name'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
)
