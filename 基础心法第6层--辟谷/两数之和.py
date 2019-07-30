def twoSum(nums, target):
    res = {}
    for i, n in enumerate(nums):
        if n in res:
            return [res[n], i]
        res[target - n] = i


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
