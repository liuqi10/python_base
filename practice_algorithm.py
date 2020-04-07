#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lq
# datetime:2020/4/1 11:17 上午
# software: PyCharm
"""
算法练习
"""


class PracticeAlgorithm(object):

    def get_median(self, n):
        """
        获取中位数
        :param n:
        :return:
        """
        lists = sorted(n)
        size = len(n)

        count = [i for i in n if isinstance(i, int)]
        if len(count) == size:
            if size % 2 == 1:
                return lists[int((size - 1) / 2)]
            else:
                if not size == 0:
                    return (lists[int(size / 2)] + lists[int(size / 2) - 1]) / 2
        else:
            return "not int list"

    def stu_reverse(self):
        pass


if __name__ == '__main__':
    lists = ["a", "b", "c", "d"]
    data = PracticeAlgorithm()
    print(data.get_median(n=lists))
    print(dir(data))
