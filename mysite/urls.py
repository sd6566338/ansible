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
from django.conf.urls import include, url
from django.contrib import admin
#from cmdb import views as cmdb_views ##Django1.8
#from cmdb.views import statement, List_all,Get_sn ##Django1.10


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cmdb/', include('cmdb.urls')),
#    url(r'^$', 'cmdb.views.index', name='home'),  ##Django1.8

#    url(r'^$', cmdb_views.home, name='home'),
#    url(r'map/', cmdb_views.map, name='map'),
]
