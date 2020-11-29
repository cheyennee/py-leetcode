#使用BFS的两个场景：遍历或找出最短路径
#好菜啊

#解法一：深度优先搜索，时间91，内存23
#扫描整个网格，如果一个位置为1，则从其开始进行深度优先搜索，将每个搜索到的位置置0
#最终岛屿的数量等于深度优先搜索的次数
#深度优先搜索使用了递归
class Solution(object):
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        #遍历上下左右
        for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if 0<=x<nr and 0<=y<nc and grid[x][y] == '1':
                self.dfs(grid,x,y)
    def numIslands(self, grid):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    self.dfs(grid, r, c)
        return num_islands

#解法二：广度优先搜索，时间98，内存21
#我不是很理解广度优先搜索。其实跟深度有点像，只不过它是从一个点出发遍历该点的上下左右，然后继续遍历下一层的上下左右
#就是广度是一层一层来的，而深度是一次到底的
class Solution(object):
    def numIslands(self, grid):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    grid[r][c] = '0'
                    #deque为双端队列
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x,y in [(row-1,col),(row,col-1),(row+1,col),(row,col+1)]:
                            if 0<=x<nr and 0<=y<nc and grid[x][y] == '1':
                                neighbors.append((x,y))
                                grid[x][y] = '0'
        return num_islands

#解法三：并查集，时间27，内存10
#不理解并查集这种方法，日后填坑
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1]*(m*n)
        #rank用于路径压缩，但是我不明白
        self.rank = [0]*(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i*n+j] = i*n+j
                    self.count += 1
    #用递归找父亲
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    #将相同父节点的两个节点合并
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1
    def getCount(self):
        return self.count

class Solution(object):
    def numIslands(self, grid):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    for x, y in [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]:
                        if 0<=x<nr and 0<=y<nc and grid[x][y] == '1':
                            uf.union(r*nc+c, x*nc+y)
        return uf.getCount()
