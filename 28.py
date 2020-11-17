#解法一：API怪又来了heihei时间78，内存13
#此处需要注意的是，find与Index的区别
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not str:
            return 0
        else:
            return haystack.find(needle)


#解法二：类似暴力，但是有做优化，称为双指针。时间97，内存54
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        L, n = len(needle), len(haystack)
        pn = 0
        #字符串比较算法其实都可以这么优化来缩短比较次数
        while pn < n - L + 1:
            while pn<n-L+1 and haystack[pn]!=needle[0]:
                pn += 1
            curr_len = pL = 0
            while pL<L and pn<n and haystack[pn] == needle[pL]:
                pL += 1
                pn += 1
                curr_len += 1
            if curr_len == L:
                return pn-curr_len
            pn = pn - curr_len + 1
        return -1

#解法三：抄的，rabin karp算法。时间43，内存15
#思想：先生成窗口内子串的hash值，然后与needle的hash值做比较，如果相同则相等
#但是有溢出的危险，而且如何生成子串的hash值呢？
'''
1.a**L可能是个很大的数，会导致上溢。可以使用取模操作实现
(但是实际上取模操作可能会导致有多种子串的hash值与needle相同，但其与needle并不相同
2.题解所采用的生成hash值的方法是：arr[i] = (int)s.charat(i)-(int)'a'
因为题解假设只出现小写字母，但是实际上题目并没有说只出现小写字母
然后根据h0=0*26^3+1*26^2+2*26^1+3*26^0这样子去计算hash值
'''
class Solution:
    def strStr(self, haystack, needle):
        L, n = len(needle), len(haystack)
        if L > n:
            return -1
        a = 26
        modulus = 2**31
        #计算每个字符的hash值
        h_to_int = lambda i : ord(haystack[i])-ord('a')
        needle_to_int = lambda i :ord(needle[i]) - ord('a')
        #计算haystack[:L], needle[:L]的hash值
        #Q:为什么不跟0这个位置的hash值不跟后面一起计算呢？
        #A:因为要得到needle的hash值。或者可以在后面循环中使用判断来单独计算，但是会消耗更多时间
        h = ref_h = 0
        for i in range(L):
            h = (h*a+h_to_int(i))%modulus
            ref_h = (ref_h*a+needle_to_int(i))%modulus
        if h == ref_h:
            return 0
        #计算a**L%modulus
        aL = pow(a, L, modulus)
        #计算滑动窗口内的hash值与needle的hash值的差别
        for i in range(1, n-L+1):
            #注意此处减去的是h_to_int*aL,而不是h_to_int，因为进行了取模操作
            h = (h*a-h_to_int(i-1)*aL+h_to_int(i+L-1))%modulus
            if h == ref_h:
                return i
        return -1
