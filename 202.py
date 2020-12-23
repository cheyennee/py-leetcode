#解法一：hash，时间92，内存5
#踩坑啦，我自己第一次写的卡过测试用例401/402（狗头
#但是就是想错了，我刚开始想的循环结束的条件是，当最后只有一个数字的时候，可是并不是这样子的
'''
思路:
最终结果有两种：
1.最后到达1
2.进入循环
'''
class Solution(object):
    def isHappy(self, n):
        sum = 0
        seen = []
        while n!=1:
            while n:
                sum += pow(n%10, 2)
                n /= 10
            n = sum
            sum = 0
            #修改了这个地方就过了
            if n in seen:
                return False
            else:
                seen.append(n)
        return True

#解法二：快慢指针，时间58，内存16
#这题快慢指针的写法真的是绝了，好厉害
class Solution(object):
    def isHappy(self, n):
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        #绝了
        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            #为什么它不会错过1呢？因为当它到达1的时候，无论它再走几步，都是1
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

