#解法一：万事可暴力(不是。时间：74，内存：5. u1s1，这个内存是很恐怖了
#主要是先找出最短的子串，然后依据最短子串去遍历每个字符串.在暴力法上有一点简化.

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs or not strs[0]:
            return ''
        index = 0
        minele = len(strs[0])
        length = len(strs)
        for i in range(1, length):
            if len(strs[i]) < minele:
                minele = len(strs[i])
                index = i
        for i in range(minele):
            temp = strs[index][:i+1]
            for j in range(length):
                if strs[j][:i+1] != temp:
                    return strs[index][:i]
        return strs[index]

#解法二：官方解法，时间28，内存7.时间出奇的低是我没想到的
#主要思想：LCP(S1, S2, S3...SN) = LCP(LCP(LCP(S1, S2), S3), ... SN).有点选择排序内味了
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        return prefix
    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

#解法三：官方解法，纵向比较，相当于也是暴力法。我以为时间会出奇的低，结果跟我写的差不多(狗头
#时间：74，内存5
#解法二和解法三都没有借鉴的地方，但是太符合人类的思维了

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            #这行代码还是可以借鉴的(狗头
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        return strs[0]

#解法四：官方解法，分治法，可是效率极低，时间28，内存5，可能跟它递归有关系

class Solution(object):
    def longestCommonPrefix(self, strs):
        def lcp(start, end):
            if start == end:
                return strs[start]
            
            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid+1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]
            return lcpLeft[:minLength]
        return ("" if not strs else lcp(0, len(strs) - 1))

#解法五：官方解法，二分法。在我的解法一的基础上，对于前缀搜索进行了改进。主要是按照最短子串的长度进行二分搜索。时间91，内存5
class Solution(object):
    def longestCommonPrefix(self, strs):
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))
        if not strs:
            return ''
        #此行代码可以参考，毕竟自己写的时候搞复杂了
        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high :
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1
        return strs[0][:low]
