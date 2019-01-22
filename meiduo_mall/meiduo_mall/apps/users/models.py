from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """用户表"""
    mobiles = models.CharField(max_length=11, verbose_name='电话号码')

    class Meta:
        db_table = 'tb_user'    # 指定表
        verbose_name = '用户'     # 后台中文显示
        verbose_name_plural = verbose_name
