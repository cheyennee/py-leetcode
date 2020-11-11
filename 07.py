#解法一：暴力法 时间：25，内存15
#解题思路：原来矩阵中第i行第j列元素，经过旋转后，变成倒数第i列第j个位置的元素
#踩坑：1.python二维数组的生成 2.注意matrix[:]=newmatrix1(matrix改变)与matrix=newmatrix1（matrix不变）的区别
'''
eg.
a=[1,2,3,4,5,6]
id(a)=280
a[:]=[1,6,9]
id(a)=280
a=[1,2,3]
id(a)=390
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        '''
        此种方法生成的数组，每一维实际指向同一个地址空间
        '''
        #newmatrix1 = [[0]*length] * length
        
        newmatrix1 = [[0 for _ in range(length)] for _ in range(length)]
        

        '''
        此种方法可生成正确的二维数组
        '''
        #newmatrix = [[0]*length for _ in range(length)]
        
        for i in range(length):
            for j in range(length):
                newmatrix1[j][length - i - 1] = matrix[i][j]
        matrix[:]=newmatrix1

#解法二：通过计算，得到元素之间的旋转关系
#原地算法，但是时间复杂度还是n^2,时间25，内存15
#通过计算，发现matrix[row][col],matrix[col][n-row-1]
#matrix[n-row-1][n-col-1],matrix[n-col-1][row]处于循环之中，前一项的值是后一项的值


class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range((n+1) // 2):
            for j in range(n // 2):
                matrix[i][j],matrix[n-j-1][i],matrix[n-i-1][n-j-1],matrix[j][n-i-1] = matrix[n-j-1][i],matrix[n-i-1][n-j-1],matrix[j][n-i-1],matrix[i][j]

#解法三：通过翻转代替旋转，时间复杂度为n^2,时间58，内存19

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n-i-1][j], matrix[i][j]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
