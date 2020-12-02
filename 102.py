#解法一：看了代码你就懂思路了，因为我是抄的hh，时间47，内存35
#踩坑，本来以为返回一个list就行了，后来发现答案是嵌套的list，也就是每一层都是一个list
#答案妙就妙在它的queue不是一次性存放所有node，而是一次存放一层的node
class Solution(object):
    def levelOrder(self, root):
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            currentLevelSize = len(queue)
            temp = []
            for i in range(0, currentLevelSize):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res
