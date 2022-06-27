# 给定一个二叉树，找出其最大深度。 
# 
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例： 
# 给定二叉树 [3,9,20,null,null,15,7]， 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最大深度 3 。 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1116 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     """
    #     方法1：自顶向下，前序遍历
    #     :param root:
    #     :return:
    #     """
    #     ans = 0
    #
    #     def traverse(root, depth):
    #         if not root:
    #             return
    #
    #         if not root.left and not root.right:
    #             nonlocal ans
    #             ans = max(ans, depth)
    #
    #         traverse(root.left, depth + 1)
    #         traverse(root.right, depth + 1)
    #
    #     traverse(root, 1)
    #     return ans
    #
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     """
    #     方法2：自底向上，后序遍历
    #     :param root:
    #     :return:
    #     """
    #
    #     def traverse(root):
    #         if not root:
    #             return 0
    #
    #         left = traverse(root.left)
    #         right = traverse(root.right)
    #
    #         return max(left, right) + 1
    #
    #     return traverse(root)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        方法2：递归
        """
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1




# leetcode submit region end(Prohibit modification and deletion)
