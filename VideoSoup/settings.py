# Django settings for VideoSoup project.

'''
Release 0.1
'''


import os
import psycopg2
from urlparse import urlparse
from os import environ
import storages
import boto

PRODUCTION = True
DEBUG = False

ADMINS = (
    ('Carl Bednorz', 'carl.bednorz@gmail.com'),
)

MANAGERS = ADMINS

#Development Settings
if PRODUCTION == False:
   
    TEMPLATE_DEBUG = DEBUG

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    print PROJECT_ROOT

    PROJECT_DIR = PROJECT_ROOT

    print PROJECT_DIR

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',#'django.db.backends.sqlite3', #'postgresql_psycopg2' # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'videosoup',                      # Or path to database file if using sqlite3. 
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # In a Windows environment this must be set to your system time zone.
    TIME_ZONE = 'Europe/Berlin'

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'de-DE'

    SITE_ID = 1

    ALLOWED_HOSTS = ['*']

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/media/"
    MEDIA_ROOT = ''

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    MEDIA_URL = ''

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    #STATIC_ROOT = '/Users/cb1754/Documents/Projects/VideoSoup/VideoSoup/static/'
    STATIC_ROOT = os.path.join(PROJECT_ROOT,'static/')
    print STATIC_ROOT


    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = '/static/'

    print os.path.join(PROJECT_DIR,'static_stuff')
    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        #"/Users/cb1754/Documents/Projects/VideoSoup/VideoSoup/static_stuff",
        os.path.join(PROJECT_DIR,'static_stuff'),
        #os.path.join(PROJECT_DIR,'static_stuff/'),
        #"/VideoSoup/static_stuff/",
        #"/static_stuff/",
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = '!kifa*ar%_o5vd3d*cr*arx0j28pe%saz9nkcqof=w*@a69#m%'

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'VideoSoup.urls'

    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = 'VideoSoup.wsgi.application'

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(os.path.dirname(__file__), 'templates')
    )

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'contentSubmit',
        'userHandling', 
        'lists',
        'clickTracker',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
    )

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.static',
        'django.contrib.messages.context_processors.messages',
    )



if PRODUCTION:
    
    TEMPLATE_DEBUG = DEBUG
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    print PROJECT_ROOT

    PROJECT_DIR = PROJECT_ROOT

    print PROJECT_DIR

    
    if environ.has_key('DATABASE_URL'):
        url = urlparse(environ['DATABASE_URL'])
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',#'django.db.backends.sqlite3', #'postgresql_psycopg2' # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': url.path[1:],                      # Or path to database file if using sqlite3. 
                'USER': url.username,                      # Not used with sqlite3.
                'PASSWORD': url.password,                  # Not used with sqlite3.
                'HOST': url.hostname,                      # Set to empty string for localhost. Not used with sqlite3.
                'PORT': url.port,                      # Set to empty string for default. Not used with sqlite3.
            }
        }
    

    '''
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',#'django.db.backends.sqlite3', #'postgresql_psycopg2' # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'videosoup',                      # Or path to database file if using sqlite3. 
                'USER': '',                      # Not used with sqlite3.
                'PASSWORD': '',                  # Not used with sqlite3.
                'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
                'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
            }
        }
    '''

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # In a Windows environment this must be set to your system time zone.
    TIME_ZONE = 'Europe/Berlin'

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'de-DE'

    SITE_ID = 1

    ALLOWED_HOSTS = ['*']

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/media/"
    MEDIA_ROOT = ''

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    MEDIA_URL = ''

    #Amazon S3 Storage Stuff
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
    AWS_PRELOAD_METADATA = True
    

    
    

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    #STATIC_ROOT = '/Users/cb1754/Documents/Projects/VideoSoup/VideoSoup/static/'
    #STATIC_ROOT = os.path.join(os.getcwd(), "VideoSoup/static")
    


    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = "https://s3.amazonaws.com/videosoup-assets/static/"
    #STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3-website-us-east-1.amazonaws.com/static/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    
    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        #"/Users/cb1754/Documents/Projects/VideoSoup/VideoSoup/static_stuff",
        os.path.abspath(__file__)+'/..'+'/static_stuff',
        #os.path.join(PROJECT_DIR,'static_stuff'),
        #os.path.join(PROJECT_DIR,'static_stuff/'),
        #"/VideoSoup/static_stuff/",
        #"/static_stuff/",
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = os.environ.get('SECRET_DJANGO_KEY')
    

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'VideoSoup.urls'

    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = 'VideoSoup.wsgi.application'

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(os.path.dirname(__file__), 'templates')
    )

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'contentSubmit',
        'userHandling', 
        'lists',
        'clickTracker',
        'storages',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
    )

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.static',
        'django.contrib.messages.context_processors.messages',
    )


    
    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
