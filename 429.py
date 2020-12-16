#解法一：迭代，时间71，内存21
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return None
        queue, res = [root], []
        while queue:
            lensize = len(queue)
            temp = []
            for c in range(lensize):
                node = queue.pop(0)
                temp.append(node.val)
                queue.extend(node.children)
            res.append(temp)
        return res

#解法二：递归，时间88，内存9
#层次遍历可以用递归是我没想到的。因为它巧妙的使用了题目的返回格式
class Solution(object):
    def levelOrder(self, root):
        
        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level+1)
        
        result = []
        if root:
            traverse_node(root, 0)
        return result

