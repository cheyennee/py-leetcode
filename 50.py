#我以为它是青铜，没想到是个强者555

#解法一：暴力，可是超过了数能表示的范围，最后输入0.0000001, 2456
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1:
            return x
        elif n == -1:
            return 1/x
        pown = abs(n)
        sum = 1
        for i in range(0, pown):
            sum *= x
        return sum if n > 0 else 1/sum

#解法二：递归快速幂，时间85，内存20
class Solution(object):
    def myPow(self, x, n):
        
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y*y*x
        
        return quickMul(n) if n>=0 else 1.0 / quickMul(-n)

#解法三：迭代快速幂，时间85，内存31
#这种解法简直是妙蛙种子吃着妙脆角妙进了米奇妙妙屋妙到家了
class Solution(object):
    def myPow(self, x, n):
        
        def quickMul(N):
            ans = 1.0
            x_contribute = x
            while N > 0:
                if N % 2 == 1:
                    ans *= x_contribute
                x_contribute *= x_contribute
                N //= 2
            return ans
        
        return quickMul(n) if n>=0 else 1.0 / quickMul(-n)

