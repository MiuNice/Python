def qiuck_sort(_list):
    if len(_list) <= 1:
        return _list
    _left = []
    _right = []
    base = _list.pop()
    for i in _list:
        if i >= base:
            _right.append(i)
        else:
            _left.append(i)
    return qiuck_sort(_left) + [base] + qiuck_sort(_right)


if __name__ == "__main__":
    _l = [1, 2, 3, 4, 222, 3, 4, 6, 99]
    print(qiuck_sort(_l))
