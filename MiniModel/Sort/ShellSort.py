"""
    ShellSort.py 希尔排序
"""

def shell_sort(_list):
    gap = len(_list) // 2
    while gap > 0:
        for i in range(gap, len(_list)):
            now = _list[i]
            j = i
            while j >= gap and now < _list[j - gap]:
                _list[j] = _list[j - gap]
                j -= gap
            _list[j] = now
        gap = gap // 2
    return _list


if __name__ == "__main__":
    _list = [11, 4, 78, 5, 9, 20, 1, 69, 99]
    print(shell_sort(_list))