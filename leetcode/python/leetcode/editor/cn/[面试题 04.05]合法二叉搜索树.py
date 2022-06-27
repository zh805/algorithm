# 实现一个函数，检查一棵二叉树是否为二叉搜索树。示例 1: 输入:     2    / \   1   3 输出: true 示例 2: 输入:     5
#     / \   1   4      / \     3   6 输出: false 解释: 输入为: [5,1,4,null,null,3,6]。    
#   根节点的值为 5 ，但是其右子节点值为 4 。 👍 68 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        方法1：遍历
        root大于左子树的所有节点，即左子树最大值是root.val
        root小于右子树的所有节点，即右子树最小值是root.val
        :param root:
        :return:
        """

        # def traverse(root, min_val=float('-inf'), max_val=float('inf')):
        #     if not root:
        #         return True
        #
        #     if root.val <= max_val or root.val >= max_val:
        #         return False
        #
        #     if not traverse(root.right, root.val, max_val):
        #         return False
        #     if not traverse(root.left, min_val, root.val):
        #         return False
        #
        #     return True
        #
        # return traverse(root)

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        return helper(root)

# leetcode submit region end(Prohibit modification and deletion)
