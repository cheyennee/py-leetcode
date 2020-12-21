#解法一：暴力法，超时了
class Solution(object):
    def kthGrammar(self, N, K):
        linelist = [0]
        for i in range(N):
            length = 2 * len(linelist)
            for j in range(0, length, 2):
                if linelist[j] == 0:
                    linelist.insert(j+1, 1)
                else:
                    linelist.insert(j+1, 0)
        return linelist[K-1]

#解法一：暴力法，官方解法，好优雅，可是还是超时
class Solution(object):
    def kthGrammar(self, N, K):
        rows = []
        lastrow = '0'
        while len(rows) < N:
            rows.append(lastrow)
            lastrow = ''.join('01' if x == '0' else '10'
                                for x in lastrow)
        return int(rows[-1][K-1])

#解法二：递归（父子递推），时间68，内存37，反正不是我能想出来的
'''
思路：
第K个数字是上一行第(K+1)/2个数字生成的
如果上一行的数字为0，则被生成的数字为1-k%2,如果上一行的数字为1，则被生成的数字为k%2

'''
class Solution(object):
    def kthGrammar(self, N, K):
        if N == 1:
            return 0
        return (1 - K%2) ^ self.kthGrammar(N-1, (K+1)//2)

#还有别的解法，可是我看不懂QAQ
