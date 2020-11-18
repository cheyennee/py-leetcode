#解法一：快慢指针，时间39，内存24
class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k

#解法二：也是快慢指针，只不过进行了优化，将要删除的元素与最后一个元素进行交换，去除了不必要的复制
#时间67，内存5

class Solution(object):
    def removeElement(self, nums, val):
        length = len(nums)
        i = 0
        while i<length:
            if nums[i] == val:
                nums[i] = nums[length-1]
                length -= 1
            else:
                i += 1
        return i
