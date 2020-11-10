'''
解法一：内存消耗大，速度快96
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            if target == nums[i]:
                return i
            if target < nums[i]:
                return i
        return length


'''
解法二：想采用二分法，但是代码写得太烂了，导致执行时间41.09，内存消耗5.10
'''
class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1
        if (left == len(nums)):
            return left
        elif (right == -1):
            return 0
        return left

'''
解法三：标准的二分法，可是执行时间：41.09，内存消耗：12.38
所以是因为py天生慢？
'''
class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1
        return left
