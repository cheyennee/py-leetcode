#我想用的迭代，可是卡在测试用例[0]上面了
class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        node, prev = root, None
        while node:
            if node.val < key:
                prev = node
                node = node.right
            elif node.val > key:
                prev = node
                node = node.left
            else:
                break
        if not node:
            return root
        if not node.left and not node.right:
            #很奇怪这里会返回错误
            node = None
        elif (not node.left and node.right):
            if prev.left == node:
                prev.left = node.right
            else:
                prev.right = node.right
        elif (not node.right and node.left):
            if prev.left == node:
                prev.left = node.left
            else:
                prev.right = node.left
        else:
            #temp为待删除的节点
            temp = node
            #寻找中序遍历后继节点
            prev = node.right
            node = node.right
            if not node.left:
                temp.val = node.val
                temp.right = node.right
                return root
            while node.left:
                prev = node
                node = node.left
            temp.val = node.val
            prev.left = None
        return root



#解法一：递归，抄的，时间59，内存25
class Solution(object):
    #寻找中序遍历的下一个节点
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    #寻找中序遍历的前一个节点
    def presuccessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root, key):
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.presuccessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root

