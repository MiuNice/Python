"""
    selection_sort.py
    选择排序 V0.1
"""


def selection_sort(_list, reverse=False):
    """
        选择排序
    :param _list: 待排序的列表
    :param reverse: 是否倒序，True为倒序
    :return: 返回有序列表
    """
    for i in range(len(_list) - 1):
        _index = i
        for j in range(i + 1, len(_list)):
            if reverse:
                if _list[_index] < _list[j]:
                    _index = j
            else:
                if _list[_index] > _list[j]:
                    _index = j
        _list[i], _list[_index] = _list[_index], _list[i]
    return _list


if __name__ == '__main__':
    _list = [11, 4, 78, 5, 9, 20, 1, 69, 99]
    list_ = selection_sort(_list)
    print(list_)
