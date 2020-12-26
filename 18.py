#解法一：排序+双指针，抄的，时间97，内存5
'''
思路：
假设两重循环枚举到的前两个数分别位于下标i和j，其中i<j。初始时，左右指针分别指向下标j+1和下标n-1。
剪枝操作：
在确定第一个数之后，如果 {nums}[i]+{nums}[i+1]+{nums}[i+2]+{nums}[i+3]>target，说明此时剩下的三个数无论取什么值，四数之和一定大于target，因此退出第一重循环；
在确定第一个数之后，如果 {nums}[i]+{nums}[n-3]+{nums}[n-2]+{nums}[n-1]<target，说明此时剩下的三个数无论取什么值，四数之和一定小于target，因此第一重循环直接进入下一轮，枚举 {nums}[i+1]；
在确定前两个数之后，如果 {nums}[i]+{nums}[j]+{nums}[j+1]+{nums}[j+2]>target，说明此时剩下的两个数无论取什么值，四数之和一定大于target，因此退出第二重循环；
在确定前两个数之后，如果 {nums}[i]+{nums}[j]+{nums}[n-2]+{nums}[n-1]<target，说明此时剩下的两个数无论取什么值，四数之和一定小于target，因此第二重循环直接进入下一轮，枚举{nums}[j+1]
'''
class Solution(object):
    def fourSum(self, nums, target):
        quadruplets = []
        if not nums or len(nums) < 4:
            return quadruplets
        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            #去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if nums[i]+nums[length-3]+nums[length-2]+nums[length-1]<target:
                continue
            for j in range(i+1, length-2):
                #去重
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                #剪枝
                if nums[i]+nums[j]+nums[j+1]+nums[j+2]>target:
                    break
                #剪枝
                if nums[i]+nums[j]+nums[length-2]+nums[length-1]<target:
                    continue
                left, right = j+1, length-1
                while left < right:
                    total = nums[i]+nums[j]+nums[left]+nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        #去重
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        left += 1
                        while left<right and nums[right]==nums[right-1]:
                            right -= 1
                        right -= 1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return quadruplets

