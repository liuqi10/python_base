#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lq
# datetime:2020/4/3 4:00 下午
# software: PyCharm
import pdb


def stu_try():
    try:
        return 10 / "1"
    except Exception as e:
        print(e)
    print("123")


if __name__ == '__main__':
    stu_try()
