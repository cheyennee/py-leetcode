#二叉搜索树的优点:可以在oh的时间复杂度内执行所有的搜索、插入、删除操作
#如果想有序存储数据或者同时执行搜索、插入、删除等，二叉搜索树will be a good choice

#解法一：二叉搜索树，可是我抄的这段代码它didn't work
#明天吧，今天不想了QAQ
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1

class KthLargest(object):

    def __init__(self, k, nums):
        self.root = None
        self.k = k
        for n in nums:
            self.addNodeToTree(n)

    def createTree(self, node, val):
        if not node:
            return TreeNode(val)
        if node.val > val:
            node.left = self.createTree(node.left, val)
        elif node.val < val:
            node.right = self.createTree(node.right, val)
        node.count += 1
        return node

    def addNodeToTree(self, val):
        self.root = self.createTree(self.root, val)

    def search(self, node, k):
        if not node:
            return node
        leftNodeCount = node.left.count if node.left else 0
        rightNodeCount = node.right.count if node.right else 0
        currNodeCount = node.count - leftNodeCount - rightNodeCount
        if k > currNodeCount + rightNodeCount:
            return search(node.left,k-currNodeCount-rightNodeCount)
        elif k<=rightNodeCount:
            return search(node.right, k)
        else:
            return node

    def add(self, val):
        self.addNodeToTree(val)
        #node = self.search(self.root, self.k)
        #return node.val
        return self.search(self.root, self.k).val



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


#解法二：一把过的那种，不过效率太低了，时间22，内存14
class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums

    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]

#解法三：应该还有堆排序的解法，日后填坑
