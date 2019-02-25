# _*_ coding: utf-8 _*_
from celery_tasks.main import celery_app

__author__ = '其实很简单'
__date__ = '19-1-24 上午11:20'


@celery_app.task
def send_email():
    print('邮件发送')