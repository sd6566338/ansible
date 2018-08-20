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
# from cmdb.views import statement, List_all,Get_sn,server_list##Django1.10
from . import views



urlpatterns = [
    # url(r'^getsn/$', Get_sn, name='Get_sn' ),
    # url(r'^statement/$', statement, name='statement'), ##Django1.10
    # url(r'^sn/$', List_all, name='List_all'), ##Django1.10
    # url(r'server_list/$', server_list, name='server_list'), ##Django1.10
    url(r'^snippets/$', views.ServerList.as_view()),
    url(r'^snippets/(?P<pk>.+)/$', views.ServerDetail.as_view()),
    url('^remark/(?P<cmdb_remark>.+)/$', views.RemarkList.as_view()),
    url(r'^post/$', views.Post_test,name='Post_test'),
    url(r'^runmod/$', views.RunmodAPI, name='RunmodAPI'),
    url(r'^playbook/$', views.playbookAPI, name='playbookAPI'),

    # url(r'^$', views.api_root),
    # url(r'^snippets/$',
    #     views.ServerList.as_view(),
    #     name='server-list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$',
    #     views.ServerDetail.as_view(),
    #     name='server-detail')
    # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
    #     views.SnippetHighlight.as_view(),
    #     name='snippet-highlight'),
    # url(r'^users/$',
    #     views.UserList.as_view(),
    #     name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$',
    #     views.UserDetail.as_view(),
    #     name='user-detail')
]


urlpatterns = format_suffix_patterns(urlpatterns)