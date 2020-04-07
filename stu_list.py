#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lq
# datetime:2020/3/18 10:41 下午
# software: PyCharm


class Stulist:
    lists = ["name", "age", "score"]

    # 列表添加元素
    def list_append(self):
        a = "phone"
        self.lists.append(a)
        print(self.lists)

    # 列表指定位置插入元素
    def list_insert(self):
        a = "phone"
        self.lists.insert(1, a)
        print(self.lists)

    # 列表删除元素
    def list_pop(self):
        print(self.lists.pop())
        print(self.lists)

    def list_remove(self):
        print(self.lists.remove("score"))
        print(self.lists)

    # 清空列表元素
    def list_clear(self):
        self.lists.clear()
        print(self.lists)

    # 批量添加元素
    def list_extend(self):
        lists_a = ["score", "name"]
        self.lists.extend(lists_a)
        print(self.lists)

    # 统计元素出现次数
    def list_count(self):
        lists = ["name", "age", "score", "phone", "score"]
        print(lists.count("score"))

    # 列表反转
    def list_reverse(self):
        lists = ["name", "age", "score", "phone", "score"]
        lists.reverse()
        print(lists)

    # 列表排序
    def list_sort(self):
        lists = ["name", "age", "score", "phone", "score"]
        lists.sort()
        print(lists)
        lists.sort(reverse=True)
        print(lists)
        lists1 = [1, 2, 3]
        print(lists1[::-1])

    # 列表复制
    def list_copy(self):
        lists = ["name", "age", "score", "phone", "score"]
        print(id(lists))
        lists_new = lists.copy()
        print(id(lists_new))
        print(lists_new)


if __name__ == '__main__':
    data = Stulist()
    data.list_sort()
