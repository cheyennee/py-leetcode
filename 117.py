#解法一：层次遍历，时间96，内存5
#这题与版本I的不同在于，树是任意的，每个节点可以没有左右孩子
class Solution(object):
    def connect(self, root):
        if not root:
            return None
        stack = [root]
        while stack:
            length = len(stack)
            for i in range(length):
                node = stack.pop(0)
                if i != length - 1:
                    node.next = stack[0]
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root


#解法二：利用已有的节点创建儿子节点的next指针，时间73，内存5
#我是抄的，这种解法着实迷糊人，而且python的值传递太迷了
class Solution(object):
    def handle(self, last, p, nextstart):
        if last:
            last.next = p
        if not nextstart:
            nextstart = p
        last = p
        return last, nextstart

    def connect(self, root):
        if not root:
            return None
        start = root
        while start:
            last = None
            nextstart = None
            p = start
            while p:
                if p.left:
                    last, nextstart = self.handle(last, p.left, nextstart)
                if p.right:
                    last, nextstart = self.handle(last, p.right, nextstart)
                p = p.next
            start = nextstart
        return root

