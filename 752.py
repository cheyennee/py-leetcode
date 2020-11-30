#解法一，广度优先搜索，时间84，内存5
#只能说自己好菜，看答案其实觉得答案很简单
#思路：将0000到9999看成是图上的10000个节点

#广度优先搜索的重点在于它怎么扩展到周围的节点
class Solution(object):
    def openLock(self, deadends, target):
        #每个节点有八个邻居，即将它的每一位增加1或减少1
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x+d)%10
                    yield node[:i]+str(y)+node[i+1:]
        
        dead = set(deadends)
        #存放节点以及该节点的高度
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in dead:
                continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1
    
