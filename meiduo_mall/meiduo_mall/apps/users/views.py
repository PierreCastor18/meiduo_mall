from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

# 测试视图
# def test(request):
#     return render(request, '../../../../front_end_pc/test.html')

# 判断用户是否已经有人注册过的
from users import serializers
from users.models import User


# 判断用户名是否重复
class UserNameCountView(APIView):
    '''
    用户名数量
    '''
    def get(self, request, username):
        # 获取指定用户名数量
        count = User.objects.filter(username=username).count()

        data = {
            'username':username,
            'count':count,
        }

        # 返回数据
        return Response(data)

# 检查手机号是否正确
class MobileCountView(APIView):
    '''
    手机号数量
    '''
    def get(self, request, mobile):
        count = User.objects.filter(mobile=mobile).count()

        data = {
            'mobile':mobile,
            'count':count,
        }

        return Response(data)


# 注册用户
class UserView(CreateAPIView):
    '''
    用户注册
    传入所有参数
    '''
    serializer_class = serializers.CreateUserSerializer