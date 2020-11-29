#解法一：数组表示，时间73，内存34
class MyCircularQueue(object):
    def __init__(self, k):
        #以数组的形式表示循环队列，这不是python内嵌的队列
        self.queue = [0]*k
        self.headIndex = 0
        #妙就妙在它没有设置尾指针，而是通过记录长度去计算尾指针的位置
        self.count = 0
        self.capacity = k
    def enQueue(self, value):
        if self.count == self.capacity:
            return False
        self.queue[(self.headIndex+self.count)%self.capacity]=value
        self.count += 1
        return True
    def deQueue(self):
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex+1)%self.capacity
        self.count-=1
        return True
    def Front(self):
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]      
    def Rear(self):
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex+self.count-1)%self.capacity]
    def isEmpty(self):
        return self.count == 0
    def isFull(self):
        return self.count == self.capacity
        
#解法二：链表表示，时间52，内存18
class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode

class MyCircularQueue(object):
    def __init__(self, k):
        self.capacity = k
        self.head = None
        #使用了尾指针，否则就要遍历去查找尾指针的位置了
        self.tail = None
        self.count = 0
    def enQueue(self, value):
        if self.count == self.capacity:
            return False
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True
    def deQueue(self):
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True
    def Front(self):
        if self.count == 0:
            return -1
        return self.head.value
    def Rear(self):
        if self.count == 0:
            return -1
        return self.tail.value
    def isEmpty(self):
        return self.count == 0
        

    def isFull(self):
        return self.count == self.capacity
