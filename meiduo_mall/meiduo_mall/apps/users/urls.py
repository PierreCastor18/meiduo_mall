# _*_ coding: utf-8 _*_
from django.conf.urls import url

from meiduo_mall.apps.users import views

__author__ = '其实很简单'
__date__ = '19-1-16 下午1:39'


urlpatterns =[
    # url(r'^test/$', views.test),
    #　获取用户名数量
    url(r'^usernames/(?P<username>\w{5,20})/count/$', views.UserNameCountView.as_view()),
    # 获取手机号数量
    url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
    # 注册用户
    url(r'^users/$', views.UserView.as_view()),
]