"""
    MonkeySort.py 猴子排序
    检测是否排序好，若没有则打乱，重复这个过程。
"""

import random, time

def monkey_sort(_list):
    num = 0
    while not is_sort(_list):
        random.shuffle(_list)
        num += 1
    else:
        return _list, num

def is_sort(_list):
    for i in range(len(_list) - 1):
        if _list[i] <= _list[i + 1]:
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    start = time.time()
    _list = [1, 3, 61 ,1, 5, 7, 2, 9, 0, 1]
    r_list, num = monkey_sort(_list)
    print(r_list)
    print("总用时", time.time() - start, "共尝试了", num, "次")
    