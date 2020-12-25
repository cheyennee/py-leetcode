#解法一：双指针，抄的别人的解法，时间78，内存54
'''
思路：这题的重点在于去重。本身可以用三重循环，但是必须优化。

1.特判。
2.对数组进行排序。
3.遍历排序后数组：
3.1 若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于0，直接返回结果。
3.2对于重复元素：跳过，避免出现重复解
3.3令左指针 L=i+1，右指针 R=n-1，当 L<R 时，执行循环：
3.3.1当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
3.3.2若和大于 0，说明 nums[R]太大，R左移
3.3.3若和小于 0，说明 nums[L]太小，L右移

'''
class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        res = []
        if not nums or n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n):
            #证明后面的元素都是大于0了，也就是没有符合题意的解了，返回
            if nums[i] > 0:
                return res
            #跳过重复元素
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    #跳过重复的元素
                    while L<R and nums[L] == nums[L+1]:
                        L = L + 1
                    while L<R and nums[R] == nums[R-1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R = R - 1
                else:
                    L = L + 1
        return res

