#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lq
# datetime:2020/3/19 6:22 下午
# software: PyCharm


def bubbling(lists):
    """
    冒泡排序
    时间复杂度：O(n2) # 计算重复运行代码数量
    空间复杂度：O(1) # 占用内存的多少
    :return:
    """
    for i in range(len(lists) - 1):
        for j in range(len(lists) - i - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    print(lists)


def quick_sort(lists):
    """
    快速排序
    :param lists:
    :return:
    """
    if len(lists) < 2:
        return lists
    mid = lists[round(len(lists) / 2)]
    left, right = [], []
    lists.remove(mid)
    for list in lists:
        if list >= mid:
            right.append(list)
        else:
            left.append(list)
    return quick_sort(left) + [mid] + quick_sort(right)


def insert_sort(lists):
    """
    插入排序
    :return:
    """
    if len(lists) < 2:
        return lists
    for i in range(1, len(lists)):
        current = lists[i]  # 当前元素
        pre_index = i - 1  # 与当前元素比较的元素
        while pre_index >= 0 and lists[pre_index] > current:
            lists[pre_index + 1] = lists[pre_index]
            pre_index -= 1
        lists[pre_index + 1] = current
    return lists


if __name__ == '__main__':
    # lists = [6, 1, 29, 3, 32, 60]
    # bubbling(lists)
    # lists_a = [11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 22]
    # data = quick_sort(lists_a)
    # print(data)
    lists_b = [11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]
    data_b = insert_sort(lists_b)
    print(data_b)
