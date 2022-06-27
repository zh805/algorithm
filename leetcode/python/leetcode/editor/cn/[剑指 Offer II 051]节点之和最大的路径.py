# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不
# 一定经过根节点。 
# 
#  路径和 是路径中各节点值的总和。 
# 
#  给定一个二叉树的根节点 root ，返回其 最大路径和，即所有路径上节点值之和的最大值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目范围是 [1, 3 * 10⁴] 
#  -1000 <= Node.val <= 1000 
#  
# 
#  
# 
#  注意：本题与主站 124 题相同： https://leetcode-cn.com/problems/binary-tree-maximum-path-
# sum/ 
#  Related Topics 树 深度优先搜索 动态规划 二叉树 👍 22 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        方法1：后续遍历，计算每个节点作为根节点时的最大路径和
        """
        res = float('-inf')

        def traverse(root):
            if not root:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)
            if left < 0:
                left = 0
            if right < 0:
                right = 0

            # 当root为根节点时的最大值
            nonlocal res
            res = max(res, root.val + left + right)

            # root作为子节点时，只能选择左右路径中最大的一个。
            return root.val + max(left, right)

        traverse(root)
        return res

# leetcode submit region end(Prohibit modification and deletion)
