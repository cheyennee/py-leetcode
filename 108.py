#给定二叉搜索树的中序遍历，二叉搜索树不唯一。若要求树是高度平衡的，树同样不唯一。

#解法一：递归，自己写的，因为这题是easy。有点类似二分法的感觉。时间41，内存41
class Solution(object):
    def sortedArrayToBST(self, nums):

        def dfs(left, right, nums):
            if left > right:
                return None
            mid = left + (right - left)//2
            root = TreeNode(nums[mid])
            root.left = dfs(left, mid-1,nums)
            root.right = dfs(mid+1, right, nums)
            return root
        
        return dfs(0, len(nums)-1, nums)

