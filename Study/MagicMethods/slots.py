"""
    slots.py
"""


class Test:
    __slots__ = ("_name", "age")  # 只能绑定 tuple 中的属性(Attribute)
    # __abc__: int
    __abc__ = 1

    def __init__(self, name):
        self._name = name


class ChildTest(Test):
    # __slots__ = ("age",)  # 子类需要单独设置 __slots__
    pass


if __name__ == '__main__':
    t = Test("wMiu")
    # t.score = 99  # The score not in Test Class of slots.
    # Error : AttributeError: 'Test' object has no attribute 'score'
    t.age = 18
    print(t.age)
    print(t.__abc__)

    print("- 分割 -")

    c = ChildTest("wMiu")
    c.score = 99  # 继承后的子类 不受父类 __slots__ 限制
    print(c.score)
