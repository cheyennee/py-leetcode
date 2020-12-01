#解法一：递归，时间60，内存24
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        if not root:
            return res
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

#解法二：迭代，时间85，内存27，使用栈
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1]
            stack.pop()
            res.append(root.val)
            root = root.right
        return res

#解法三：morris遍历，时间85，内存28
#如果p2.right为空，则继续访问；否则说明已经遍历完p1的左子树,可以将p1.val加入答案
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        if not root:
            return res
        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    res.append(p1.val)
                    p2.right = None
            else:
                res.append(p1.val)
            p1 = p1.right
        return res

