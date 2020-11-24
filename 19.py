#当题目给出的链表没有头结点的时候，需要自己创建哑节点以保证操作的一致性

#解法一：快慢指针，时间28，内存6
#我抄的，我想到了使用dummy and 快慢指针，但是返回了head
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        left, right = dummy, head
        for _ in range(n):
            right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

#解法二：求出链表长度，第length-n+1就是我们要删除的元素
#时间97，内存33
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        cur = head
        while head:
            length += 1
            head = head.next
        head = cur
        dummy = ListNode(0, head)
        cur = dummy
        for _ in range(1, length-n+1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

#解法三：利用了栈(实际上这里使用的是list)，时间51，内存23，这种解法也很巧妙
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next
    
