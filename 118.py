#解法一：暴力法，时间92，内存5
#大一对于杨辉三角的题逻辑写得真的很混乱，现在几分钟就写出来了，还是有点长进的吧
#看了题解才知道原来这种方法是动态规划(狗头
class Solution(object):
    def generate(self, numRows):
        if not numRows:
            return []
        result = [[1]]
        for i in range(1, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(result[i-1][j]+result[i-1][j-1])
            temp.append(1)
            result.append(temp)
        return result

