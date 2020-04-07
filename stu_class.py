#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lq
# datetime:2020/3/31 11:19 下午
# software: PyCharm

"""
类学习
dir()获取类中所有属性和方法
hasattr(object, name) 判断对象中是否有该属性
setattr(object, name, value) 设置对象属性且赋值
getattr(object, name) 获取对象属性
"""


def set_method(self):
    """
    需要类绑定的方法
    :param self:
    :return:
    """
    print("类绑定方法")


class StuClass(object):
    # __slots__ = ("name", "age", "score")  # 限定动态绑定属性，对继承子类不生效
    a = 10

    def __init__(self):
        self.__score = 0

    def stu_method1(self):
        print("ok")

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.score = value

class Student(object):
    _score = 0
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value >100:
            raise ValueError('score must between 0~100!')
        self._score=value


if __name__ == '__main__':
    # StuClass.set_method = set_method  # 动态绑定方法
    data = StuClass()
    # stu1 = getattr(data, 'stu_method1')
    # data.set_method()
    # data.name = "zhangsan"
    print(data.score)

    s = Student()
    s.score
