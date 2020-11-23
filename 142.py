#解法一：哈希，时间54，内存5
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None

#解法二：快慢指针，时间30，内存17
#不明白这样做的数学道理-^-
    
class Solution(object):
    def detectCycle(self, head):
        fast, slow, res = head, head, head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if flag:
                res = res.next
            if slow == fast:
                flag = True
            if flag and slow == res:
                return res
        return None

