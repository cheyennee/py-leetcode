#解法一：递归，自己写的，时间37，内存5
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        
        def helper(node, height):
            if not node:
                #此处注意是返回0，而不是height，因为是自底向上求高度的
                return 0
            hei = []
            for i in node.children:
                hei.append(helper(i, height))
            #踩坑，加入这个判断的原因是因为当孩子节点为空时，此列表为空，max会返回异常
            if hei == []:
                return 1
            else:
                return max(hei) + 1
        
        return helper(root, 0)

#解法二：迭代，抄的，时间57，内存12
#广度优先
class Solution(object):
    def maxDepth(self, root):
        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                for c in root.children:
                    stack.append((current_depth+1, c))
        return depth
    
