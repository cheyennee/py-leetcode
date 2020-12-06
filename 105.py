#解法一：递归，时间74，内存83
#很奇怪为什么后序+中序遍历需要先创建右节点，而前序+中序不需要呢？
class Solution(object):
    def buildTree(self, preorder, inorder):
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            root = TreeNode(preorder.pop(0))
            root.left = helper(in_left, inorder.index(root.val)-1)
            root.right = helper(inorder.index(root.val)+1, in_right)
            return root
        
        return helper(0, len(inorder)-1)

#解法二：迭代，来日填坑，我真是不会做了QAQ
