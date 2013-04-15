from django.conf.urls import patterns, include, url
from contentSubmit import views
from userHandling import views as user_views
from lists import views as list_views
from miscPages import views as misc_views
from clickTracker import views as click_tracker
from django.contrib.auth.views import login
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^submit/$', views.contentSubmit),
	(r'^signup/$', user_views.signup),
	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^$', list_views.latest),
    (r'^label_search/$', list_views.filterByLabel),
    (r'^category/$', list_views.category),
    (r'^my_posts/$', views.manageContent),
    (r'^ct/$', click_tracker.clickTracker),
    (r'^impressum/$', misc_views.imprint),
    (r'^datenschutz/$', misc_views.privacyPolicy),
    (r'^agb/$', misc_views.AGB),

    # Examples:
    # url(r'^$', 'VideoSoup.views.home', name='home'),
    # url(r'^VideoSoup/', include('VideoSoup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^VideoSoup/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

'''
if not settings.PRODUCTION:
   urlpatterns += staticfiles_urlpatterns()
'''