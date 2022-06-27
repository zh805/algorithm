# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树 不
# 应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。 
# 
#  所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,0,2], low = 1, high = 2
# 输出：[1,null,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# 输出：[3,2,null,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数在范围 [1, 10⁴] 内 
#  0 <= Node.val <= 10⁴ 
#  树中每个节点的值都是 唯一 的 
#  题目数据保证输入是一棵有效的二叉搜索树 
#  0 <= low <= high <= 10⁴ 
#  
#  👍 477 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        方法1：
        若当前节点root不在[low, high]中，则有两种情况
        1）root.val < low, 则root包括其左子树均小于low，需要修剪。
        2）root.val > high, 则root包括其右子树均大于high，需要修剪。
        :param root:
        :param low:
        :param high:
        :return:
        """
        if not root:
            return
        if root.val < low:
            # 情况1），返回右子树的修剪结果，相当于删除root和及其左子树。
            return self.trimBST(root.right, low, high)

        if root.val > high:
            # 情况2），返回左子树的修剪结果，相当于删除root及其右子树
            return self.trimBST(root.left, low, high)

        # [low, high]内节点不需要删除
        # 继续遍历左子树和右子树
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


# leetcode submit region end(Prohibit modification and deletion)
