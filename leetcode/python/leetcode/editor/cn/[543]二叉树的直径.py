# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。 
# 
#  
# 
#  示例 : 
# 给定二叉树 
# 
#            1
#          / \
#         2   3
#        / \     
#       4   5    
#  
# 
#  返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。 
# 
#  
# 
#  注意：两结点之间的路径长度是以它们之间边的数目表示。 
#  👍 975 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        方法1：后续遍历。分解问题的思路。
        左子树的最大深度+右子树的最大深度+1 = 当前节点的直径
        """
        res = 0

        def max_depth(root):
            # 求节点的最大深度
            if not root:
                return 0

            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)

            # 有了左右节点的最大深度，即可计算当前节点的直径。同时更新最大直径。
            nonlocal res
            res = max(res, left_depth + right_depth)

            # 返回当前节点的最大深度
            return max(left_depth, right_depth) + 1

        max_depth(root)
        return res

# leetcode submit region end(Prohibit modification and deletion)
