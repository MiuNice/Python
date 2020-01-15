"""
    len.py  __len__
"""


class Test:
    def __init__(self):
        self._val = [i for i in range(1, 101)]

    def __len__(self):
        return len(self._val)


if __name__ == '__main__':
    t = Test()
    # 如果想使用len() 必须重写 __len__ 方法，否则报错
    print(len(t))
