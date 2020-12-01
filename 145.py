#解法一：递归，时间96，内存13
class Solution(object):
    def postorderTraversal(self, root):
        res = []
        if not root:
            return res
        def postorder(root):
            if not root:
                return 
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res

#解法二：迭代，时间96，内存5
'''
在后序遍历中，节点要入两次栈，出两次栈
第一次出栈：只遍历完左子树，该节点不出栈，利用栈顶节点找到它的右子树
第二次出栈：遍历完右子树，将该节点出栈，并访问它
'''
#不理解
class Solution(object):
    def postorderTraversal(self, root):
        res = []
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            #第二次出栈
            #我不理解这个prev？？？
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                #保证下次循环的时候可以进入else部分
                root = None
            else:
                #第一次出栈
                stack.append(root)
                root = root.right
        return res

#解法三：迭代，时间84，内存16
#这种解法利用的是前序遍历与后序遍历的差异，好香啊
class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans[::-1]

#解法四：morris遍历，时间57，内存5
#不理解
class Solution(object):
    def postorderTraversal(self, root):
        def addPath(node):
            count = 0
            while node:
                count += 1
                res.append(node.val)
                node = node.right
            i, j = len(res) - count, len(res) - 1
            while i< j:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
        
        if not root:
            return []
        res = []
        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
                    addPath(p1.left)
            p1 = p1.right
        addPath(root)
        return res
