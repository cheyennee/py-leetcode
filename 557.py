#解法一：API怪出现了，时间74，内存14
#一行代码真是太舒服了
class Solution(object):
    def reverseWords(self, s):
        return " ".join(part[::-1] for part in s.split(' '))

#剩下的解法就只有拆分单词然后反转了，我觉得没必要，自己写的还不如API呢
