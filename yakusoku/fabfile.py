from __future__ import with_statement
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def add(app_name):
    local('./manage.py startapp %s' % app_name)

def db():
    local('./manage.py syncdb')

def server():
    local('./manage.py runserver')

def shell():
    local('./manage.py shell')