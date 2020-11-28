#菜哭了，我真的没看懂题目的意思5555
#后来在评论里翻到了解释：把原来链表复制一份，在不更改原链表的情况下返回拷贝链表
#谢谢，有被侮辱到QAQ，菜字当头

#解法一：python API，时间46，内存5
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        return copy.deepcopy(head)

#解法二：暴力，时间5，内存48，基于对题目的理解，写的，我觉得好蠢的解法
#我的想法是，首先遍历一遍，复制节点的值，然后遍历一遍，复制random指针
#经过踩坑，我发现random不是数而是指向的节点
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        psudoHead = Node(head.val, None,None)
        dummy = Node(0,psudoHead,None)
        curr = head.next
        while curr:
            psudo = Node(curr.val, None, None)
            psudoHead.next = psudo
            psudoHead = psudoHead.next
            curr = curr.next
        curr = head
        currPsudo = dummy.next
        while curr:
            if curr.random == None:
                curr = curr.next
                currPsudo = currPsudo.next
                continue
            else:
                psudoHead = dummy.next
                curr1 = head
                while curr1!=curr.random:
                    curr1 = curr1.next
                    psudoHead = psudoHead.next
                currPsudo.random = psudoHead
                curr = curr.next
                currPsudo = currPsudo.next
        return dummy.next

