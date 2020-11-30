#解法一：递归，时间95，内存46
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def preorderTraversal(self, root):

        def preorder(root):
            if not root:
                return
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        result = []
        preorder(root)
        return result

#解法二：迭代，时间95，内存15，使用栈
class Solution(object):
    def preorderTraversal(self, root):
        res = []
        if not root:
            return res
        
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

#解法三:morris算法，时间82，内存10,时间on,空间o1，利用了树的空闲指针,好厉害
'''
算法思想：
当前节点为cur
1.如果cur无左孩子，cur向右移动（cur=cur.right）
2.如果cur有左孩子，找到cur左子树上最右的节点，记为mostright
  2.1如果mostright的right指针指向空，让其指向cur，cur向左移动（cur=cur.left）
  2.2如果mostright的right指针指向cur，让其指向空，cur向右移动（cur=cur.right）

'''
class Solution(object):
    def preorderTraversal(self, root):
        res = []
        if not root:
            return res
        
        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                #查找当前节点在中序遍历下的前驱结点
                while p2.right and p2.right != p1:
                    p2 = p2.right
                #如果前驱结点的右子节点为空，将当前节点加入答案，并将前驱结点的右子节点更新为当前节点，当前节点更新为当前节点的左子节点
                if not p2.right:
                    res.append(p1.val)
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                #如果前驱结点的右子节点为当前节点，将它的右子节点设空
                    p2.right = None
            else:
                res.append(p1.val)
            #因为p1向右移动有两种情况,所以统一写这句话
            p1 = p1.right
        return res
    
