# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。 
# 
#  路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [0,1000] 
#  -10⁹ <= Node.val <= 10⁹ 
#  -1000 <= targetSum <= 1000 
#  
#  👍 1269 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def pathSum(self, root: TreeNode, targetSum: int) -> int:
    #     """
    #     方法1：深度优先。前序遍历思想。
    #     """
    #     def path(root, num):
    #         if not root:
    #             return 0
    #         ret = 0
    #         if root.val == num:
    #             ret += 1
    #         ret += path(root.left, num - root.val)
    #         ret += path(root.right, num - root.val)
    #         return ret
    #
    #     if not root:
    #         return 0
    #
    #     res = path(root, targetSum)
    #     res += self.pathSum(root.left, targetSum)
    #     res += self.pathSum(root.right, targetSum)
    #     return res

    # def pathSum(self, root: TreeNode, targetSum: int) -> int:
    #     """
    #     方法2：前缀和, 回溯思想。
    #     """
    #     res = 0
    #     if not root:
    #         return res
    #     from collections import defaultdict
    #     prefix_sum = defaultdict(int)
    #     prefix_sum[0] = 1
    #
    #     def dfs(root, cur):
    #         nonlocal res
    #         if not root:
    #             return
    #
    #         cur += root.val
    #         res += prefix_sum[cur - targetSum]
    #
    #         prefix_sum[cur] += 1
    #         dfs(root.left, cur)
    #         dfs(root.right, cur)
    #         prefix_sum[cur] -= 1
    #
    #     dfs(root, 0)
    #     return res

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """
        方法3：前缀和 + 深度优先，回溯
        """
        from collections import defaultdict
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def dfs(root, cur):
            res = 0
            if not root:
                return res

            cur += root.val
            res += prefix_sum[cur - targetSum]

            prefix_sum[cur] += 1
            res += dfs(root.left, cur)
            res += dfs(root.right, cur)
            prefix_sum[cur] -= 1

            return res

        return dfs(root, 0)



# leetcode submit region end(Prohibit modification and deletion)
