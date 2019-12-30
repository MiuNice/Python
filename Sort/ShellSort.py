"""
    ShellSort.py 希尔排序 - BUG只能对五个或五个以下长度 的列表做排序操作
"""

def shell_sort(_list):
    
    gap = int(len(_list) / 2)
    for i in range(gap):
        step_size = gap if gap > 0 else 1
        for j in range(gap, len(_list) - 1):
            now = _list[j + 1]
            for x in range(j - gap + 1, -1, -step_size):
                if now < _list[x]:
                    _list[j + 1] = _list[x]
                else:
                    x += step_size
                    break
            _list[x] = now
        gap = int(gap / 2)
    return _list



if __name__ == "__main__":
    _list = [2, 30, 7, 9, 11, 10, 12]
    print(shell_sort(_list))