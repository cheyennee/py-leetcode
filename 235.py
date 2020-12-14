#解法一：与二叉树找最近共同祖先一致，时间58，内存5
#踩坑，忘记fa[root.val] = None了
class Solution(object):
    def helper(self, root, fa):
        if root.left:
            fa[root.left.val] = root
            self.helper(root.left, fa)
        if root.right:
            fa[root.right.val] = root
            self.helper(root.right, fa)

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        fa, vis = {}, {}
        fa[root.val] = None
        self.helper(root, fa)
        while p:
            vis[p.val] = True
            p = fa[p.val]
        while q:
            if q.val in vis.keys() and vis[q.val] == True:
                return q
            q = fa[q.val]
        return None


#解法二：递归，时间74，内存7
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        lNode = self.lowestCommonAncestor(root.left, p, q)
        rNode = self.lowestCommonAncestor(root.right, p, q)
        if lNode and rNode:
            return root
        elif lNode:
            return lNode
        else :
            return rNode
        return None


#解法三：利用了二叉搜索树的性质，妙啊，时间74，内存30
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val :
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor


#解法四：先找出经过p和q的路径，然后比较两条路径上的节点，时间86，内存16
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def getPath(root, target):
            path = []
            node = root
            while node != target:
                path.append(node)
                if target.val < node.val:
                    node = node.left
                else:
                    node = node.right
            path.append(node)
            return path
        
        path_p = getPath(root, p)
        path_q = getPath(root, q)
        ancestor = None
        for u, v in zip(path_p, path_q):
            if u == v:
                ancestor = u
            else:
                break
        return ancestor

