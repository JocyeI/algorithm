# encoding: utf-8

"""
设计模式：结构型
8.桥接

将抽象部分与它的实现部分进行分离，使得它们都可以独立地变化

- 独立变化
"""

from abc import ABCMeta, abstractmethod

class Implementor(metaclass = ABCMeta):
    """实现接口"""
    @abstractmethod
    def operation(self):
        pass

class ConcreteImplementorA(Implementor):
    def operation(self):
        print("plan A")

class ConcreteImplementorB(Implementor):
    def operation(self):
        print("plan B")

class Abstraction(object):
    def __init__(self, implementor = None):
        if implementor is not None:
            self.__implementor = implementor

    @property
    def implementor(self):
        return self.__implementor

    @implementor.setter
    def implementor(self, value):
        self.__implementor = value

    def operation(self):
        self.__implementor.operation()

class RefineAbstraction(Abstraction):
    pass

if __name__ == '__main__':
    ab = RefineAbstraction()

    ab.implementor = ConcreteImplementorA()
    ab.operation()

    ab.implementor = ConcreteImplementorB()
    ab.operation()