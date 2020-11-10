
'''
本题易混点：1.循环结束条件:right>left 2.在nums[mid] == target可以不用判断
'''

'''
解法一：暴力法：内存15.55,运行时间66.97
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
增加了target == nums[mid]判断之后，若数组元素有重复，可能会出错
例如：[1,1,1,1,1]
增加此判断条件后，返回2，但实际应该返回0
'''


'''
解法二：想采用二分法，但是代码写得太烂了，导致执行时间41.09，内存5.10
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
解法三：在解法二的基础上修改了，执行时间：41.09，内存：12.38
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

'''
解法四：解法二的改进版，执行时间：96.8,内存：9.1
'''
class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = int((left + right) / 2)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


