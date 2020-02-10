"""
    Sorted.py  对所有可迭代对象进行排序
    sorted(__iterable, key, reverse)
        __iterable : 可迭代对象
        key ：传一个函数；用来比较元素，一个参数
        reverse ：布尔值，默认为False；True为降序，False为升序。
    Return： List 排好序的列表
"""

_l = [5, 3, 2, 1, 4]
print(sorted(_l))  # 默认升序
print(sorted(_l, reverse=True))  # 降序

_l2 = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
print(sorted(_l2, key=lambda item: item[-1]))  # key = function
print(sorted(_l2, key=lambda item: item[-1], reverse=True))  # 降序

# 利用Key 实现倒序
print(sorted(_l, key=lambda item: -item))
print(sorted(_l2, key=lambda item: -(item[-1])))
