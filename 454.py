#解法一：哈希+分组，抄的，时间38，内存85
#总结：看到形如A+B+...+N=0的式子，可转换为(A+..+T)=-(T+1+...+N)
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        countAB = collections.Counter(u+v for u in A for v in B)
        ans = 0
        for u in C:
            for v in D:
                if -u-v in countAB:
                    ans += countAB[-u-v]
        return ans

