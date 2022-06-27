# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。 
# 
#  除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接
# 相连的房子在同一天晚上被打劫 ，房屋将自动报警。 
# 
#  给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: root = [3,2,3,null,3,null,1]
# 输出: 7 
# 解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7 
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: root = [3,4,5,1,3,null,1]
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
#  
# 
#  
# 
#  提示： 
# 
#  
# 
#  
#  树的节点数在 [1, 10⁴] 范围内 
#  0 <= Node.val <= 10⁴ 
#  
#  👍 1216 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # def rob(self, root: TreeNode) -> int:
    #     """
    #     方法1：递归。会超时，有重复计算。
    #     站在每个节点，偷法有两种。
    #     1）偷当前节点 + 偷孙子节点
    #     2）偷左孩子节点 + 偷右孩子节点
    #     """
    #
    #     if not root:
    #         return 0
    #
    #     # 方式1：爷爷 + 孙子
    #     method1 = root.val
    #     # 左孙子
    #     if root.left:
    #         method1 += self.rob(root.left.left) + self.rob(root.left.right)
    #     # 右孙子
    #     if root.right:
    #         method1 += self.rob(root.right.left) + self.rob(root.right.right)
    #
    #     # 方式2：两个孩子
    #     method2 = self.rob(root.left) + self.rob(root.right)
    #
    #     return max(method1, method2)

    # def rob(self, root: TreeNode) -> int:
    #     """
    #     方法2：递归+备忘录。还是超时，奇怪。
    #     """
    #     # 记录每个节点当root节点时的最大偷盗价值
    #     memo = {}
    #
    #     def dfs(node):
    #         if not node:
    #             return 0
    #
    #         if node in memo:
    #             return memo[node]
    #
    #         # 方式1：爷爷 + 孙子
    #         method1 = root.val
    #         # 左孙子
    #         if root.left:
    #             method1 += self.rob(root.left.left) + self.rob(root.left.right)
    #         # 右孙子
    #         if root.right:
    #             method1 += self.rob(root.right.left) + self.rob(root.right.right)
    #
    #         # 方式2：两个孩子
    #         method2 = self.rob(root.left) + self.rob(root.right)
    #
    #         max_value = max(method1, method2)
    #         memo[node] = max_value
    #         return max_value
    #
    #     return dfs(root)

    def rob(self, root: TreeNode) -> int:
        """
        方法3：使用包含两个元素的列表表示每个节点的偷或者不偷，所能偷到的最大值。
        0 不偷；1 偷；
        二叉树后序遍历
        """

        def dfs(node):
            result = [0, 0]
            if not node:
                return result

            left = dfs(node.left)
            right = dfs(node.right)

            # 1）不偷当前node，左和右都可以选择偷或者不偷，取最大值即可。
            result[0] = max(left[0], left[1]) + max(right[0], right[1])

            # 2）偷当前node。则左右都不能偷。
            result[1] = left[0] + right[0] + node.val

            return result

        res = dfs(root)
        return max(res)

# leetcode submit region end(Prohibit modification and deletion)

