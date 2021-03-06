# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：[1]
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [1,2]
# 输出：[2,1]
#  
# 
#  示例 5： 
# 
#  
# 输入：root = [1,null,2]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [0, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  👍 1326 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     """
    #     方法1：递归
    #     """
    #     res = []
    #
    #     def pre(root):
    #         if not root:
    #             return
    #         pre(root.left)
    #         res.append(root.val)
    #         pre(root.right)
    #
    #     pre(root)
    #     return res


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        方法2：栈
        """
        res = []
        stack = []

        p = root
        while stack or p:
            while p:
                stack.append(p)
                p = p.left

            node = stack.pop()
            res.append(node.val)
            p = node.right
        return res

# leetcode submit region end(Prohibit modification and deletion)
