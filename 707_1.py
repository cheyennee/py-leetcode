#单链表
#时间31，内存51
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)


    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        #因为有一个多余的头结点，所以range(index+1)
        for _ in range(index+1):
            curr = curr.next
        return curr.val


    def addAtHead(self, val):
        self.addAtIndex(0, val)


    def addAtTail(self, val):
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index, val):
        if index > self.size:
            return 
        if index < 0:
            index = 0
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add


    def deleteAtIndex(self, index):
        if index<0 or index>=self.size:
            return 
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next

