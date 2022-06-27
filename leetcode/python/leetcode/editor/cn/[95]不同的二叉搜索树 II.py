# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
#  
#  
#  Related Topics 树 二叉搜索树 动态规划 回溯 二叉树 👍 1128 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        方法1：回溯。
        """
        if n == 0:
            return []

        def helper(start, end):
            # 返回start到end组成的二叉搜索树
            res = []
            if start > end:
                return [None, ]
            for i in range(start, end+1):
                lefts = helper(start, i-1)
                rights = helper(i+1, end)

                for l in lefts:
                    for r in rights:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        res.append(node)

            return res

        return helper(1, n)



# leetcode submit region end(Prohibit modification and deletion)
