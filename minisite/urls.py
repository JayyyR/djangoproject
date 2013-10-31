from django.conf.urls import patterns, include, url

from expenselogger import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
