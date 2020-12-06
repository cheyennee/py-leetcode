#解法一：递归，时间92， 内存68，我抄的，思路虽然有，但是自己写的时候别扭别扭
#踩坑，题目给的列表里的是数字而不是node
#踩坑，这里需要先创建右子树，再创建左子树。可以理解为在后序遍历中，整个数组是先存储左子树的节点，再存储右子树的节点，最后存储根节点。如果按照每次选择后序遍历的最后一个节点为根节点，则先被构造出来的应该是右子树

class Solution(object):
    def buildTree(self, inorder, postorder):
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = idx_map[val]
            #
            root.right = helper(index+1, in_right)
            root.left = helper(in_left, index-1)
            #
            return root
        #因为题目已经明确list中的val是不会重复的，所以可以用val作为key
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)

#解法二：迭代，时间87，内存99。我第一次见过内存这么高的，不愧是官方解法
'''
思路：后序遍历两个相邻节点u与v之间的关系
1.u是v的右儿子
2.v没有右儿子，并且u是v的某个祖先节点的左儿子
'''
'''
算法流程：
1.用一个栈和一个指针辅助进行二叉树的构造。初始时，栈中存放了根节点，指针指向中序遍历的最后一个节点
2.
2.1枚举后序遍历中除了第一个节点之外的每一个节点。如果index正好指向栈顶元素，则弹出栈顶节点并向左移动index，并将当前节点作为最后一个弹出的节点的左儿子
2.2如果index和栈顶节点不同，我们将当前节点作为栈顶节点的右儿子
'''
'''
栈：当前节点的所有还没有考虑过左儿子的祖先节点，栈顶即为当前节点
index:当前节点不断往右走到达的最终节点
'''
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        stack = [root]
        inorderindex = len(inorder) - 1
        for i in range(len(postorder)-2, -1, -1):
            postorderVal = postorder[i]
            node = stack[-1]
            if node.val != inorder[inorderindex]:
                node.right = TreeNode(postorderVal)
                stack.append(node.right)
            else:
                while stack and stack[-1].val == inorder[inorderindex]:
                    node = stack.pop()
                    inorderindex -= 1
                node.left = TreeNode(postorderVal)
                stack.append(node.left)
        return root
