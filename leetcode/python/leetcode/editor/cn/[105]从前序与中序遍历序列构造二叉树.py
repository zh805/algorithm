# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并
# 返回其根节点。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= preorder.length <= 3000 
#  inorder.length == preorder.length 
#  -3000 <= preorder[i], inorder[i] <= 3000 
#  preorder 和 inorder 均 无重复 元素 
#  inorder 均出现在 preorder 
#  preorder 保证 为二叉树的前序遍历序列 
#  inorder 保证 为二叉树的中序遍历序列 
#  
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 1433 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        方法1：递归
        :param preorder: 
        :param inorder: 
        :return: 
        """
        if not preorder or not inorder:
            return None

        # 1. 先构造根节点
        root_val = preorder[0]
        root = TreeNode(val=root_val)

        # 2. 中序遍历数组中，根节点左侧即左子树节点，右侧即右子树节点。
        # 找出根节点位置
        inorder_idx = inorder.index(root_val)

        # 3. 递归构造左右子树
        root.left = self.buildTree(preorder[1:inorder_idx + 1], inorder[:inorder_idx])
        root.right = self.buildTree(preorder[inorder_idx+1:], inorder[inorder_idx+1:])
        return root

# leetcode submit region end(Prohibit modification and deletion)
