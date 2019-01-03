"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import  url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
# from . import views
from views import server_detail,server_list,form,Servers,RunmodAPI,playbookAPI



urlpatterns = [
    url(r'server_list/$', server_list, name='server_list'),
    url(r'server_detail/$', server_detail, name='server_detail'),
    url(r'servers/$', Servers, name='Servers'),
    url(r'form/$', form, name='form'),

    # url(r'^snippets/$', views.ServerList.as_view()),
    # url(r'^snippets/(?P<pk>.+)/$', views.ServerDetail.as_view()),
    # url(r'^post/$', views.Post_test,name='Post_test'),
    url(r'^runmod/$', RunmodAPI, name='RunmodAPI'),
    url(r'^playbook/$', playbookAPI, name='playbookAPI'),
]


urlpatterns = format_suffix_patterns(urlpatterns)