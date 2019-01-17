# _*_ coding: utf-8 _*_
from django.conf.urls import url

from meiduo_mall.apps.users import views

__author__ = '其实很简单'
__date__ = '19-1-16 下午1:39'


urlpatterns =[
    url(r'^test/$', views.test),
]