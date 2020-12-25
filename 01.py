#解法一：时间65，内存63
class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return i, j
        return -1, -1

#解法二：构建查找表，时间91，内存91
#这个解法我有想到target-nums[i]，但是没有想到具体怎么做，果然还是题写得不够
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        if n < 2:
            return []
        dict1 = {}
        for i in range(n):
            other = target - nums[i]
            if other in dict1:
                return [dict1[other], i]
            dict1[nums[i]] = i
        return []

