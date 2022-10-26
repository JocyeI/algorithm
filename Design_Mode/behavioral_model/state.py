# encoding: utf-8

"""
设计模式：行为型
17.状态模式

当一个对象的内在状态改变时，允许改变其行为，这个对象看起来更像是改变了其类

- 解决：当控制一个对象状态改变的条件表达式过于复杂的情况
       把状态的判断逻辑转移到表示不同状态的一系列类中，可把复杂的判断逻辑简单化

- 好处：将与特定状态相关的行为局部化，并且将不同状态的行为分割开来
- 通过定义新的子类，可以很容易地增加新的状态和转换
- 消除庞大的条件分支语句，减少相互间的依赖，把各种状态换衣逻辑分布到state的子类之间
- 适用：当一个对象的行为却决于它的状态，并且它不许在允许时刻改变其行为，使用状态模式
"""

from abc import ABCMeta, abstractmethod

class State(metaclass = ABCMeta):
    """
    抽象状态类，定义一个接口以封装与Context的一个特定状态相关的行为
    """

    @abstractmethod
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        """
        设定下一个状态是
        :param context:  下一个状态
        :return: 返回下一个状态的内容
        """
        context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self, context):
        """
        设定下一个状态是
        :param context: 下一个状态
        :return: 返回下一个状态内容
        """
        context.state = ConcreteStateA()

class Context(object):
    """
    维护一个ConcreteState子类实列，这个实列定义当前的状态
    """
    def __init__(self, state):
        self.__state = state

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        print("current status:", value.__class__.__name__)
        self.__value = value

    def request(self):
        self.__state.handle(self)

if __name__ == '__main__':
    c = Context(ConcreteStateA())

    c.request()
    c.request()
    c.request()
    c.request()