#解法一：递归，第一次这么快想出递归的解法来，时间74，内存9

class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        #第一次提交失败是因为漏掉了到叶子节点这个条件
        if root.val - sum == 0 and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right,sum-root.val)

#解法二：深度优先遍历，时间53，内存28
#说是说深度优先遍历，但是实际上这是后序遍历的思想我拿来借鉴了，因为一个节点需要入栈两次
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack = []
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                sum -= root.val
                root = root.left
            root = stack.pop()
            if sum == 0 and not root.right and not root.left:
                return True
            #如果它有右节点证明它肯定不满足叶子节点的条件，故直接去访问其右子树
            #第二次入栈
            if root.right and root.right != prev:
                stack.append(root)
                root = root.right
            else:
                #该出栈了
                sum += root.val
                #后序遍历精髓
                prev = root
                root = None
                #
        return False
    
