from django.conf.urls import patterns, include, url
from contentSubmit import views
from userHandling import views as user_views
from django.contrib.auth.views import login
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^submit/$', views.contentSubmit),
	(r'^signup/$', user_views.signup),
	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^$', views.frontPage),
    (r'^my_posts/$', views.manageContent),
	

    # Examples:
    # url(r'^$', 'VideoSoup.views.home', name='home'),
    # url(r'^VideoSoup/', include('VideoSoup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
