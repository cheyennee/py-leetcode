#看着题目给的用例，我本来以为树是类似满二叉树的样子，后来发现并不是(狗头
#于是写了下面这些傻逼代码，还不舍得删掉(狗头
class Codec:

    def serialize(self, root):
        if not root:
            return None
        stack = [root]
        res = []
        while stack:
            length = len(stack)
            for i in range(length):
                node = stack.pop(0)
                if not node:
                    res.append(None)
                    continue
                else:
                    res.append(node.val)
                if node.left:
                    stack.append(node.left)
                else:
                    stack.append(None)
                if node.right:
                    stack.append(node.right)
                else:
                    stack.append(None)
        return res

    def deserialize(self, data):
        if not data:
            return None
        length = len(data)
        queue = []
        j = 0
        for i in range(length):
            if data[i]:
                queue.append(TreeNode(data[i]))
            else:
                queue.append(None)
        for i in range(length//2):
            queue[i].left = queue[2*i+1]
            queue[i].right = queue[2*(i+1)]
        return queue[0]
    
#这题竟然是hard

#解法一：深度优先遍历,时间48，内存53
class Codec:

    #前序遍历
    def rserialize(self, root, strstr):
        if not root:
            strstr.append(None)
        else:
            #这几行代码老厉害了
            strstr.append(root.val)
            strstr = self.rserialize(root.left, strstr)
            strstr = self.rserialize(root.right, strstr)
        return strstr

    def serialize(self, root):
        return self.rserialize(root, [])

    #从左往右遍历
    def rdeserialize(self, strstr):
        if strstr[0] == None:
            strstr.pop(0)
            return None
        root = TreeNode(strstr[0])
        strstr.pop(0)
        root.left = self.rdeserialize(strstr)
        root.right = self.rdeserialize(strstr)
        return root
    
    def deserialize(self, data):
        return self.rdeserialize(data)
        
#解法二：层次遍历，抄的别人的解法，时间98，内存13
#层次遍历真的是可行的，只不过我写序列化最后没有加上去除none的一行以及不会写反序列化
#菜猪是我了555
class Codec:

    def serialize(self, root):
        if not root:
            return None
        ans = [root.val]
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if not node.left:
                    ans.append(None)
                else:
                    ans.append(node.left.val)
                    queue.append(node.left)
                if not node.right:
                    ans.append(None)
                else:
                    ans.append(node.right.val)
                    queue.append(node.right)
        size = len(ans)
        #删除最后一行多余的none
        for i in range(size - 1, -1, -1):
            if ans[i] == None:
                ans.pop(i)
            else:
                break
        return ans

    def deserialize(self, data):
        if not data:
            return None
        root = TreeNode(data[0])
        #pos是关键
        pos = 1
        size = len(data)
        queue = [root]
        while queue:
            s = len(queue)
            for i in range(s):
                node = queue.pop(0)
                if pos == size:
                    return root
                m = data[pos]
                pos += 1
                #在还原的时候，当叶子节点为none时无需理会
                if m != None:
                    temp1 = TreeNode(m)
                    node.left = temp1
                    queue.append(temp1)
                if pos == size:
                    return root
                m = data[pos]
                pos += 1
                if m != None:
                    temp2 = TreeNode(m)
                    node.right = temp2
                    queue.append(temp2) 
        return root


#解法三：括号表示编码+递归下降解码，官方解法，没看懂
#日后填坑
    
