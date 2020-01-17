"""
    filter.py
    filter(function, iterable) ： 过滤掉可迭代对象中不符合条件的数据
        function ：函数
        iterable : 可迭代对象
"""

re = filter(lambda x: x % 2 == 0, range(1, 11))
for i in re:
    print(i, end=" ")

# 比较 if
r = []
for i in range(1, 11):
    if i % 2 == 0:
        r.append(i)
print(r)
