#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lq
# datetime:2020/3/30 2:23 下午
# software: PyCharm
import time
import functools

"""
    高阶函数教程
    1.把函数作为参数传递
    2.把函数作为结果返回
"""


def stu_map(n):
    """
    map函数使用,高阶函数
    new_list是迭代器,惰性序列
    :param n:
    :return:
    """
    new_list = [i for i in map(lambda x: x ** x, n)]
    print(new_list)


def stu_map1(n):
    result = [i for i in map(lambda x: x.title(), n)]
    print(result)


from functools import reduce


def stu_reduce(n):
    """
    迭代组合
    :param n:
    :return:
    """
    result = reduce(lambda x, y: x * 10 + y, n)
    print(result)


def stu_filter(n):
    """
    filter 函数过滤不符合条件的数据
    :param n:
    :return:
    """
    result = filter(lambda x: x % 2 == 0, n)
    result = [i for i in result]
    print(result)


def stu_sorted(n):
    """
    排序方法，可以通过参数值控制
    :param n:
    :return:
    """
    try:
        result = sorted(n, key=abs, reverse=True)
    except Exception as e:
        result = sorted(n, key=str.upper, reverse=True)
    print(result)


def stu_sorted1(n, param=0):
    """
    排序，param参数设置
    :param n:
    :param param:
    :return:
    """

    if isinstance(n, dict):
        result = sorted(n.items(), key=lambda x: x[param])
        print(result)


def stu_bibao():
    """
    闭包函数
    :return:
    """
    a = 1
    b = 2

    def count_sum():
        return a + b

    return count_sum


def stu_decorator(func):
    """
    装饰器函数
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print(end_time - start_time)

    return wrapper


@stu_decorator
def count_time(n):
    time.sleep(n)
    print("显示等待时间{}".format(n))


def stu_partial(n):
    """
    偏函数
    :return:
    """
    data = int(n, base=16)
    int1 = functools.partial(int, base=2)
    print(data)
    print(int1(n))


if __name__ == '__main__':
    # list = [1, 2, 3, 4, 5]
    # list1 = ['adam', 'LISA', 'barT']
    # list2 = [-1, -3, 5, 3, 1]
    # list3 = {"name": "zhangsan", "age": "20", "address": "北京市海淀区"}
    # stu_map(list)
    # stu_map1(list1)
    # stu_reduce(list)
    # stu_filter(list)
    # stu_sorted(list1)
    # stu_sorted1(list3, 1)
    # print(stu_bibao()())
    # count_time(3)
    stu_partial("10")
