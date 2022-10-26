# encoding: utf-8

"""
设计模式：结构型
12.享元模式

运用共享技术有效地支持大量细粒度的对象

- 可以避免大量相似类的开销
- 把区分的参数放在类实列外面，在方法调用时传递出去

- 如果一个应用程序使用了大量对象。而大量的这些对象造成了很大的存储开销时
"""

from  abc import ABCMeta, abstractmethod

class Flyweight(metaclass = ABCMeta):
    """
    所有具体享元的超累或接口
    通过这个接口，flyweight可以接收并作用与外部状态
    """
    @abstractmethod
    def operation(self, extrinsic_state):
        pass

class ConcreteFlyweight(Flyweight):
    """
    继承flyweight超类或实现fltweight接口，并未内部状态增加存储空间
    """
    def operation(self, extrinsic_state):
        print("specific flyweight", extrinsic_state)

class UnconcreteFlyweight(Flyweight):
    """
    不需要共享的flyweight子类
    """
    def operation(self, extrinsic_state):
        print("unshared flyweight", extrinsic_state)

class FlyweightFactory(object):
    """
    一个享原工厂，用来创建并管理flyweight对象，主要是用阿里确保合理的共享flyweight
    当用户请求一个flyweight时，flyweightFactory提供一个已经·创建的实列或者创建一个
    """
    def __init__(self):
        self.__flyweight = dict()
        fx = ConcreteFlyweight()
        self.__flyweight["X"] = fx

        fy = ConcreteFlyweight()
        self.__flyweight["Y"] = fy

    def add_flyweight(self, key, flyweight):
        self.__flyweight[key] = flyweight

    def get_flyweight(self, key):
        flyweight = self.__flyweight.get(key)
        if not flyweight:
            flyweight = ConcreteFlyweight()
            self.__flyweight[key] = flyweight

        return flyweight

if __name__ == '__main__':
    f = FlyweightFactory()
    flyweight = f.get_flyweight("X")
    flyweight.operation(100)



