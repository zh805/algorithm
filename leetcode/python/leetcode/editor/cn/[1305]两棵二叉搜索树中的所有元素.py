# 给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。. 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root1 = [2,1,4], root2 = [1,0,3]
# 输出：[0,1,1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root1 = [1,null,8], root2 = [8,1]
# 输出：[1,1,8,8]
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树的节点数在 [0, 5000] 范围内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
#  👍 91 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    #     """
    #     方法1：中序遍历出后合并
    #     """
    #     vals1, vals2 = [], []
    #
    #     def in_order(root, vals):
    #         if not root:
    #             return root
    #
    #         in_order(root.left, vals)
    #         vals.append(root.val)
    #         in_order(root.right, vals)
    #
    #     in_order(root1, vals1)
    #     in_order(root2, vals2)
    #     # print(vals1)
    #     # print(vals2)
    #     return sorted(vals1 + vals2)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        方法2：中序遍历+归并
        """
        vals1, vals2 = [], []

        def in_order(root, vals):
            if not root:
                return root

            in_order(root.left, vals)
            vals.append(root.val)
            in_order(root.right, vals)

        in_order(root1, vals1)
        in_order(root2, vals2)

        p1, n1 = 0, len(vals1)
        p2, n2 = 0, len(vals2)
        res = []
        while True:
            # 遍历到头
            if p1 == n1:
                res.extend(vals2[p2:])
                break
            if p2 == n2:
                res.extend(vals1[p1:])
                break
            if vals1[p1] <= vals2[p2]:
                res.append(vals1[p1])
                p1 += 1
            else:
                res.append(vals2[p2])
                p2 += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
