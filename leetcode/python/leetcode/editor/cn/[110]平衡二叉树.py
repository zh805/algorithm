# 给定一个二叉树，判断它是否是高度平衡的二叉树。 
# 
#  本题中，一棵高度平衡二叉树定义为： 
# 
#  
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：root = []
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数在范围 [0, 5000] 内 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  👍 1177 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        方法1：DFS
        """
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        if not root:
            return True
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        return abs(left_depth-right_depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# leetcode submit region end(Prohibit modification and deletion)
