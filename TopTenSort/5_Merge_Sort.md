# 归并排序

## 简介

归并排序(merge sort)是一种非常高效的排序方法，它用来分治的思想，基本思想是：

1.先将整个序列两两分开，然后每组中的两个元素排好顺序

2.接着就是组与组和合并，只需要将两组所有的元素遍历一遍，即可按顺序合并

3.以此类推，最终所有组合并为一组时，整个数列完成排序

## 实现步骤

1.把长度为n的输入序列分成两个长度为n/2的子序列

2.对这两个子序列分别采用递归的进行排序

3.将两个排序好的子序列的元素拿出来，按照顺序合并成一个最终的序列，即可完成排序

## 代码实现(Python)

```python
from typing import List

def merge(arr1: List[int], arr2: List[int]):
    # 1.定义一个遍历来接收排序结果
    result = []
    
    # 2.遍历，并判断大小
    while arr1 and arr2:
        # 3.如果a1中第一个元素小于a2第一个元素
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    if arr1:
        result += arr1
    if arr2:
        result += arr2
    return result


def merge_sort(arr: List[int]):
    """
    归并排序
    :param arr: 待排序的List
    :return: 排好序的List
    """
    if len(arr) <= 1:
        return 
    
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

# 测试数据
if __name__ == '__main__':
    import random
    random.seed(54)
    arr = [random.randint(0,100) for _ in range(10)]
    print("原始数据：", arr)
    arr_new = merge_sort(arr)
    print("归并排序结果：", arr_new)
    
    
# 输出结果
原始数据： [17, 56, 71, 38, 61, 62, 48, 28, 57, 42]
归并排序结果： [17, 28, 38, 42, 48, 56, 57, 61, 62, 71]
```

## 动图演示

 ![归并排序动画演示](Images/701d53bd85cfca937c1a3172d67630cd.webp) 

## 算法分析

-   时间复杂度

归并排序时间复杂度的计算公式： 排序总时间 = 子序列排序时间 + 合并时间，假设一个序列有n个数的排序时间为$T(n)$，那么$T(n) = 2T(\frac{n}{2})+合并时间$

由于合并时，两个子序列已经组内排好序了。将两个排号序的序列组合成一个大的有序序列，时间复杂度为$n$，则：

$T(n) = 2T(\frac{n}{2}) + n$

递归推到可得出：

$T(n) = 2^mT(\frac{n}{2^m}) + mn$，

当$(\frac{n}{2^m}) = 1$ 时，递归结束，此时有：

$T(1) = 0, T(n) = nlog_2n$

所以归并排序的时间复杂度为$O(nlog_2n)$

-   空间复杂度

每次递归需要用到一个辅助表，长度与待排序的表相等，虽然不递归的次数是$(O(log_2n))$，但是，每次递归都会释放掉所占的辅助空间，下次递归的栈空间和辅助空间与这部分释放的空间就不相关了，因而空间复杂度为$O(n)$

-   稳定性

归并排序过程中，能够保证相等于的元素相对位置不变，因此，为稳定排序

-   总结

| 时间复杂度(平均) | 时间复杂度(平均) | 时间复杂度(最坏) | 空间复杂度 | 排序方式  | 稳定性 |
| ---------------- | ---------------- | ---------------- | ---------- | --------- | ------ |
| $O(nlog_2n)$     | $O(nlog_2n)$     | $O(nlog_2n)$     | $O(n)$     | out_place | 稳定   |



