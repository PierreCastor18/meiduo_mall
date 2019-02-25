# _*_ coding: utf-8 _*_
from time import sleep

from celery_tasks.main import celery_app

__author__ = '其实很简单'
__date__ = '19-1-24 上午11:20'


# 通过装饰器把函数变为celery任务
@celery_app.task
def send_sms_code(mobile, sms_code):
    # 参数１：　手机号码
    # 参数２：　【短信号码，　有效时间】
    # 参数３：　使用id为１的云通讯模板
    # CCP().send_template_sms(mobile, [sms_code, 5], 1)
    print('发生送短信验证码: %s %s' %(mobile, sms_code))
    sleep(3)