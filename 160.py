#解法一：遍历一遍A与B，时间90，内存6，主要是set太吃内存了
#而且这个题给的链表是没有头节点的
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        aset = set()
        while headA:
            aset.add(headA)
            headA = headA.next
        while headB:
            if headB in aset:
                return headB
            headB = headB.next
        return None


#解法二：双指针，根据官方的思路自己写的代码，事实证明，我菜得一批
#时间85，内存5
'''
思路：
创建pa,pb,指向A和B的头结点，然后逐节点遍历
当pa到达A的尾部时，将它重定位到B的头结点；pb亦然
某一时刻pa和pb相遇，即为A与B的交点

通俗解释：len(A+B)=len(B+A),若A和B相交则尾巴长度一定相同，故在相遇点之前一定遍历相同的长度
'''

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        length = 0
        while headA:
            headA = headA.next
            length += 1
        while headB:
            headB = headB.next
            length += 1
        headA = pa
        headB = pb
        for _ in range(length):
            if pa == None:
                pa = headB
            if pb == None:
                pb = headA
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None


#解法三：双指针，抄的评论的比较简洁的做法，时间98，内存24
#这个解法巧妙在循环的判断条件，巧妙的利用了None = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        pa = headA
        pb = headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa

