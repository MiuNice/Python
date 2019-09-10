"""
    heap_sort.py    堆排序
"""


def heap_sort(_list):
    _n = len(_list)
    parent = (_n - 1) // 2
    for i in range(parent, -1, -1):
        heapify(_list, _n, i)
    for i in range(_n - 1, -1, -1):
        _list[0], _list[i] = _list[i], _list[0]
        heapify(_list, i, 0)
    return _list


def heapify(_list, _n, i):
    if i >= _n:
        return
    c1, c2 = i * 2 + 1, i * 2 + 2
    _max = i
    if c1 < _n and _list[c1] > _list[_max]:
        _max = c1
    if c2 < _n and _list[c2] > _list[_max]:
        _max = c2
    if _max != i:
        _list[i], _list[_max] = _list[_max], _list[i]
        heapify(_list, _n, _max)


if __name__ == "__main__":
    _list = [2, 30, 7, 9, 11, 4, 5, 9]
    print(heap_sort(_list))
    
