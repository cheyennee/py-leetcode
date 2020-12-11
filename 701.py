#插入一个新节点的方法：找到合适的子节点的位置插入

#解法一：迭代，自己写的，时间96，内存5
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        pre = root
        node = root.left if root.val > val else root.right
        while node:
            pre = node
            if node.val > val:
                node = node.left
            else:
                node = node.right
        if pre.val > val:
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)
        return root

#解法二：递归，自己写的，时间99，内存5
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

