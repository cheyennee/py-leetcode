#解法一：常规解法，时间75，内存17
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0, head)
        pre = dummy
        while head:
            if head.val == val:
                pre.next = head.next
                head = pre.next
            else:
                pre = pre.next
                head = head.next
        return dummy.next

#解法二：递归，时间6，内存5
#感觉用递归解决的题目都好巧妙啊，也就是说链表很多题目是可以用递归解决的？
#永远不会写递归系列QAQ
#常常因为菜而看不懂题解
class Solution(object):
    def removeElements(self, head, val):
        #边界条件
        if not head:
            return None
        #递归最深处，但是还是很理不清这个逻辑
        #假设前面的节点都已经处理完了，现在该处理当前节点
        #如果当前节点的值与val相同，则返回下一个节点的值，否则返回当前节点？
        #妙啊
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
