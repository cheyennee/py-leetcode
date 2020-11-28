#解法一：遍历求长度后拼接，用了快慢指针，自己写的，时间98，内存34
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return None
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        k = k % length
        if not k or k == length:
            return head
        fast = head
        for i in range(k):
            fast = fast.next
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        newHead = slow.next
        slow.next = None
        slow = newHead
        while slow.next:
            slow = slow.next
        slow.next = head
        return newHead
