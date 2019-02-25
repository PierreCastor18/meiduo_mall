# _*_ coding: utf-8 _*_
__author__ = '其实很简单'
__date__ = '19-1-29 下午7:12'


#　函数装饰器
def say_hello(contry):
    def wrapper(func):
        def demo(*args, **kwargs):
           if contry == 'china':
               print('你好')
           elif contry == 'america':
               print('hello.')
           else:
               return
           # 函数执行的地方
           func(*args, **kwargs)
        return demo
    return wrapper


# 调用装饰器
@say_hello('china')
def american():
    print('我来自中国')


@say_hello('america')
def chinese():
    print('I am from american')


american()
print('+分界线+'*10)
chinese()

