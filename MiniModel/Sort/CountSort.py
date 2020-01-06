"""
    CountSort.py 计数排序
    思想 : 找到最大值，建立一个长度为最大值的列表值都为0；
    将 index 抽象为元素的值， value 抽象为元素的个数。
    [2, 3, 1, 1, 2] -> [0, 2, 2, 1]
    将抽象后的列表 输出 -> [1, 1, 2, 2, 3]
"""

def count_sort(_list):
    _max = _list[0]
    _min = _list[0]
    for num in range(1, len(_list)):
        if _list[num] > _max:
            _max = _list[num]
        if _list[num] < _min:
            _min = _list[num]
    sort_list = [0 for x in range(_max - _min + 1)]
    for i in _list:
        sort_list[i - _min] += 1
    return [sort + _min for sort in range(len(sort_list)) for j in range(sort_list[sort])]


if __name__ == "__main__":
    _list = [2, 4, 6, 5, 9, 6, 1, 5, 7, 9]
    list_ = count_sort(_list)
    print(list_)