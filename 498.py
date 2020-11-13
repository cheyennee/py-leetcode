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
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result


