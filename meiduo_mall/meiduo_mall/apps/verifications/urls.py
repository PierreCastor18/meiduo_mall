# _*_ coding: utf-8 _*_
from django.conf.urls import url

from verifications import views

__author__ = '其实很简单'
__date__ = '19-1-17 下午4:45'

urlpatterns = [
    #　短信验证码
    url(r'^sms_codes/(?P<mobile>1[3-9]\d{9})/$', views.SMSCode.as_view()),
]