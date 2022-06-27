# 给定一棵二叉搜索树和其中的一个节点 p ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 null 。 
# 
#  节点 p 的后继是值比 p.val 大的节点中键值最小的节点，即按中序遍历的顺序节点 p 的下一个节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [2,1,3], p = 1
# 输出：2
# 解释：这里 1 的中序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [5,3,6,2,4,null,null,1], p = 6
# 输出：null
# 解释：因为给出的节点没有中序后继，所以答案就返回 null 了。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [1, 10⁴] 内。 
#  -10⁵ <= Node.val <= 10⁵ 
#  树中各节点的值均保证唯一。 
#  
# 
#  
# 
#  注意：本题与主站 285 题相同： https://leetcode-cn.com/problems/inorder-successor-in-bst/ 
# 
#  👍 27 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    #     """
    #     方法1：先遍历找到p节点
    #     """
    #     pre, cur = None, root
    #     while cur:
    #         if cur == p:
    #             break
    #         elif cur.val < p.val:
    #             cur = cur.right
    #         elif cur.val > p.val:
    #             pre, cur = cur, cur.left
    #
    #     if cur != p:
    #         return None
    #
    #     # 如果p有右子节点，则返回右子节点
    #     if cur.right:
    #         # 找右子树的最小值
    #         cur = cur.right
    #         while cur.left:
    #             cur = cur.left
    #         return cur
    #     else:
    #         # 没有右子节点，看是否有父节点
    #         return pre if pre else None

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """
        方法2：中序遍历
        """
        is_p = False
        res = None

        def traverse(root):
            if not root:
                return

            traverse(root.left)
            nonlocal is_p, res
            if is_p and res is None:
                res = root
            if root == p:
                is_p = True
            traverse(root.right)
        traverse(root)
        return res




# leetcode submit region end(Prohibit modification and deletion)
