"""
    bubble_sort.py
    冒泡排序 V0.1
"""


def bubble_sort(_list, reverse=False):
    """
        冒泡排序
    :param _list: 需要排序的列表
    :param reverse: 是否倒序，True为倒序
    :return: 返回列表
    """
    _len = len(_list)
    for i in range(_len - 1):
        count = 0
        for j in range(_len - i - 1):
            if reverse:
                if _list[j] < _list[j + 1]:
                    _list[j], _list[j + 1] = _list[j + 1], _list[j]
                    count += 1
            else:
                if _list[j] > _list[j + 1]:
                    _list[j], _list[j + 1] = _list[j + 1], _list[j]
                    count += 1
        if count == 0:
            return _list  # 最优情况 / _len() - 1 为有序列表

    return _list


if __name__ == "__main__":
    _list = [11, 4, 78, 5, 9, 20, 1, 69, 99]
    list_ = bubble_sort(_list)
    print(list_)
    
