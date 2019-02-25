# _*_ coding: utf-8 _*_
import re

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User

__author__ = '其实很简单'
__date__ = '19-2-24 下午2:59'


# 注册用户所需要的序列化器
class CreateUserSerializer(ModelSerializer):
    '''
    要校验的属性
    要返回的属性
    '''
    # 新增的属性(要校验的属性)
    password2 = serializers.CharField(label='确认密码', write_only=True)
    sms_code = serializers.CharField(label='短信验证码', max_length=6, write_only=True)
    allow = serializers.BooleanField(label='同意协议', write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'sms_code', 'mobile', 'allow')

        extra_kwargs = {
            'username':{
                'min_length':5,
                'max_length':20,
                'error_messages':{
                    'min_length':'仅允许5-20个字符的用户名',
                    'max_length':'仅允许5-20个字符的用户名'
                }
            },
            'password':{
                'write_only':True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许8-20个字符的用户名',
                    'max_length': '仅允许8-20个字符的用户名'
                }
            }
        }

    # 验证手机号
    def validate_mobile(self, value):
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号格式错误')
        return value

    # 检验用户是否同意协议
    def validate_allow(self, value):
        if not value:
            raise serializers.ValidationError('请同意用户协议')
        return value

    # 判断密码，短信验证码
    def validate(self, attrs):
        # 判断密码是否一致
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('两次密码不一致')

        # 判断短信验证码
        # 获取redis数据库中的验证码
        from django_redis import get_redis_connection
        redis_conn = get_redis_connection('sms_codes')
        mobile = attrs['mobile']
        #正确的短信验证码
        real_sms_code = redis_conn.get('sms_%s' % mobile)   # bytes
        sms_code = attrs.get('sms_code')

        print('real_sms_code: ', real_sms_code.decode())
        print('sms_code: ', sms_code)
        print('mobile: ', mobile)

        if real_sms_code is None:
            raise serializers.ValidationError('无法获取短信验证码')

        # 用户输入的短信验证码

        if sms_code != real_sms_code.decode():
            raise serializers.ValidationError('短信验证码错误')

        return attrs

    # 新增一个用户 // 可能会报错
    # Django的认证系统会加密密码
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            mobile=validated_data.get('mobile'),
        )
        return user

