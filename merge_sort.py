import random


def merge_sort(_list):
    if len(_list) <= 1:
        return _list
    _mid = len(_list) // 2
    _left = _list[:_mid]
    _right = _list[_mid:]

    left_list = merge_sort(_left)
    right_list = merge_sort(_right)

    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    return result


if __name__ == '__main__':
    _l = []
    for i in range(10000000):
        _l.append(random.randint(1, 100000))
    import time

    st = time.time()
    print(merge_sort(_l))
    print(time.time() - st)
