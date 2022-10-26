# encoding: utf-8

"""
设计模式：行为型
24.迭代器模式

提供一种方法顺序地访问聚合对象种的各个元素，而不是保留随便更改对象的内部表示

- 无差别遍历聚合对象
- 需要对聚合进行多种遍历时
- 分离了集合对象的遍历行为，做到不是保留集合内部结构，又可以让外部代码透明的访问集合内部

用于在数据集合中按照顺序遍历集合, 让用户通过特定的接口巡访容器中的每一个元素而不用了解底层的实现
wiki: https://zh.wikipedia.org/wiki/%E8%BF%AD%E4%BB%A3%E5%99%A8%E6%A8%A1%E5%BC%8F
python:
    - http://nvie.com/posts/iterators-vs-generators/
    - https://docs.python.org/3.6/glossary.html#term-iterator
    - https://docs.python.org/3.6/library/collections.abc.html?highlight=iterable#collections.abc.Iterable
    - https://docs.python.org/3.6/library/collections.abc.html?highlight=iterator#collections.abc.Iterator
"""

# 不考虑默认迭代器

from abc import ABCMeta, abstractmethod

class Iterator(metaclass = ABCMeta):
    """
    迭代抽象类:
    定义迭代器抽象方法
    """
    @abstractmethod
    def __iter__(self):
        """
        迭代
        """
    def __next__(self):
        """
        下一个元素
        """
        pass

class ConcreteIterator(Iterator):
    def __init__(self, aggregate):
        self.__aggregate = aggregate
        self.index = 0

    def __next__(self):
        try:
            value = self.__aggregate[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return value

    def __iter__(self):
        return self

# 定义一个迭代器
import collections

class YRange(collections.Iterator):
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


if __name__ == '__main__':
    aggregate = "a b c d e".split()

    print(issubclass(ConcreteIterator, collections.Iterator))

    it = ConcreteIterator(aggregate)
    i = iter(it)

    # equals to for j in i
    while True:
        try:
            print(next(i))
        except StopIteration:
            del i
            break

    y = YRange(3)
    print(list(y))

    y1 = YRange(5)
    print(iter(y1))