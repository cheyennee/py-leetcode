#f(x) = f(x-1) + f(x-2)
#爬到第x级台阶的方案数就是爬到第x-1级台阶的方案数+爬到第x-2级台阶的方案数

#解法一：递归，不保存结果，超时
class Solution(object):
    def climbStairs(self, n):
        return self.climb_Stairs(0, n)
    def climb_Stairs(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_Stairs(i+1, n) + self.climb_Stairs(i+2,n)

#解法二：递归，保存结果，超时
class Solution(object):
    def climbStairs(self, n):
        memo = [0]*n
        return self.climb_Stairs(0, n, memo)
    
    def climb_Stairs(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        memo[i]=self.climb_Stairs(i+1,n,memo)+self.climb_Stairs(i+2,n,memo)
        return memo[i]

#解法三：动态规划，时间92，内存12
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return n
        memo = [0]*(n+1)
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n+1):
            memo[i] = memo[i-1]+memo[i-2]
        return memo[-1]

    
