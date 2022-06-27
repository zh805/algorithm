# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。 
# 
#  
# 
#  示例1： 
# 
#  
# 
#  
# 输入: root = [1,3,2,5,3,null,9]
# 输出: [1,3,9]
#  
# 
#  示例2： 
# 
#  
# 输入: root = [1,2,3]
# 输出: [1,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  二叉树的节点个数的范围是 [0,10⁴] 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  
#  👍 169 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        方法1：层序遍历
        :param root:
        :return:
        """
        res = []
        if not root:
            return res
        from collections import deque
        q = deque([root])
        while q:            
            layer_max = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                layer_max = max(layer_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(layer_max)
        return res

# leetcode submit region end(Prohibit modification and deletion)
