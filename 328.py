#解法一：常规解法，遍历，然后摘节点，时间96，内存41
class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        i = 1
        cur= head
        pahead = ListNode(0)
        pbhead = ListNode(1)
        pa, pb = pahead, pbhead
        while cur:
            if i%2 == 1:
                pa.next = cur
                pa = pa.next
            else:
                pb.next = cur
                pb = pb.next
            cur = cur.next
            i += 1
        pb.next = None
        pa.next = pbhead.next
        head = pahead.next
        return head

#解法一：官方题解
#又是别人的代码更优雅系列
class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        evenHead = head.next
        odd, even = head, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
    
