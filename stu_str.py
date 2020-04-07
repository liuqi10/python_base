#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lq
# datetime:2020/3/18 9:11 下午
# software: PyCharm


class StuStr(object):
    """
    """

    # 去除字符串空格
    def char_space(self):
        str = "   charspace   "
        str_new = str.strip()
        print(str_new)

        str_l = str.lstrip()
        print(str_l)

        str_r = str.rstrip()
        print(str_r)

    # 链接两个字符串
    def str_connect(self):
        str_list = ["str", "connect"]
        str = "-".join(str_list)
        print(str)

    # 字符串大小写转化
    def str_transformation(self):
        str = "HelloWorld"
        str_lower = str.lower()
        print(str_lower)
        str_upper = str.upper()
        print(str_upper)

    # 统计字符数
    def str_count(self):
        str = "helloworld"
        print(str.count('l'))

    # 判断字符串开头和结尾
    def str_startend(self):
        str = "helloworld"
        str_start = str.startswith("he")
        str_end = str.endswith("ld")
        print(str_start)
        print(str_end)

    # 分割字符串
    def str_partition(self):
        str = "helloworld"
        ret = str.partition("lo")
        print(ret)

    # 替换字符串
    def str_replace(self):
        str = "helloworld"
        print(str.replace("h", "H"))

    # 按指定字符分割字符串
    def str_split(self):
        str = "helloworld"
        print(str.split("o"))

    # 添加字符
    def str_add(self):
        str = "hello world "
        str_a = "python"
        for i in str_a:
            str += i
        print(str)

    # 字符串反转
    def str_reverse(self):
        str = "hello world"
        str_a = "".join(reversed(str))
        print(str_a)
        print(str[::-1])

    def str_reversal(self):
        str = "hello world"
        str_a = str[::-1]
        print(str_a)

    def str_set(self):
        str = "hello world"
        print(set(str))

    def str_sort(self):
        str = "hello world"
        print(sorted(str))

    def str_count(self):
        """
        字符串统计
        :return:
        """
        dict = {}
        str = "aaabbbccceeee"
        set_str = set(str)
        for i in set_str:
            dict[i] = str.count(i)

    def str_counts(self):
        """
        重复子字符串统计
        :return:
        """
        src_str = "aabbccdefjhigk"
        new_str = set([i for i in src_str if src_str.count(i) >= 2])
        print(new_str)

    def str_1(self):
        """
        字符串截取
        :return:
        """
        str = "abcdef"
        print(str[::2])

if __name__ == '__main__':
    data = StuStr()
    # data.char_space()
    # data.str_connect()
    # data.str_transformation()
    # data.str_count()
    # data.str_startend()
    # data.str_partition()
    # data.str_replace()
    # data.str_split()
    # data.str_add()
    # data.str_reverse()
    # data.str_reversal()
    # data.str_set()
    # data.str_sort()
    # data.str_1()
    data.str_partition()
    data.str_split()
