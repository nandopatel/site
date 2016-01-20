from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Basic_Website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$','Webapp.views.base',name='base'),
	url(r'booking.html','Webapp.views.booking',name='booking'),
	url(r'gallery.html','Webapp.views.gallery',name='gallery'),
	url(r'currency','Webapp.views.currency',name='currency'),
    url(r'^admin/', include(admin.site.urls)),
)
