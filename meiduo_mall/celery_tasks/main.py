# _*_ coding: utf-8 _*_
import os

from celery import Celery

__author__ = '其实很简单'
__date__ = '19-1-24 上午11:30'

# 指定setting文件　celery 工作进程会使用
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.dev")

# celery 应用
celery_app = Celery('meiduo', broker='redis://127.0.0.1:6379/14')
# celery_app.config_from_object('celery_tasks.config')

# 添加扫描任务函数
celery_app.autodiscover_tasks(['celery_tasks.sms', 'celery_tasks.email'])


