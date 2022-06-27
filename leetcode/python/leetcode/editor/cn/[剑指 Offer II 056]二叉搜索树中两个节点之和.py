# 给定一个二叉搜索树的 根节点 root 和一个整数 k , 请判断该二叉搜索树中是否存在两个节点它们的值之和等于 k 。假设二叉搜索树中节点的值均唯一。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: root = [8,6,10,5,7,9,11], k = 12
# 输出: true
# 解释: 节点 5 和节点 7 之和等于 12
#  
# 
#  示例 2： 
# 
#  
# 输入: root = [8,6,10,5,7,9,11], k = 22
# 输出: false
# 解释: 不存在两个节点值之和为 22 的节点
#  
# 
#  
# 
#  提示： 
# 
#  
#  二叉树的节点个数的范围是 [1, 10⁴]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  root 为二叉搜索树 
#  -10⁵ <= k <= 10⁵ 
#  
# 
#  
# 
#  注意：本题与主站 653 题相同： https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/
#  
#  👍 24 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
        方法1：中序遍历，记录遍历过的节点值。遍历到当前节点时，看是否遍历过差值。
        """
        vals = set()
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack.pop()
            diff = k - node.val
            if diff in vals:
                return True
            vals.add(node.val)

            cur = node.right

        return False

    # def findTarget(self, root: TreeNode, k: int) -> bool:
    #     """
    #     方法2：递归遍历
    #     """
    #     vals = set()
    #     res = False
    #
    #     def traverse(root):
    #         if not root:
    #             return
    #         traverse(root.left)
    #         diff = k - root.val
    #         if diff in vals:
    #             nonlocal res
    #             res = True
    #             return
    #         vals.add(root.val)
    #         traverse(root.right)
    #
    #     traverse(root)
    #     return res





# leetcode submit region end(Prohibit modification and deletion)
