#解法一：层次遍历，时间59，内存33，这一定是最快做出题目的一次哈哈哈
class Solution(object):
    def connect(self, root):
        if not root:
            return None
        queue = [root]
        while queue:
            lensize = len(queue)
            for i in range(lensize):
                node = queue.pop(0)
                if i != lensize-1:
                    node.next = queue[0]
                else:
                    node.next = None
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
        return root


#解法二：使用已建立的next指针，答案这种做法好巧妙啊
#时间：79，内存：57
#我感觉也是层次遍历的思想，只不过它这个层次遍历利用了已有的层次，注意题目已给所有next指针初始化为none
'''
1.两个子节点属于同一个父节点，直接通过父节点建立两个子节点的next指针
2.第一个父节点的右孩子和第二个父节点的左孩子
'''
class Solution(object):
    def connect(self, root):
        if not root:
            return None
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
