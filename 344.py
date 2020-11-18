#运用双指针的场景：从两端向中间迭代数组


#解法一：还是API怪哈哈哈，时间88，内存5
#没错就一行
#踩坑，如果写成s=s[::-1]则不改变字符串，写s[:]=s[::-1]才改变字符串
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

#解法二：双指针，时间88，内存48.我一直以为API应该采用的解法比这种方法好，可是...
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left +=1
            right -= 1

