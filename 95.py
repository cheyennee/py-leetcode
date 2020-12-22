#解法一：递归，抄的，时间88，内存33
#能够想到这个思路，但是递归写的真的不好
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):
                #这一行代码不可以放在此处
                #这样会导致有num棵子树会共用这个root节点
                #current_tree = TreeNode(i)
                
                left_trees = generate_trees(start, i - 1)
                
                right_trees = generate_trees(i + 1, end)
                
                #从左子树集合和右子树集合中分别选一棵拼接到根节点上
                #因为这个函数返回的是一个列表所以可以这么做
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            
            return all_trees
        
        return generate_trees(1, n) if n else []



#自己写的什么乱七八糟？我是什么辣鸡？555
class Solution(object):
    def generateTrees(self, n):
        

        def helper(left, right):
            if left > right:
                return None
            temp = []
            for i in range(left, right+1):
                node = TreeNode(i)
                node.left = helper(left, i-1)
                node.right = helper(i+1, right)
                temp = [node]
                if not node:
                    temp.extend(node.left)
                    temp.extend(node.right)
            return temp
        
        
        if n == 0:
            return None
        treeList = []
        for i in range(1, n+1):
            node = TreeNode(i)
            node.left = helper(1, i-1)
            node.right = helper(i+1, n)
            temp = [node]
            if not node:
                temp.extend(node.left)
                temp.extend(node.right)
            treeList.append(temp)
        return treeList
