import random
from time import sleep
from celery_tasks.sms.tasks import *

from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework.views import APIView


# /sms_codes/136000000/


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
        send_flag = strict_redis.get('sms_flag_%s' %mobile)
        # print(send_flag)
        if send_flag:
            return Response({'message':'60秒内频繁操作'}, status=400)

        # 1. 生成短信验证码    000333
        sms_code = '%06d' % random.randint(0, 999999)
        print('sms_codes: ', sms_code)

        # 2. 发生短信验证码
        # 参数１：　手机号码
        # 参数２：　【短信号码，　有效时间】
        # 参数３：　使用id为１的云通讯模板
        # CCP().send_template_sms(mobile, [sms_code, 5], 1)
        # sleep(3)

        # 使用celery 异步执行发送短信任务
        send_sms_code.delay(mobile, sms_code)

        #3.保存短信验证码(redis)
        # strict_redis.setex('sms_%s' % mobile, 60*5, 1)
        # strict_redis.setex('sms_flag_%s' % mobile, 60, True)

        # 使用管道发送短信验证码
        pipline = strict_redis.pipeline()
        pipline.setex('sms_%s' % mobile, 60*5, sms_code)
        pipline.setex('sms_flag_%s' % mobile, 60, True)
        result = pipline.execute()

        # print(result)

        return Response({"message":"ok"})
