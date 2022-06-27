# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
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
# 输出：[1,2]
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
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 730 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         """
#         方法1：递归
#         :param root:
#         :return:
#         """
#         result = []
#         self.preorder(root, result)
#         return result
#
#     def preorder(self, node: Optional[TreeNode], res: List):
#         if not node:
#             return
#         res.append(node.val)
#         self.preorder(node.left, res)
#         self.preorder(node.right, res)

# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         """
#         方法2：递归, 闭包
#         :param root:
#         :return:
#         """
#         result = []
#
#         def preorder(node: Optional[TreeNode]):
#             if not node:
#                 return
#             result.append(node.val)
#             preorder(node.left)
#             preorder(node.right)
#
#         preorder(root)
#         return result


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        方法3：迭代；使用栈,沿着左子树遍历
        :param root:
        :return:
        """
        stack = []
        res = []
        if not root:
            return res
        stack.append(root)
        while stack:
            node = stack.pop()
            # 先存父节点的值
            res.append(node.val)
            # 先压入右节点，再压入左节点; 弹出时则可以先弹左，再弹右。
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

# leetcode submit region end(Prohibit modification and deletion)
