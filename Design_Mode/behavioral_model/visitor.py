# encoding: utf-8

"""
设计模式：行为型
21.访问者模式

标识一个卓越与某对象结构种各元素的操作

可以使你在不改变各个元素类的前提下定义用于这些元素的新操作

- 适用于数据结构相对稳定的系统，把数据结构和作用于结构上的操作之间的耦合解脱开，使得操作集合可以相对自由的演化
- 目的：把处理从数据结构分离出来，有比较稳定的数据结构，又有易于变化的算法
- 有点：增加新的操作很容易，等一同于一个新的访问者
"""

from abc import ABCMeta, abstractmethod

class Visitor(metaclass = ABCMeta):
    """
    为该对象结构种concreteelement的每一个类声明一个visit操作
    """
    @abstractmethod
    def visitor_concrete_element_a(self, concrete_element_a):
        pass

    @abstractmethod
    def visitor_concrete_element_b(self, concrete_element_b):
        pass

class ConcreteVisitor1(Visitor):
    """
    具体访问者，实现每个声明操作
    每个操作实现算法的一部分，而该算法片段乃是对应于结构种对象的类
    """

    def visitor_concrete_element_a(self, concrete_element_a):
        print("%s visit %s" % (self.__class__.__name__,
                               concrete_element_a.__class__.__name__))

    def visitor_concrete_element_b(self, concrete_element_b):
        print("%s visit %s" % (self.__class__.__name__,
                               concrete_element_b.__class__.__name__))

class ConcreteVisitor2(Visitor):
    """
    具体访问者，实现每个声明操作
    每个操作实现算法的一部分，而该算法片段乃是对应于结构种对象的类
    """

    def visitor_concrete_element_a(self, concrete_element_a):
        print("%s visit %s" % (self.__class__.__name__,
                               concrete_element_a.__class__.__name__))

    def visitor_concrete_element_b(self, concrete_element_b):
        print("%s visit %s" % (self.__class__.__name__,
                               concrete_element_b.__class__.__name__))

class Eelement(metaclass = ABCMeta):
    """
    定义一个accept操作，以一个访问者作为参数
    """
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteElementA(Eelement):
    """
    具体实现元素，实现accept操作
    """
    def accept(self, visitor):
        visitor.visitor_concrete_element_a(self)

class ConcreteElementB(Eelement):
    """
    具体实现元素，接受accept操作
    """
    def accept(self, visitor):
        visitor.visitor_concrete_element_b(self)


class ObjectStructure(object):
    """
    能够枚举它的元素，可以提供一个高层的接口以一奶香访问者访问它的元素
    """
    def __init__(self):
        self.__element = []

    def attach(self, element):
        self.__element.append(element)

    def detach(self, element):
        self.__element.remove(element)

    def accept(self, visitor):
        for e in self.__element:
            e.accept(visitor)


if __name__ == '__main__':
    os = ObjectStructure()

    os.attach(ConcreteElementA())
    os.attach(ConcreteElementB())

    v1 = ConcreteVisitor1()
    os.accept(v1)

    v2 = ConcreteVisitor2()
    os.accept(v2)

