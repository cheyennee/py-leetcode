#解法一：暴力，超时
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums:
            return False
        ordermap = {}
        for index, num in enumerate(nums):
            ordermap[index] = num
        ordermap.sort()
        for i in range(length):
            for j in range(i+1,length):
                if abs(nums[i]-nums[j]) <= t and abs(i-j) <= k:
                    return True
        return False

#解法二：桶排序，时间43，内存26，我不是很理解
'''
思路：
将数据分到M个桶中
每个数字nums[i]都被分配到桶中，分配的依据是nums[i]//(t+1)
这样的话
1.相邻桶里的数字最多相差2*t+1
2.不相邻的桶一定不满足相差小于等于t
3.同一个桶内的数字最多相差t
由于题目中有索引相差k的要求，因此要维护一个大小为k的窗口，定期清除桶中过期的数字
'''
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        bucket = {}
        if t<0:
            return False
        for i in range(len(nums)):
            nth = nums[i] // (t+1)
            if nth in bucket:
                return True
            if nth - 1 in bucket and abs(nums[i] - bucket[nth-1]) <= t:
                return True
            if nth + 1 in bucket and abs(nums[i] - bucket[nth+1])<=t:
                return True
            bucket[nth] = nums[i]
            if i >= k:
                bucket.pop(nums[i-k]//(t+1))
        return False


