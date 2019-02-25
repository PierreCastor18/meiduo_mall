# _*_ coding: utf-8 _*_
import time

from past.builtins import reduce

__author__ = '其实很简单'
__date__ = '19-1-29 下午6:52'


# 函数装饰器
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('程序用时　%s　秒' %(end_time - start_time))
    return wrapper


@timer      #调用装饰器
def test(sleep_time):
    time.sleep(sleep_time)

test(2)