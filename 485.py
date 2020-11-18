#解法一：我想用双指针，我真的觉得我的代码没错，可是它卡在一个测试用例了sad
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        length = len(nums)
        maxlen = 0
        i = 0
        start = -1
        while i < length:
            if nums[i] == 1 :
                if start == -1:
                    start = i
            else:
                if start != -1 and maxlen < i - start:
                    maxlen = i-start
                    start = -1
            i += 1
        if start != -1 and maxlen < i-start:
            maxlen = i-start
        return maxlen


#解法二：无敌弱智，可是我没想出来？时间12，内存27
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)


#解法三：没看懂，专为py设计的解法
def findMaxConsecutiveOnes(self, nums):
  return max(map(len, ''.join(map(str, nums)).split('0')))


