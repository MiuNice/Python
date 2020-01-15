"""
    NamedTuple.py  用来构建简单且无方法的类（继承自tuple类）
    collections.namedtuple(typename, field_names, verbose=False, rename=False)
    typename : 类名
    field_names : 字段名，值可以是可迭代对象或逗号(英文)相隔的字符串
    verbose ：布尔值、默认为False，若为True则打印类的定义代码。
    rename ：布尔值、默认为False，默认会对字段名检测若不合法则抛出异常；
            如果设置为True则不会抛出异常，重新命名不合法的字段名为 _$d, $d索引
"""
import collections

# 设置field_names 的多种方法
field_names1 = ("x", "y")
field_names2 = ["x", "y"]
field_names3 = "1,2"

Point = collections.namedtuple("Point", field_names1)
p1 = Point(1, 2)
print(p1.x, p1.y)

# 显示构造类的代码
Point2 = collections.namedtuple("Point2", field_names1, verbose=True)

# rename 对不合法的属性名自动修改
Point3 = collections.namedtuple("Point2", field_names3, rename=True)
p3 = Point3(1, 2)
print(p3._0, p3._1)
