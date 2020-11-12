
#解法一：暴力法，时间：94，内存19
#踩坑：关于append和extend.虽然在MLIA中已经知道它们有区别，但是还是入坑了。
#append:后面可以直接(数字/字符串/...)任意字符串，extend：后面只能接收list

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        locationM = []
        locationN = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    locationM.append(i)
                    locationN.append(j)
        locationM = set(locationM)
        locationN = set(locationN)
        for i in range(m):
            if i in locationM:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if j in locationN:
                for i in range(m):
                    matrix[i][j] = 0


        
#解法二：对解法一的改进，我觉得时间应该更短的，但是时间：83，内存17
#整个性能完全下降了-^-。想了一下好像也有道理，解法二遍历了所有元素，但是解法一遍历时先对元素进行了筛选
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        locationM = []
        locationN = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    locationM.append(i)
                    locationN.append(j)
        locationM = set(locationM)
        locationN = set(locationN)
        for i in range(m):
            for j in range(n):
                if i in locationM or j in locationN:
                    matrix[i][j] = 0


#解法三：抄的，我觉得很妙，可是为什么时间和内存都一言难尽，时间68，内存17
#先记录第一行第一列是否有0，如果有则标记。然后遍历清除非第一行和第一列的数据，最后根据标记清除第一行和第一列
#是原地算法，巧妙的借用第一行和第一列
#踩坑：清除时，要先清除非第一行第一列。若同时清除第一行和第一列，在[[0,1,2,0],[3,4,5,2],[1,3,1,5]]这种情况下，会出错，会得到全零的list
class Solution(object):
    def setZeroes(self, matrix):
        isRowZero = False
        isColZero = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                isRowZero = True
        for i in range(n):
            if matrix[0][i] == 0:
                isColZero = True
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if isRowZero == True:
            for i in range(m):
                matrix[i][0] = 0
        if isColZero == True:
            for i in range(n):
                matrix[0][i] = 0
