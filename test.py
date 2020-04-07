#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lq
# datetime:2020/3/19 11:32 上午
# software: PyCharm

def readlog():
    count = 0
    str = ""
    with open(r'./file/log.txt', encoding='utf-8') as files:
        file = files.readlines()
    lists = [x[4] for x in file if len(x) >= 5]
    print(sorted(lists))
    for i in sorted(set(lists)):
        if lists.count(i) > int(count):
            count = lists.count(i)
            str = i
    print(str, count)


from itertools import product


class ListTool(object):
    count = 0
    mid = 0

    def __init__(self, lists):
        self.lists = lists

    def a(self):
        # for i in range(1, len(self.lists)+1):
        data = list(product(self.lists, self.lists))
        print(data)


def a(n):
    if isinstance(n, int):
        if n >= 0:
            return int(str(n)[::-1])
        else:
            new_n = str(abs(n))[::-1]
            return int("-" + new_n)


if __name__ == '__main__':
    print(a(0))
