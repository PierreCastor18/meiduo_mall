# _*_ coding: utf-8 _*_
__author__ = '其实很简单'
__date__ = '19-1-29 下午9:34'


#　函数装饰器
def logger(func):
    def wrapper(*args, **kwargs):
        print('我开始计算: {}函数了'.format(func.__name__))
        func(*args, **kwargs)
        print('我计算完啦！')

    return wrapper

# 调用装饰器
@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x + y))

add(10, 5)