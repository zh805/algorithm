# 给定一棵二叉树 root，返回所有重复的子树。 
# 
#  对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。 
# 
#  如果两棵树具有相同的结构和相同的结点值，则它们是重复的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,2,3,4,null,2,4,null,null,4]
# 输出：[[2,4],[4]] 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [2,1,1]
# 输出：[[1]] 
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：root = [2,2,2,3,null,3,null]
# 输出：[[2,3],[3]] 
# 
#  
# 
#  提示： 
# 
#  
#  树中的结点数在[1,10^4]范围内。 
#  -200 <= Node.val <= 200 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 372 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        方法1：递归，后序遍历
        :param root:
        :return:
        """
        res = []
        # 记录遍历过的路径出现的次数
        memo = dict()

        def traverse(root):
            if not root:
                return '#'

            lefts = traverse(root.left)
            rights = traverse(root.right)
            path = f'{lefts},{rights},{root.val}'
            if path not in memo:
                memo[path] = 1
            elif memo[path] == 1:
                res.append(root)
                memo[path] += 1
            return path

        traverse(root)
        return res

# leetcode submit region end(Prohibit modification and deletion)
