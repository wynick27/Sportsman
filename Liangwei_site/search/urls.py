__author__ = 'guoliangwei'
#from django.conf.urls import url
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
    # url(r'^search_result',views.search_result, name='search_result')
]