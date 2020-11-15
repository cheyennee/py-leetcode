#解法一：暴力法，虽然我也不想，可是我脑子里只有这一个方法，而且对它逐步修改
#但是很遗憾，还是超时了-^-代码应该是没有问题的。我麻了。
#官方题解中，Java使用暴力法可以通过，是我大py不配了...时间复杂度n^3
class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        length = len(s)
        maxlen = 0
        index = 0
        #一个改进点：i的范围
        for i in range(length-maxlen):
            for j in range(i, length):
                temp = s[i:j+1]
                temp=temp[::-1]
                if temp == s[i:j+1]:
                    if len(temp)>maxlen:
                        #另一个改进点：只保存长度和开始index，否则太消耗内存和时间
                        index = i
                        maxlen = len(temp)
        return s[index:index+maxlen]


#解法二：动态规划(表格法)，抄的。也差点超时。时间9，内存26
'''
dp解题步骤
1.状态：代表求解问题的某个阶段，一般用二维数组来保存历史状态(一般题目问什么，就把什么设置为状态)
2.状态转移方程：是原始问题的不同规模的子问题的联系
3.初始化：直接从语义出发或者考虑状态转移方程的边界
'''
#感觉好像也有点暴力法内味了，不过时间复杂度降了一个level，n^2
'''状态转移方程：
P(i, i) = true
p(i, i+1) = (si == si+1)
p(i, j) = p(i+1, j-1) && (si == sj)
'''
#注意循环的顺序。因为在状态转移方程中，是从长度较短的字符串向长度较长的字符串转移的

class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        #n*n的数组
        dp = [[False]*n for _ in range(n)]
        ans = ""
        #k表示字符串长度
        for k in range(n):
            for i in range(n):
                j = i + k
                if j >= len(s):
                    break
                if k == 0:
                    dp[i][j] = True
                elif k == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    #或许这就是表格法的好处，只用一步判断，而不用再写一个循环
                    #相当于是记录了前面的结果，不用重复计算
                    #如果再写一个循环，相当于重复计算了
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and k + 1 > len(ans):
                    ans = s[i:j+1]
        return ans

#我将解法二修改了一下，主要是减少了循环的次数，时间19，内存25
class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = ""
        for k in range(n):
            #修改的地方1
            for i in range(n-k):
                j = i + k
                #修改的地方2
                '''
                if j >= len(s):
                    break
                '''
                if k == 0:
                    dp[i][j] = True
                elif k == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and k + 1 > len(ans):
                    ans = s[i:j+1]
        return ans


#解法三：中心扩展法，抄的。属于动态规划的逆向，时间79，内存55
#动态规划从两边向中心，中心扩展从中心向两边扩展
#感觉这种方法比动态规划好理解一点
class Solution(object):
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right<len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1
    def longestPalindrome(self, s):
        start, end = 0, 0
        for i in range(len(s)):
            #考虑到中心奇偶的情况
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i+1)
            if right1-left1 > end-start:
                start, end = left1, right1
            if right2-left2 > end - start:
                start, end = left2, right2
        return s[start: end+1]


