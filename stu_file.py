#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lq
# datetime:2020/3/24 5:44 下午
# software: PyCharm
import os
import math
import time

file1 = r"./file/"


def size_file(file, mode="KB"):
    """
    获取文件大小
    :param file:
    :param mode:
    :return:
    """
    file_size = os.path.getsize(file)
    n = 0
    if mode == "KB":
        n = 1
    elif mode == "MB":
        n = 2
    elif mode == "GB":
        n = 3
    return round(file_size / math.pow(1024, n), 2)


def read_file(file, size=1024 * 1024, mode='r'):
    """
    配置文件
    :param file:
    :param size:
    :param mode:
    :return:
    """
    with open(file, mode, encoding='utf-8') as f:
        count = 0
        while True:
            check_content = f.readlines(size)
            if not check_content:
                break
            count += 1
            write_file(os.path.join(file1, str(time.time()) + ".txt"), check_content)


def write_file(file, content, mode='a'):
    """
    文件写入
    :param file:
    :param content:
    :param mode:
    :return:
    """
    with open(file, mode=mode, encoding='utf-8') as f:
        if isinstance(content, str):
            f.write(content)
        else:
            f.writelines(content)
    f.close()


def getmtime_file(path):
    list = os.listdir(path)
    sort_list = sorted(list, key=lambda x: os.path.getmtime(os.path.join(path, x)))
    print(sort_list)


def get_file():
    pass


# 读写内存数据
from io import StringIO, BytesIO


def stu_stringio():
    f = StringIO()
    f.write("hello")
    f.write("---")
    f.write("123123")
    f.write("world!")
    print(f.getvalue())


def stu_stringio1():
    f = StringIO("hello\n----\nworld\n")
    while True:
        s = f.readline()
        if s == "":
            break
        print(s.strip())

def stu_bytesio():
    f = BytesIO()
    f.write("张三".encode("utf-8"))
    value = f.getvalue()
    print(value)


def stu_bytesio1():
    f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    s = f.read()
    print(s.strip())

import os


def stu_path():
    print(os.path.abspath("."))  # 获取当前路径绝对规范化路径
    # os.mkdir(r'/Users/lq/PycharmProjects/python_base/test')  # 创建一个目录
    # time.sleep(3)
    # os.rmdir(r'/Users/lq/PycharmProjects/python_base/test')  # 删除当前目录
    # 拆分当前目录
    path_file = os.path.split(r"/Users/lq/PycharmProjects/python_base/test.py")
    print(path_file)

if __name__ == '__main__':
    file = r"./file/log.txt"
    # read_file(file, 1024*1024, 'r')
    # print(size_file(file, "MB"))
    # read_file(file)
    # getmtime_file(r"./file/")
    # stu_stringio()
    # stu_stringio1()
    # stu_bytesio()
    # stu_bytesio1()
    # print(os.name)
    # print(os.uname())
    stu_path()

