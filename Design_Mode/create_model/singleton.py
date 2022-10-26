# encoding: utf-8

"""
设计模式：创造型
6.单列模式

保证一个类仅有一个实列，并提供一个访问他的全局访问点

- 确保任何情况下绝对只有一个实列

坑：
- 多进程，需要考虑加锁
- web时，往往时多进程启动
- web时， 扩容时还往往时多机器实列
"""

class Singleton_1(type):
    """基于元类实现单列模式"""
    def __init__(self, *args, **kwargs):
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance =super().__call__(self, *args, **kwargs)
            return self.__instance
        else:
            return self.__instance
class MyClass(metaclass=Singleton_1):
    pass

def singleton_2(cls):
    """基于装饰器实现单列模式"""
    def wrapper(*args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = cls(*args, **kwargs)
        return wrapper
@singleton_2
class Singleton_2():
    pass

class Singleton_3:
    def __new__(cls, *args, **kwargs):
        """基于__new__方法实现单列模式"""
        if not hasattr(cls, '__instance'):
            cls._instance = super(Singleton_3.cls).__new__.call__(cls, *args, **kwargs)
        return cls._instance

class Singleton_4:
    """基于静态方法实现单列模式"""
    @classmethod
    def getInstance(cls):
        if not hasattr(cls, '__instance'):
            cls.__instance = cls()
        return cls._instance

class Singleton_5:
    """
    基于模块实现单列模式
    """
    pass
s = Singleton_5()
# 在另一个py文件中导入该类对象
# from base import S

print(s)


class Singleton_6:
    """基于Monostate单列模式"""
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Singleton_6).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


if __name__ == '__main__':

    s1 = Singleton_1()
    s2 = Singleton_1()
    print(s1)
    print(s2)

    # Singleton_2，对象加括号执行元类中的__call__方法
    s1 = Singleton_2()
    s2 = Singleton_2()
    print(s1)
    print(s2)

    s1 = Singleton_3()
    s2 = Singleton_3()
    print(s1)  # <__main__.SingleTonTest object at 0x0000000000BD68D0>
    print(s2)  # <__main__.SingleTonTest object at 0x0000000000BD68D0>

    s1 = Singleton_4.getInstance()
    s2 = Singleton_4.getInstance()
    print(s1)  # <__main__.SingleTonTest object at 0x0000000000646828>
    print(s2)  # <__main__.SingleTonTest object at 0x0000000000646828>

    # 共享同一个字典，一个对象改变属性，另一个也跟着改变
    b1 = Singleton_6()
    b1.name = 'Bright'
    b2 = Singleton_6()

    print(b1.__dict__)  # {'name': 'Bright'}
    print(b2.__dict__)  # {'name': 'Bright'}

