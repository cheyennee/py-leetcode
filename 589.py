#解法一：递归，时间76，内存39
#踩坑，此处的children是列表，列表中每个元素是node
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        
        def helper(node):
            if not node:
                return 
            res.append(node.val)
            for i in range(len(node.children)):
                helper(node.children[i])
        
        res = []
        helper(root)
        return res


#解法二：遍历，抄的，时间55，内存13
class Solution(object):
    def preorder(self, root):
        if not root:
            return None
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            #将u的子节点逆序推入栈中。
            #若u的子节点为v1,v2,v3,则推入栈的顺序为v3,v2,v1,出栈的顺序为v1,v2,v3
            stack.extend(root.children[::-1])
        return output

