"""MyPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from cmdb import views
from . import testdb,phonedb

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^index/',views.index),
    url(r'^404/',views.errpage),
    url(r'^account/', views.account),
    url(r'^phone/', views.phone),
    url(r'^commonurl/', views.urlpage),
    url(r'^data_add',testdb.data_add),
    url(r'^data_get',testdb.data_get),
    url(r'^account_data_all_del',testdb.data_all_del),
    url(r'^phone_data_all_del',phonedb.data_all_del),
]
