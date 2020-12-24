#解法一：字典，抄的，时间96，内存48
#自己写的思路有点混乱，卡在31/32的测试用例上了,aabb,abba
#这种解法妙就妙在它的键和值都是字符串，而我一直想的用次数当作值

class Solution(object):
    def isIsomorphic(self, s, t):
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]] = t[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True


#解法二：将两个字符串映射成一个中间串，再比较这个中间串是否相同
#时间5，内存44
#abb映射成112，egg映射成112
class Solution(object):
    def helper(self, s):
        dic = {}
        n = len(s)
        res = ""
        count = 1
        for i in range(n):
            #妙在映射的过程
            if s[i] not in dic.keys():
                dic[s[i]] = count 
                count += 1
            res += (str(dic[s[i]]))
        return res
    def isIsomorphic(self, s, t):
        return self.helper(s) == self.helper(t)

