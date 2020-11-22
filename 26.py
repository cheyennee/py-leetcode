#解法一：双指针，时间83，内存9
class Solution(object):
    def removeDuplicates(self, nums):
        length = len(nums)
        k = 0
        for i in range(1, length):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k+1

