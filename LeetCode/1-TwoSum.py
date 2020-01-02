"""
    TwoSum.py 两数之和
    给定一个 Int 数组，返回两个数字的 索引 使得两数之和等于一个特定的数。

    例: 
        array = [2, 7, 11, 15] target = 9
        return [0, 1]  // 因为 arry[0] + arry[1] = 9
"""

def twoSum(nums : list, target: int) -> list:
    """暴力破解法

        寻找所有可能性，直到相加得出结果为止。

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    """

    """寻找另一个值

        target - x = y
        list.index(y) : 获得 y的索引
        list.count(y) : 判断是否有多个y

        for i in range(len(nums) - 1):
            num2 = target - nums[i]
            if num2 in nums and nums.index(num2) != i or nums.count(num2) > 1:
                return [i, nums.index(num2, i + 1)]
        return []
    """

    dict_nums = {}
    for i, v in enumerate(nums):
        if target - v in dict_nums:
            return [dict_nums[target - v], i]
        else:
            dict_nums[v] = i
    return[]

if __name__ == "__main__":
    test = {"array": [3, 3], "target": 6}
    re = twoSum(test["array"], test["target"])
    print(re)