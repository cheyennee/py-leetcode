#解法一：双指针，时间92，内存12，但是我感觉好像我写的这个过于麻烦了
class Solution(object):
    def moveZeroes(self, nums):
        length = len(nums)
        k = 0
        for i in range(length):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k, length):
            nums[i] = 0


#解法二：左右指针，时间92，内存8，官方的这个左右指针写的巧妙一点
class Solution(object):
    def moveZeroes(self, nums):
        length = len(nums)
        k = 0
        for i in range(length):
            if nums[i] != 0:
                #当前左指针指向的元素是0，所以可以与右指针交换而不改变顺序
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
