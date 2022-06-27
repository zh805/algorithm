# 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。 
# 
#  二叉搜索树的定义如下： 
# 
#  
#  任意节点的左子树中的键值都 小于 此节点的键值。 
#  任意节点的右子树中的键值都 大于 此节点的键值。 
#  任意节点的左子树和右子树都是二叉搜索树。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# 输出：20
# 解释：键值为 3 的子树是和最大的二叉搜索树。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [4,3,null,1,2]
# 输出：2
# 解释：键值为 2 的单节点子树是和最大的二叉搜索树。
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [-4,-2,-5]
# 输出：0
# 解释：所有节点键值都为负数，和最大的二叉搜索树为空。
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [2,1,3]
# 输出：6
#  
# 
#  示例 5： 
# 
#  
# 输入：root = [5,4,8,3,null,6,3]
# 输出：7
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树有 1 到 40000 个节点。 
#  每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。 
#  
#  👍 80 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        """
        方法1：后序遍历
        遍历到的当前节点，需要知道以下三点
        1）左右子树是否为BST
        2）左子树的最大值，右子树的最小值
        3）左右子树的节点值之和
        :param n:
        :return:
        """
        max_sum = 0

        def traverse(root):
            nonlocal max_sum
            if not root:
                # 是否为BST 0：否， 1：是
                # 以root为根的二叉树的所有节点的最小值
                # 以root为根的二叉树的所有节点的最大值
                # 左右子树节点值之和
                return [1, float('inf'), float('-inf'), 0]
            left = traverse(root.left)
            right = traverse(root.right)
            # 判断以root为根的二叉树是否为BST
            res = [0 for _ in range(4)]
            if left[0] and right[0] and left[2] < root.val < right[1]:
                # 是BST
                res[0] = 1
                # 计算以root为根的BST的最小值
                res[1] = min(left[1], root.val)
                # 计算以root为根的BST的最大值
                res[2] = max(right[2], root.val)
                # 计算以root为根的BST的所有节点和
                res[3] = root.val + left[3] + right[3]
                # 更新全局变量
                max_sum = max(max_sum, res[3])
            else:
                res[0] = 0
            return res

        traverse(root)
        return max_sum

# leetcode submit region end(Prohibit modification and deletion)
