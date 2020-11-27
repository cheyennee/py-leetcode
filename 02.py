#解法一：遍历，时间82，内存14
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return l1 if not l2 else l2
        head = ListNode(0)
        cur = head
        ci = 0
        while l1 and l2:
            if l1.val + l2.val + ci >= 10:
                newNode = ListNode(l1.val+l2.val+ci-10)
                ci = 1
                cur.next = newNode
                cur = cur.next
            else:
                newNode = ListNode(l1.val+l2.val+ci)
                ci = 0
                cur.next = newNode
                cur = cur.next
            l1 = l1.next
            l2 = l2.next
        l1 = l2 if not l1 else l1
        while l1:
            if l1.val + ci >= 10:
                newNode = ListNode(l1.val+ci-10)
                ci = 1
                cur.next = newNode
                cur = cur.next
            else:
                newNode = ListNode(l1.val+ci)
                ci = 0
                cur.next = newNode
                cur = cur.next
            l1 = l1.next
        #踩坑，被测试用例卡了才想到最后ci=1的时候还需要加一位
        if ci == 1:
            cur.next = ListNode(1)
        return head.next
