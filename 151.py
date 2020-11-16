#解法一：时间98，内存84.这绝对是做的最快，而且效率最高的一个程序了。
#调包大法好(狗头
class Solution(object):
    def reverseWords(self, s):
        #split()踩坑，刚开始用的split(' '),后来发现这个只能匹配一个空格的情况
        listarr = s.strip().split()
        listarr = listarr[::-1]
        result = ""
        length = len(listarr)
        for i in range(length):
            if i != length-1:
                result+=listarr[i]+" "
            else:
                result +=listarr[i]
        return result


#解法二：python大法好。看到答案这个python写法的简略，我我我...
#好奇怪啊，同样的代码提交三次时间和内存还不同
#时间98，内存85
class Solution(object):
    def reverseWords(self, s):
        return " ".join(reversed(s.split()))


#解法三：按照常规写法做。时间44，内存84
'''
1.去除字符串中首尾空格，去除字符串中间多余空格
2.翻转字符串
3.将每个单词翻转
'''
class Solution(object):
    def trim_spaces(self, s):
        left, right = 0, len(s)-1
        while left <= right and s[left]==' ':
            left += 1
        while left <= right and s[right]==' ':
            right -= 1
        current = []
        while left <= right:
            if s[left] != ' ':
                current.append(s[left])
            elif current[-1] !=' ':
                current.append(s[left])
            left += 1
        return current
    def reverse(self, l, left, right):
        while left<right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
    def reverse_each_word(self, l):
        right = len(l)
        start, end = 0
        while start < right:
            while l[end] != ' ' and end < n:
                end+=1
            self.reverse(l, start, end-1)
            start = end+1
            end += 1
    def reverseWords(self, s):
        l = self.trim_spaces(s)
        reverse(l, 0, len(l)-1)
        reverse_each_word(l)
        return ''.join(l)


#解法四：双端队列，本质思想其实与解法三一样，只是最后利用了队列的性质，简化了翻转操作
#时间57，内存31
class Solution():
    def reverseWords(self, s):
        left, right = 0, len(s)-1
        while left <= right and s[left]==' ':
            left += 1
        while left <= right and s[right]==' ':
            right -= 1
        d, word = collections.deque(), []
        while left <= right :
            if s[left] != ' ':
                word.append(s[left])
            elif s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word=[]
            left += 1
        d.appendleft(''.join(word))
        return ' '.join(d)
