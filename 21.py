#解法一：遍历，时间88，内存15
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l2 if not l1 else l1
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1:
            head.next = l1
        elif l2:
            head.next = l2
        return dummy.next

#解法二：递归，时间96，内存14
#哭死了，官方题解的递归太优雅了
#酸死了，又是我写不出来的
'''
list1[0]+merge(list1[1:],list2) list1[0]<list2[0]
list2[0]+merge(list1,list2[1:]) otherwise
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l2 if not l1 else l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

