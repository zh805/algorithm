# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数为 n 。 
#  1 <= k <= n <= 10⁴ 
#  0 <= Node.val <= 10⁴ 
#  
# 
#  
# 
#  进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？ 
#  👍 578 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     """
    #     方法1：BST, 中序遍历，递归
    #     :param root:
    #     :param k:
    #     :return:
    #     """
    #     nodes = list()
    #
    #     def traverse(root):
    #         if not root:
    #             return
    #         traverse(root.left)
    #         nodes.append(root)
    #         traverse(root.right)
    #
    #     traverse(root)
    #     node = nodes[k-1]
    #     return node.val


    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     """
    #     方法2：中序遍历，非递归
    #     :param root:
    #     :param k:
    #     :return:
    #     """
    #     stack = []
    #     stack.append(root)
    #     nodes = []
    #     while root or stack:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #
    #         root = stack.pop()
    #         nodes.append(root)
    #         root = root.right
    #
    #     node = nodes[k-1]
    #     return node.val

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        方法3：中序遍历非递归，k递减
        :param root: 
        :param k: 
        :return: 
        """
        stack = []
        stack.append(root)
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val

            root = root.right
# leetcode submit region end(Prohibit modification and deletion)
