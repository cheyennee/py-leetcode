#解法一：迭代，自己写的，时间86，内存18
#第一次提交的时候不通过，是因为忘记修改两组数据之间的指针了
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        temp = head.next
        dummy = ListNode(0, head)
        prev, cur = head, head.next
        while True:
            prev.next = cur.next
            cur.next = prev
            prev, cur = cur, prev
            dummy.next = prev
            if prev.next.next and cur.next.next:
                dummy = dummy.next.next
                prev = prev.next.next
                cur = cur.next.next
            else:
                break
        return temp

#解法二：递归，抄的，在知道思路下自己写的，时间38，内存9
#思路：将2指向1，1指向下一层的递归函数，最后返回节点2
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        newhead = head.next
        head.next = self.swapPairs(newhead.next)
        newhead.next = head
        return newhead

