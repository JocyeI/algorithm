# encoding: utf-8

"""
设计模式：创造型
5.原型模式

用原型实列指定创建对象的种类。并且通过拷贝这些原型创建新的对象

- 原型模式其实是从一个对象再创建另一个可定制的对象，而且不需要知道任何创建细节
- 一般再初始化信息不会发生的情况，克隆是最好的办法，即隐藏了对象创建的细节，也提高了性能

在不指定类名的前提下生成实列
- 对象种类繁多。无法将它们整合到一个类中
- 难以根据类生成实列时
- 解耦框架与生成实列，让框架不依赖具体的类，不能指定类名来生成实列，要实现注册一个原型，然后，通过赋值该实列来生成新的实列

why:
一旦在代码中出现要实现的类的名字，就无法与该类分离开开，也就无法实现复用
"""

import copy
from abc import ABCMeta, abstractmethod

class ProtoType(metaclass = ABCMeta):
    """
    原型类：声明一个克隆自身的接口
    """
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @abstractmethod
    def clone(self):
        pass

class ConcretePrototypeA(ProtoType):
    """
    具体原型类。实现一个克隆自身的操作
    """
    def clone(self):
        # 浅拷贝
        return copy.copy(self)

class ConcretePrototypeB(ProtoType):
    """
    具体原型类。实现一个克隆自身的操作
    """
    def clone(self):
        return  copy.copy(self)

class Manager(object):
    """
    管理类
    """
    def __init__(self):
        self._dict = {}

    def register(self, name, prototype):
        self._dict[name] = prototype

    def create(self, proto_name):
        p = self._dict.get(proto_name)
        return p.clone()

if __name__ == '__main__':
    ca = ConcretePrototypeA(1)
    c2 = ca.clone()
    print(c2.id)

    # with manager
    cb = ConcretePrototypeB(1)
    c3 = cb.clone()
    print(c3.id)

    m = Manager()
    m.register("ca: ", ca)
    m.register("cb: ", cb)

    x = m.create("ca")
    print(x.id)