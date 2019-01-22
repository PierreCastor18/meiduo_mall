import random

from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework.views import APIView


# /sms_codes/136000000/
from meiduo_mall.libs.yuntongxun.sms import CCP


class SMSCode(APIView):

    def get(self, request, mobile):
        """
        获取短信验证码
        :param request:
        :param mobile:
        :return:

            1. 生成短信验证码
            2. 发生短信验证码
            3. 保存短信验证码(redis)
            4. 判断验证码６０秒内是否过期
        """
        strict_redis = get_redis_connection('sms_codes')  # type: StrictRedis

        # 4. 判断验证码６０秒内是否过期
        send = strict_redis.get('sms_flag_%s' %mobile)
        if send:
            return Response({'message':'60秒内频繁操作'})

        # 1. 生成短信验证码    000333
        sms_code = '%06d' % random.randint(0, 999999)

        # 2. 发生短信验证码
        # 参数１：　手机号码
        # 参数２：　【短信号码，　有效时间】
        # 参数３：　使用id为１的云通讯模板
        # CCP().send_template_sms(mobile, [sms_code, 5], 1)

        #3.保存短信验证码(redis)
        strict_redis.setex('sms_%s' % mobile, 60*5, 1)
        strict_redis.setex('sms_flag_%s' % mobile, 60, True)

        return Response({"message":"ok"})
