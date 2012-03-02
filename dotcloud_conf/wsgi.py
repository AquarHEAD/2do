import os
import sys
sys.path.append('/home/dotcloud/current')
sys.path.append('/home/dotcloud/current/yakusoku')
os.environ['DJANGO_SETTINGS_MODULE'] = 'yakusoku.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
