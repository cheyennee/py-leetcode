#解法一：递归，时间5，内存16，消除了重复计算，可是还是很慢
class Solution(object):
    def fib(self, n):
        res = {}
        def helper(n):
            if n in res.keys():
                return res[n]
            if n < 2:
                result = n
            else:
                result = self.fib(n-1) + self.fib(n-2)
            res[n] = result
            return result
        return helper(n)

#解法二：迭代，时间34，内存15
class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        res = [0, 1]
        for i in range(2, n+1):
            #踩坑，刚开始直接写res[i]=res[i-1]+res[i-2]然后out of range hh
            res.append(res[i-1] + res[i-2])
        return res[-1]

