"""
    insert_sort 插入排序
"""

def insert_sort(_list):
    for i in range(1, len(_list)):
        now = _list[i]
        for j in range(i - 1, -1, -1):
            if now < _list[j]:
                _list[j + 1] = _list[j]
            else:
                break
        _list[j + 1] = now
    return _list

if __name__ == "__main__":
    _list = [2, 30, 7, 9, 11, 4, 5, 9]
    print(insert_sort(_list))