#解法一：列表，时间81，内存7
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if (s and not t) or (not s and t):
            return False
        sList = [0]*26
        tList = [0]*26
        for i in range(len(s)):
            #踩坑，python与c++不同，不可以直接字符-字符，必须使用ascii相减
            sList[ord(s[i])-ord('a')] += 1
            tList[ord(t[i])-ord('a')] += 1
        for i in range(26):
            if sList[i] != tList[i]:
                return False
        return True

#解法二：API,时间17，内存73
#这是collections里面的api，counter只要用于计算每个字符出现的次数
class Solution(object):
    def isAnagram(self, s, t):
        c1 = Counter(s)
        c2 = Counter(t)
        if c1 == c2:
            return True
        return False

#解法三：排序，时间51，内存40
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        #python中没有字符串内字符排序的方法，需转换成列表
        s = list(s)
        s.sort()
        s = "".join(s)
        t = list(t)
        t.sort()
        t = "".join(t)
        if s != t:
            return False
        return True


