#解法一：递归，时间63，内存5
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        if (root.val > val):
            return self.searchBST(root.left, val);
        else:
            return self.searchBST(root.right, val);

#解法二：迭代，时间89，内存5，可是我的迭代浪费一棵这么好的树555
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val == val:
                return root
            root = root.right
        return None

#解法二：迭代，官方解法，时间97，内存37
class Solution(object):
    def searchBST(self, root, val):
        while root and root.val != val:
            root = root.left if root.val > val else root.right
        return root

