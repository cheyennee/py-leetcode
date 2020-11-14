#解法一：抄的。自己写的过于麻烦，主要是把循环写麻烦了。
#时间99，内存45
#主要思路是简化问题。首先考虑按照逐条对角线打印元素，而不考虑翻转的情况。对结果中的数组的奇数条对角线进行翻转
#踩坑：matrix=[]时，matrix[0]会报错
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        n, m = len(matrix), len(matrix[0])
        result, intermediate = [], []
        for d in range(n + m -1):
            intermediate.clear()
            #r, c = 0 id d<m else d-m+1, d if d<m else m-1
            #妙在此处的判断条件
            if d<m:
                r = 0
                c = d
            else:
                r = d-m+1
                c = m -1
            while r<n and c>-1:
                intermediate.append(matrix[r][c])
                r+=1
                c-=1
            if d%2 == 0:
			#此处的翻转也很巧妙
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result


#解法二：模拟当前行列的位置。为了实现模拟，需要明确1.对角线的走向 2.确定对角线的起点元素
#1.使用direction记录对角线的走向
#2.找出向上对角线的头部：如果当前尾部不在矩阵最后一行，则下一个对角线的头部是当前尾部的正下方元素；
#否则下一条对角线首部是当前尾部的右边元素
#找出向下对角线的头部：如果当前尾部不在矩阵最后一行，下一条对角线的首部是当前尾部正下方元素；
#否则下一条对角线首部是当前尾部的右边元素
#时间99，内存20.这种解法比较难想，但是实现起来逻辑还是很清晰的
    
class Solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        n, m = len(matrix), len(matrix[0])
        row, column = 0, 0
        direction = 1
        result = []
        while row < n and column < m:
            result.append(matrix[row][column])
            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)
            if new_row<0 or new_row == n or new_column<0 or new_column == m:
                #此解法妙就妙在此处
                #往上
                if direction:
                    row += (column == m-1)
                    column += (column < m-1)
                else:
                    column += (row == n-1)
                    row += (row<n-1)
                #此种写法可以借鉴，实现0\1之间的跳变
                    direction = 1 - direction
            else:
                row = new_row
                column = new_column
        return result
