#解法一：层次遍历，自己写的！时间78，内存34
#卡了一会，本来是没有把空节点加入队列，后来发现null,3,null,3这种例子过不去
#于是做了修改，将空节点加进入了就过了
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        queue = [root]
        while queue:
            lensize = len(queue)
            res = []
            for i in range(lensize):
                node = queue.pop(0)
                if node:
                    res.append(node.val)
                else:
                    res.append(None)
                    continue
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
            if res != res[::-1]:
                return False
        return True

#解法二：递归，抄的，时间92，内存5
#不得不说这个递归太难想了555，转不过来...答案这个递归很傻逼的是它从根节点开始比较，可是只有一个节点的时候完全没有必要进行比较

class Solution(object):
    def check(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)
    
    def isSymmetric(self, root):
        return self.check(root, root)

#解法二：递归，将答案的递归进行了改进。这个递归我比较好理解，时间92，内存12
class Solution(object):
    def check(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)
    
    def isSymmetric(self, root):
        if not root:
            return True
        return self.check(root.left, root.right)
    
