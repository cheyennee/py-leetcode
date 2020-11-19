#解法一：万物唯我暴力法独尊。官方的代码说卡不过，我自己写的竟然卡过了，哈哈哈
#时间5，内存5，辣鸡
class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        length = len(nums)
        ans = length+1
        sumnum = 0
        i, j = 0, 0
        flag = 0
        for i in range(length):
            sumnum = nums[i]
            if sumnum >= s:
                ans = 1
                break
            for j in range(i+1,length):
                sumnum += nums[j]
                if sumnum >= s:
                    flag = 1
                    ans = min(ans, j-i+1)
                    break
        if sumnum >= s:
            flag = 1
            ans = min(ans, j-i+1)
        if flag:
            return ans
        else:
            return 0

#解法一：修改一下
class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        length = len(nums)
        ans = length+1
        sumnum = 0
        i, j = 0, 0
        for i in range(length):
            sumnum = nums[i]
            if sumnum >= s:
                ans = 1
                break
            for j in range(i+1,length):
                sumnum += nums[j]
                if sumnum >= s:
                    ans = min(ans, j-i+1)
                    break
        if sumnum >= s:
            ans = min(ans, j-i+1)
        return 0 if ans == length+1 else ans

#解法二：双指针，时间95，内存51，我自己写的时候逻辑混乱的一批
#当sum<s时，end++;当sum>=s时，start++
#不理解为什么这个时间复杂度是on
#感觉暴力法跟双指针，好像有那么一点像，同样是两个指针，但是前者是后面的指针慢慢悠悠的变化，前面的遍历所有可能的情况，前面的指针会重复很多次，所以浪费
#而双指针前面的指针没有重复做无差别的劳动，就节省了很多时间
class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        n = len(nums)
        ans = n+1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end-start+1)
                total -= nums[start]
                start+=1
            end+=1
        return 0 if ans == n+1 else ans

#解法三：前缀+二分，时间51，内存5
#前缀有点类似贪心，先用一个数组保存nums[0]-nums[i]的和，再用二分去找值
class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        n = len(nums)
        ans = n+1
        sums = [0]
        for i in range(n):
            #这种技巧用一次用到了
            sums.append(sums[-1]+nums[i])
        for i in range(1, n+1):
            #sums[bound]-sums[i-1]>=s
            target = s+sums[i-1]
            #bisect.bisect_left:用于查找大于等于某一个的第一个位置
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound-(i-1))
        return 0 if ans == n+1 else ans

