#想用递归的，然后自己写的代码如下，它卡在第69/77个用例上了
#卡住的原因是：没有考虑到[5,3,6,null,null,4,7]这样的用例，也就是没有保证子树的大小与父节点的祖先的关系
#所以需要记录祖先节点的值，因为记录每个值不现实，所以此处选择记录一个区间
class Solution(object):        
    def isValidBST(self, root):
        if not root:
            return True
        if root.left and root.right:
            if root.left.val < root.val and root.right.val > root.val:
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            else:
                return False
        elif not root.left and root.right:
            if root.right.val > root.val:
                return self.isValidBST(root.right)
            else:
                return False
        elif not root.right and root.left:
            if root.left.val < root.val:
                return self.isValidBST(root.left)
            else:
                return False
        return True

#解法一：递归,抄的，时间80，内存59
class Solution(object):
    def isValidBST(self, root):
        def helper(node, lower=float('-inf'),upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val<=lower or val>=upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        return helper(root)

#解法二：中序遍历，我竟然忘记这个知识点了QAQ
#中序遍历可以检查二叉搜索树，时间93，内存43
class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            #妙在比较大小这里
            if root.val <= inorder:
                return False
            else:
                inorder = root.val
            root = root.right
        return True

