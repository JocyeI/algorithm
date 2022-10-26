# encoding: utf-8

"""
设计模式：行为型
20.中介模式

适用一个中介对象来封装一些列的对象交互
中介者使各对象不需要显示的相互引用，从而使耦合松散，可以独立地改变它们之间的交互

- 多对多交互
- 把对象如何写作进行了抽象
"""

from abc import ABCMeta, abstractmethod

class Mediator(metaclass = ABCMeta):
    """
    抽象中介者，定义同时对象到中介对象的接口
    """
    @abstractmethod
    def send(self, msg, colleague):
        pass

class ConcreteMediator(Mediator):
    """
    具体中介对象，实现抽象类的方法
    需要知道所有具体的同事类，并冲具体的同时类接收消息，向具体同时对象发出命令
    """
    @property
    def colleague1(self):
        return self.__colleague1

    @colleague1.setter
    def colleague1(self, value):
        self.__colleague1 = value

    @property
    def colleague2(self):
        return self.__colleague2

    @colleague2.setter
    def colleague2(self, value):
        self.__colleague2 = value

    def send(self, msg, colleague):
        if colleague == self.__colleague1:
            self.__colleague2.notify(msg)
        else:
            self.__colleague1.send(msg)

class Colleague(metaclass = ABCMeta):
    """
    抽象同事类
    """
    def __init__(self, mediator):
        self.__mediator = mediator

    @property
    def mediator(self):
        return self.__mediator

    @mediator.setter
    def mediator(self, value):
        self.__mediator = value

    @abstractmethod
    def send(self, msg, colleague):
        pass

    @abstractmethod
    def notify(self, message):
        pass

class ConcreteColleague1(Colleague):
    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print("colleague 1 get message: ", message)

class ConcreteColleague2(Colleague):
    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print("colleague 2 get message: ", message)

if __name__ == '__main__':
    m = ConcreteMediator()

    c1 = ConcreteColleague1(m)
    c2 = ConcreteColleague2(m)

    m.colleague1 = c1
    m.colleague2 = c2

    c1.send("hello, I am C1")
    c2.send("Hey, I am C2")