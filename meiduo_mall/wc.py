# _*_ coding: utf-8 _*_
__author__ = '其实很简单'
__date__ = '19-1-29 下午8:53'


# 类装饰器
class logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('[INFO]: the function {func}() is running...'.format(func=self.func.__name__))
        return self.func(*args, **kwargs)


@logger     #调用装饰器
def say(something):
    print('say {}!'.format(something))
say('hello')


