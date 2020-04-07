#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lq
# datetime:2020/3/23 12:11 下午
# software: PyCharm


def stu_filter():
    """
    filter,内置函数，过了列表内容
    lambda,匿名函数，简化代码
    :return:
    """
    lists = [1, 2, 3, 4, 5, 6]
    result = list(filter(lambda x: x % 2 == 0, lists))
    print(result)


def bubble_sort(lists):
    """
    冒泡排序
    :return:
    """
    for i in range(len(lists) - 1):
        for j in range(0, len(lists) - i - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    print(lists)


def insert_sort(lists):
    """
    插入排序
    :return:
    """
    length = len(lists)
    for i in range(1, length):
        j = i - 1
        while j >= 0 and lists[j] > lists[i]:
            lists[j], lists[i] = lists[i], lists[j]
            j = j - 1
    print(lists)


def quicksort(lists):
    """
    快速排序
    :return:
    """
    if len(lists) < 2:
        print(lists)
    mid = lists[int(len(lists) / 2)]
    left, right = [], []
    lists.remove(mid)
    for list in lists:
        if list > mid:
            right.append(list)
        else:
            left.append(list)
    return quick_sort(left) + [mid] + quick_sort(right)


def quick_sort(b):
    """快速排序"""
    if len(b) < 2:
        return b
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = b[len(b) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    b.remove(mid)
    for item in b:
        # 大于基准值放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用迭代进行比较
    return quick_sort(left) + [mid] + quick_sort(right)


def niming(lists):
    """
    匿名函数使用
    :param lists:
    :return:
    """
    lists1 = [i ** 2 for i in lists]
    print(lists1)
    mid = lambda x: x ** 2
    lists2 = map(mid, lists)
    print(list(lists2))


if __name__ == '__main__':
    lists = [16, 8, 5, 6, 3]
    niming(lists)
