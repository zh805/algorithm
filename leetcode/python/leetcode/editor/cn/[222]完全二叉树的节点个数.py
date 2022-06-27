# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。 
# 
#  完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层
# 为第 h 层，则该层包含 1~ 2ʰ 个节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,2,3,4,5,6]
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目范围是[0, 5 * 10⁴] 
#  0 <= Node.val <= 5 * 10⁴ 
#  题目数据保证输入的树是 完全二叉树 
#  
# 
#  
# 
#  进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？ 
#  👍 623 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def countNodes(self, root: TreeNode) -> int:
    #     """
    #     方法1：遍历 O(N)
    #     :param root:
    #     :return:
    #     """
    #     if not root:
    #         return 0
    #     return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes(self, root: TreeNode) -> int:
        """
        方法2：满二叉树节点数： 2**depth - 1
        递归时，看左右子树是否是满二叉树
        :param root:
        :return:
        """
        if not root:
            return 0
        l, r = 0, 0
        left, right = root, root
        while left:
            l += 1
            left = left.left

        while right:
            r += 1
            right = right.right

        if l == r:
            return 2 ** l - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)



# leetcode submit region end(Prohibit modification and deletion)
