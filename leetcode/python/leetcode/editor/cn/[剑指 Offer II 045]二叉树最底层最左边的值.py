# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。 
# 
#  假设二叉树中至少有一个节点。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: root = [2,1,3]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: [1,2,3,4,null,5,6,null,null,7]
# 输出: 7
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [1,10⁴] 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  
# 
#  注意：本题与主站 513 题相同： https://leetcode-cn.com/problems/find-bottom-left-tree-
# value/ 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 13 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def findBottomLeftValue(self, root: TreeNode) -> int:
    #     """
    #     方法1：层序遍历
    #     :param root:
    #     :return:
    #     """
    #     from collections import deque
    #     q = deque()
    #     q.append(root)
    #     res = []
    #     while q:
    #         layer = []
    #         for _ in range(len(q)):
    #             node = q.popleft()
    #             layer.append(node.val)
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #         res.append(layer)
    #     return res[-1][0]

    def findBottomLeftValue(self, root: TreeNode) -> int:
        """
        方法1：层序遍历,改进：遍历时记录每行第一个值
        :param root:
        :return:
        """
        from collections import deque
        q = deque()
        ret = root.val
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == 0:
                    ret = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ret

# leetcode submit region end(Prohibit modification and deletion)
