from django.conf.urls.defaults import patterns, include, url
import settings

urlpatterns = patterns('',
    url(r'^m/signup', 'yakusoku.members.views.signup'),
    url(r'^m/login', 'yakusoku.members.views.login'),
    url(r'^t/add', 'yakusoku.todos.views.add'),
    url(r'^t/done/(?P<tid>\d+)$', 'yakusoku.todos.views.done'),
    url(r'^t/remove/(?P<tid>\d+)$', 'yakusoku.todos.views.remove'),
    url(r'^(?P<slug>\w+)$', 'yakusoku.todos.views.handler'),
    url(r'^$', 'yakusoku.todos.views.handler'),
    url(r'^s/(?P<path>.*)$', 'django.views.static.serve', {
           'document_root': settings.STATIC_ROOT,
       }),
)
