#解法一：快慢指针，时间45，内存32，对链表有点不太熟，写的时候卡顿了
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        left, right = head.next, head.next
        while left != None and right != None:
            if not left.next:
                return False
            else:
                left = left.next
            if not right.next:
                return False
            else:
                right = right.next.next
            if left == right:
                return True
        return False


#解法二：哈希，时间45，内存6，这种方法也太简洁了555
#如果
class Solution(object):
    def hasCycle(self, head):
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
