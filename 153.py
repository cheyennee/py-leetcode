#在我还没有看其他解法之前，我觉得这题很s
#解法一：遍历，时间63，内存19
#时间复杂度on
class Solution(object):
    def findMin(self, nums):
        length = len(nums)
        for i in range(1, length):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]

#解法二：在我看到解法二的时候，这个题好题啊
#二分法，没想到吧，这种题还能用二分法，而且官方解答不屑写遍历
#时间85，内存5
#时间复杂度为ologn
'''
当数组最右边的元素>数组第一个元素时，说明没有进行翻转，直接返回第一个元素
寻找一个mid点，在这个点附近发生了翻转
如果mid点<数组第一个元素，则需要在mid左边搜索变化点
如果mid点>数组第一个元素，则需要在mid右边搜索变化点
我觉得上述结论都需要证明一下，这时候就体现了形式化方法的作用(狗头
'''
class Solution(object):
    def findMin(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]
        left, right = 0, length-1
        #没有发生旋转
        if nums[left] < nums[right]:
            return nums[0]
        while left<=right:
            mid = left + (right-left)/2
            #这两种情况对应的是旋转中心的值<旋转中心前一个元素的值
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            
            if nums[mid]>nums[0]:
                left = mid+1
            else:
                right = mid-1
