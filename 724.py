
'''
核心思想是判断当前索引i是否满足leftsum == s - nums[i] - leftnum
'''


class Solution(object):
    def pivotIndex(self, nums):
        s = sum(nums)
        leftnum = 0
        for i,x in enumerate(nums):
            if(leftnum == s - x - leftnum):
                return i
            leftnum += x
        return -1
