# 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: root = [5,3,6,2,4,null,7], k = 9
# 输出: true
#  
# 
#  示例 2： 
# 
#  
# 输入: root = [5,3,6,2,4,null,7], k = 28
# 输出: false
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [1, 10⁴]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  root 为二叉搜索树 
#  -10⁵ <= k <= 10⁵ 
#  
#  👍 332 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    #     """
    #     方法1：中序遍历从小到大存入数组，再从数据遍历。
    #     """
    #     if not root:
    #         return False
    #
    #     nums = []
    #
    #     def inorder(root):
    #         if not root:
    #             return
    #         inorder(root.left)
    #         nums.append(root.val)
    #         inorder(root.right)
    #
    #     inorder(root)
    #
    #     d = set()
    #     for num in nums:
    #         target = k - num
    #         if target in d:
    #             return True
    #         else:
    #             d.add(num)
    #
    #     return False


    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        方法2：中序遍历从小到大存入数组，双指针遍历。
        """
        if not root:
            return False

        nums = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)

        inorder(root)

        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s < k:
                i += 1
            elif s > k:
                j -= 1
            else:
                return True

        return False

    # def __init__(self):
    #     self.s = set()
    #
    # def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    #     """
    #     方法3：深度优先+哈希
    #     """
    #     if not root:
    #         return False
    #
    #     if k - root.val in self.s:
    #         return True
    #     else:
    #         self.s.add(root.val)
    #
    #     return self.findTarget(root.left, k) or self.findTarget(root.right, k)

# leetcode submit region end(Prohibit modification and deletion)
