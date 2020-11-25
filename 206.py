#解法一：头插法，时间42，内存46
#踩坑，摘下来的那个节点的next指针并不是头结点，而是dummy.next
class Solution(object):
    def reverseList(self, head):
        if not head:
            return head
        dummy = ListNode(0, head)
        while head.next:
            cur = head.next
            head.next = head.next.next
            cur.next = dummy.next
            dummy.next = cur
        return dummy.next

#解法二：递归，抄的，时间21，内存7
#只能说妙啊-^-
#愿天堂没有递归QAQ
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        #head.next为nk+1
        #此句话要表达的意思是，前面的节点都已经反转好了，接下来要反转nk+1
        #让nk+1.next = nk
        head.next.next = head
        #确保n1的下一个指向是null
        head.next = None
        #整个递归的返回值其实只有一个
        return p
