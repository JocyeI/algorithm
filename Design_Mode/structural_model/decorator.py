# encoding: utf-8

"""
设计模式：结构型
10.装饰模式

动态地给一个对象添加一些额外的职责
就增加功能来说，装饰模式比生成模式子类更加灵活

- 装饰模式：视为已有功能动态地添加更多功能的一种方法
- 有效地将核心职责和装饰功能区分开
"""

from abc import ABCMeta, abstractmethod

class Component(metaclass = ABCMeta):
    """
    定义一个对象接口，可以给这些对象动态地增加职责
    """
    @abstractmethod
    def operational(self):
        pass

class ConcreteComponent(Component):
    """
    定义一个具体对象，也可以给这个对象增加职责
    """
    def operational(self):
        print("Hello World")

class Decortor(Component):
    """
    装饰器抽象类
    继承了component，从外类来扩展component类的功能
    但对于component来说，是无序知道decortor类的存在的
    """
    def __init__(self, component):
        self.__component = component

    def operational(self):
        if self.__component:
            self.__component.operational()

class DecortorA(Decortor):
    """
    具体装饰对象，给component添加职责
    """
    def operational(self):
        print("<h1>")
        super(DecortorA, self).operational()
        print("</h1>")

class DecortorB(Decortor):
    def operational(self):
        print("<strong>")
        super(DecortorB, self).operational()
        print("</strong>")

if __name__ == '__main__':
    c = ConcreteComponent()
    d1 = DecortorA(c)
    d1.operational()

    d2 = DecortorB(d1)
    d2.operational()