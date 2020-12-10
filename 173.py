#解法一：中序遍历，自己写的，时间59，内存100.哇，我第一次见过内存100

class BSTIterator(object):

    def __init__(self, root):
        stack = []
        self.res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.res.append(root.val)
            root = root.right

    def next(self):
        #rtype:int
        return self.res.pop(0)


    def hasNext(self):
        return True if len(self.res) else False

#解法二：中序遍历，抄的，时间59，内存64。受控递归，虽然本质上与解法一一致，但是真的太强了
#太妙了啊。这个解法可以控制中序遍历的停止与开始，真正符合next的含义

class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    #妙在这个方法
    def next(self):
        topmost_node = self.stack.pop()
        #需要继续将该节点的右子树入栈。如果让我写我肯定直接返回节点的val了。
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val


    def hasNext(self):
        return len(self.stack) > 0

