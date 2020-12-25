#解法一：时间5，内存16
class Solution(object):
    def frequencySort(self, s):
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic.keys():
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        #踩坑，这个排序返回的竟然是列表,[('e', 2),('t', 1)]
        #而且如果将转换后的列表强转成字典，那么会破坏它的排序
        dic = sorted(dic.items(), key = lambda x:x[1], reverse = True)
        result = ""
        for i in dic:
            for j in range(i[1]):
                result += i[0]
        return result


#解法二：时间53，内存14，官方的解法，我没有看懂？它在说啥？
class Solution:
    def frequencySort(self, s):
        n = len(s)
        #counter返回的是有序的({}),将其dict一下就变成无序的了
        sc = dict(Counter(s))
        ll = ['' for i in range(0, n+1)]
        ret = ""
        for key,value in sc.items():
                ll[value] += key * value
        for i in range(n, -1, -1):
            if ll[i] != '':
                ret += ll[i]
        return ret


#解法三：网友的解法，时间66，内存49
class Solution:
    def frequencySort(self, s):
        return ''.join([i * j for i, j in collections.Counter(s).most_common()])

