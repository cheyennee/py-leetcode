#解法一：存储父节点，抄的，时间69，内存33
#我本来想用先序遍历的，后来发现这种方法就没有办法知道父节点，从后往前找父节点的时候就有问题
class Solution(object):
    #寻找每一个节点的父节点
    '''
    这里的代码感觉是可以优化的，因为此处存放了一棵树中所有的父节点
    但是实际上我只需要存放p和q中最深的那个节点之前的所有父节点即可
    '''
    def dfs(self, fa, root):
        if root.left:
            fa[root.left.val] = root
            self.dfs(fa, root.left)
        if root.right:
            fa[root.right.val] = root
            self.dfs(fa, root.right)
        
    def lowestCommonAncestor(self, root, p, q):
        #fa用于存放父节点，vis用于存放已经访问过的节点
        fa, vis = {}, {}
        fa[root.val] = None
        self.dfs(fa, root)
        #从后往前找父节点，答案太妙了啊
        while p:
            vis[p.val] = True
            p = fa[p.val]
        while q:
            if q.val in vis.keys() and vis[q.val]:
                return q
            q = fa[q.val]
        return None


#解法二：递归，时间82，内存60
#思路：如果在当前节点的左右子树中找到了p和q，那么返回当前节点；如果在当前节点的左子树/右子树找到p和q，则去左子树/右子树

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root
        if root:
            lNode = self.lowestCommonAncestor(root.left,p,q)
            rNode = self.lowestCommonAncestor(root.right,p,q)
            if lNode and rNode:
                return root
            #两个都在右子树
            elif not lNode:
                return rNode
            #两个都在左子树
            else:
                return lNode
        return None

