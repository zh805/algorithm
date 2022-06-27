# 给定一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。 
# 
#  
#  
#  每条从根节点到叶节点的路径都代表一个数字： 
# 
#  
#  例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。 
#  
# 
#  计算从根节点到叶节点生成的 所有数字之和 。 
# 
#  叶节点 是指没有子节点的节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,2,3]
# 输出：25
# 解释：
# 从根到叶子节点路径 1->2 代表数字 12
# 从根到叶子节点路径 1->3 代表数字 13
# 因此，数字总和 = 12 + 13 = 25 
# 
#  示例 2： 
# 
#  
# 输入：root = [4,9,0,5,1]
# 输出：1026
# 解释：
# 从根到叶子节点路径 4->9->5 代表数字 495
# 从根到叶子节点路径 4->9->1 代表数字 491
# 从根到叶子节点路径 4->0 代表数字 40
# 因此，数字总和 = 495 + 491 + 40 = 1026
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [1, 1000] 内 
#  0 <= Node.val <= 9 
#  树的深度不超过 10 
#  
#  
#  
# 
#  
# 
#  注意：本题与主站 129 题相同： https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/ 
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 16 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def sumNumbers(self, root: TreeNode) -> int:
    #     """
    #     方法1：深度优先+分支思想
    #     :param root:
    #     :return:
    #     """
    #     path = 0
    #     if not root:
    #         return path
    #     return self.dfs(root, path)
    #
    # def dfs(self, node: TreeNode, path: int) -> int:
    #     # 遍历到了叶结点的子节点，直接返回
    #     if not node:
    #         return 0
    #     # 节点存在，加上当前节点值
    #     path = path * 10 + node.val
    #     # 节点为叶子节点，返回值
    #     if not node.left and not node.right:
    #         return path
    #     # 分治思想，左右子节点值相加
    #     return self.dfs(node.left, path) + self.dfs(node.right, path)

    # def sumNumbers(self, root: TreeNode) -> int:
    #     path = 0
    #
    #     def dfs(node, path):
    #         if not node:
    #             return 0
    #         path = path * 10 + node.val
    #         if not node.left and not node.right:
    #             return path
    #         return dfs(node.left, path) + dfs(node.right, path)
    #     return dfs(root, path)

    def sumNumbers(self, root: TreeNode) -> int:
        """
        方法2：广度优先，层序遍历
        :param root:
        :return:
        """
        from collections import deque
        # 两个队列，一个存遍历到的节点，一个存当前的和
        node_q = deque([root])
        sum_q = deque([root.val])

        res = 0
        while node_q:
            node = node_q.popleft()
            num = sum_q.popleft()
            left, right = node.left, node.right
            if not left and not right:
                # 到了叶子节点
                res += num
            else:
                if left:
                    node_q.append(left)
                    sum_q.append(num * 10 + left.val)
                if node.right:
                    node_q.append(right)
                    sum_q.append(num * 10 + right.val)
        return res

# leetcode submit region end(Prohibit modification and deletion)
