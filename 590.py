#解法一：递归，时间54，内存28
class Solution(object):
    def postorder(self, root):
        
        def helper(node):
            if not node:
                return 
            for i in range(len(node.children)):
                helper(node.children[i])
            res.append(node.val)

        res = []
        helper(root)
        return res

#解法二：迭代，抄的，时间77，内存31
#这个这么简洁是我没有想到的QAQ
class Solution(object):
    def postorder(self, root):
        if not root:
            return None
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
            for c in root.children:
                stack.append(c)
        return output[::-1]

