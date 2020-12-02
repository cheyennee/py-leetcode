#解法一：递归，我自己写的，时间57，内存5
class Solution(object):
    def maxDepth(self, root):
        #踩坑，此句完全是为了卡测试用例[]
        if not root:
            return 0
            
        def getDepth(root, depth):
            if not root:
                return depth
            #踩坑，如果不写这个，当左/右子树为空时，会报错
            #而且它们的初始值为depth而不是0
            leftDepth, rightDepth = depth, depth 
            if root.left:
                leftDepth = getDepth(root.left,depth+1)
            if root.right:
                rightDepth = getDepth(root.right,depth+1)
            return max(leftDepth, rightDepth)
        
        depth = getDepth(root, 0)
        return depth + 1

#解法一：递归，这是官方题解，时间57，内存43
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth)+1

#解法二：使用层次遍历，我自己写的嘻嘻，时间33，内存41
#我终于理解层次遍历为什么既可以求深度也可以求宽度了，刷题的快乐就在于此吧
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        queue = [root]
        height = 0
        while queue:
            currentSize = len(queue)
            for i in range(currentSize):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height += 1
        return height
