"""
    merge_sort.py   归并排序
"""


def merge_sort(_list):
    if len(_list) <= 1:
        return _list
    _mid = len(_list) // 2
    left_list = merge_sort(_list[:_mid])
    right_list = merge_sort(_list[_mid:])
    result = []
    if left_list and right_list:
        while len(left_list) > 0 and len(right_list) > 0:
            result.append(left_list.pop(0)) if left_list[0] <= right_list[0] else result.append(right_list.pop(0))
    result += left_list
    result += right_list
    return result


if __name__ == '__main__':
    _l = [1, 2, 3, 4, 222, 3, 4, 6, 99]
    print(merge_sort(_l))
