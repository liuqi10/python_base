#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:lq
# datetime:2020/3/18 11:19 下午
# software: PyCharm
import copy


class StuCopy:

    list_a = ["a", "c"]
    list_b = ["a", ["b", "c"], "d", "e"]
    list_c = "abc"

    # 浅拷贝
    def shallow_copy(self):
        a = copy.copy(self.list_a)
        c = self.list_a
        print(id(self.list_a))
        print(id(a))
        print(id(c))

        e = copy.copy(self.list_c)
        print(id(self.list_c))
        print(id(e))

        print(id(self.list_b))
        b = copy.copy(self.list_b)
        d = self.list_b
        print(id(b))
        print(id(d))

    # 深拷贝
    def shallow_deepcopy(self):
        print(id(self.list_a))
        a = copy.deepcopy(self.list_a)
        print(id(a))

        print(id(self.list_b))
        b = copy.deepcopy(self.list_b)
        print(id(b))


if __name__ == '__main__':
    data = StuCopy()
    data.shallow_copy()
    # data.shallow_deepcopy()