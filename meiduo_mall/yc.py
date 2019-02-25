# _*_ coding: utf-8 _*_
__author__ = '其实很简单'
__date__ = '19-1-29 下午8:53'


# 类装饰器
class logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):   # 接收函数

        def wrapper(*args, **kwargs):
            print('[{level}]: the function {func}() is running...'.format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        # 返回函数
        return wrapper


@logger(level='WARNING')
def say(something):
    print('say {}!'.format(something))

say('hello')


