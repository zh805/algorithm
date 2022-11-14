# 给定一个非空二叉树的根节点
#  root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10⁻⁵ 以内的答案可以被接受。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[3.00000,14.50000,11.00000]
# 解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
# 因此返回 [3, 14.5, 11] 。
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入：root = [3,9,20,15,7]
# 输出：[3.00000,14.50000,11.00000]
#  
# 
#  
# 
#  提示： 
# 
#  
#  
# 
#  
#  树中节点数量在 [1, 10⁴] 范围内 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  👍 376 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque([root])
        while q:
            i, n = 0, len(q)
            tmp = 0
            while i < n:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                tmp += node.val
                i += 1
            res.append(tmp/n)
        return res

# leetcode submit region end(Prohibit modification and deletion)