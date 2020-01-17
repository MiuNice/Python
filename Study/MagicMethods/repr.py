"""
    repr.py  __repr__
"""


class Test:
    def __init__(self):
        self._val = "Repr"

    def __repr__(self):
        return "Test({})".format(self._val)


if __name__ == '__main__':
    t = Test()
    # print(t)  # 若不重写repr方法则返回。<__main__.Test object at 0x000001522C3A97F0>
    print(t)  # Test(Repr)
