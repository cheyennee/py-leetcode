#解法一：动态规划，时间32，内存12
class Solution(object):
    def getRow(self, rowIndex):
        result = [[1]]
        for i in range(1, rowIndex+1):
            temp = [1]
            for j in range(1, i):
                temp.append(result[i-1][j]+result[i-1][j-1])
            temp.append(1)
            result.append(temp)
        return result[rowIndex]

#解法二：修改之后的动态规划，时间83，内存5
#真的很奇怪，这次我用的一维数组，可是内存竟然比刚刚的二维数组低
class Solution(object):
    def getRow(self, rowIndex):
        result = [1]
        for i in range(1, rowIndex+1):
            temp = [1]
            for j in range(1, i):
                temp.append(result[j]+result[j-1])
            temp.append(1)
            result[:] = temp
        return result

#解法三：使用公式，抄的。时间99，内存13
#规律：第N行每个值为：后一个值等于前一个值乘以(n-i)*i
class Solution(object):
    def getRow(self, rowIndex):
        result = []
        numRows = rowIndex + 1
        for i in range(0, numRows):
            if i == 0:
                result.append(1)
            else:
                eachValofRows =result[i-1]*(numRows-i)/i
                result.append(eachValofRows)
        return result

    
