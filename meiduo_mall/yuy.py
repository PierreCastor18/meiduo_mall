# _*_ coding: utf-8 _*_
__author__ = '其实很简单'
__date__ = '19-2-21 下午3:35'

# l = [1,2,4,6,7,98,22,56]
# num = []
# for i in l:
#     if i % 2 == 0:
#         num.append(i)
#
#         print(sum(num))
# list_1 = [1,[2,3],[4,5,6,7,[8,9,10]]]
#
# def flat(nums):
#
#     for i in nums:
#         if isinstance(i, list):
#             flat(i)
#         else:
#
#             print(i)
#
# flat(list_1)

# def getiteam(l):
#     for iteam in l:
#         if isinstance(iteam, list):
#             getiteam(iteam)
#         else:
#             print(iteam)
#
# getiteam(list_1)
def is_leap_year(year):
    # 判断是否是闰年
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def get_day(year, month):
    # 给定年月返回月份的天数
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28

def get_total_day(year, month):
    # 获取自１８００年一共多少天
    days = 0
    for y in range(1800, year):
        if is_leap_year(year):
            days += 366
        else:
            days += 365

    for m in range(1, month):
        days += get_day(year, m)
    return days

def get_start(year, month):
    # 返回当日１日是星期几
    return 3 + get_total_day(year, month) % 7

month_dict = {1 : '一月', 2 : '二月', 3:'三月', 4:'四月', 5:'五月',
6:'六月', 7:'七月', 8 :'八月', 9:'九月', 10:'十月', 11:'十一月', 12:'十二月'
}

def get_month_name(month):
    #　返回当月名字
    return month_dict[month]


def print_month_title(year, month):
    # 打印日历的首部
    print('    ', get_month_name(month), '    ', year, '    ')
    print('--' * 10)
    print(' Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')

def month_body(year, month):
    i = get_start(year, month)
    if i != 7:
        print('  ')
        print('  ' * i)

    for j in range(1, get_day(year, month) + 1):
        print('%4d' %j)
        i += 1
        if i % 7 == 0:
            print(' ')


year = int(input('输入年：'))
month = int(input('输入月：'))
print_month_title(year, month)
month_body(year, month)