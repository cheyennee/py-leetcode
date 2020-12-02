class Solution(object):
    def preorder(self, root):
        res = []
        if not root:
            return res
        stack = []
        node = root
        while stack or node:
            while node:
                #每个节点只有一次入栈的操作
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

class Solution(object):
    def inorder(self, root):
        res = []
        if not root:
            return res
        stack = []
        node = root
        while stack or node:
            while node:
                #每个节点只有一次入栈的操作
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

class Solution(object):
    def postorder(self, root):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]

class Solution(object):
    def postorder(self, root):
        res = []
        stack = []
        prev = None
        while root or stack:
            while root:
                #每个节点第一次入栈
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                #保证下次循环可以进入else部分
                root = None
            else:
                #每个节点第二次入栈
                stack.append(root)
                root = root.right
        return res
    
