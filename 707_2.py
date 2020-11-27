#双链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        #可以借鉴，通过比较查看从头遍历更快到达目标节点还是从尾开始遍历更快到达
        if index+1<self.size-index:
            curr = self.head
            for _ in range(index+1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size-index):
                curr = curr.prev
        return curr.val


    def addAtHead(self, val: int) -> None:
        pred, succ = self.head, self.head.next
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtTail(self, val: int) -> None:
        succ, pred = self.tail, self.tail.prev
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        if index < 0:
            index = 0
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred 
        to_add.next = succ 
        succ.prev = to_add
        pred.next = to_add


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size-index-1):
                succ = succ.prev
            pred = succ.prev.prev
        self.size -= 1
        pred.next = succ
        succ.prev = pred

