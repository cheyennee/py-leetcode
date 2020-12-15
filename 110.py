#解法一：自底向上递归，抄的，时间88，内存5
class Solution(object):
    def isBalanced(self, root):

        def height(root):
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            #如果左右子树有问题就一直返回-1
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight-rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0

    
