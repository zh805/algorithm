# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。 
# 
#  空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。 
# 
#  示例 1: 
# 
#  
# 输入: 二叉树: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /    
#   4     
# 
# 输出: "1(2(4))(3)"
# 
# 解释: 原本将是“1(2(4)())(3())”，
# 在你省略所有不必要的空括号对之后，
# 它将是“1(2(4))(3)”。
#  
# 
#  示例 2: 
# 
#  
# 输入: 二叉树: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \  
#       4 
# 
# 输出: "1(2()(4))(3)"
# 
# 解释: 和第一个示例相似，
# 除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。
#  
#  👍 271 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def tree2str(self, root: Optional[TreeNode]) -> str:
    #     """
    #     方法1：前序遍历，递归。
    #     """
    #     res = []
    #
    #     def pre(root):
    #         if not root:
    #             return
    #         res.append(str(root.val))
    #
    #         if root.left and root.right:
    #             res.append('(')
    #             pre(root.left)
    #             res.append(')')
    #             res.append('(')
    #             pre(root.right)
    #             res.append(')')
    #
    #         elif root.left:
    #             res.append('(')
    #             pre(root.left)
    #             res.append(')')
    #
    #         elif root.right:
    #             res.append('()')
    #             res.append('(')
    #             pre(root.right)
    #             res.append(')')
    #         else:
    #             return
    #
    #     pre(root)
    #     # print(res)
    #     return ''.join(res)

    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        方法2：遍历，栈
        """
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node == '(' or node == ')':
                res.append(node)
                continue
            res.append(str(node.val))

            if node.right and node.left:
                stack.extend([')', node.right, '('])
                stack.extend([')', node.left, '('])
            elif node.left:
                stack.extend([')', node.left, '('])
            elif node.right:
                stack.extend([')', node.right, '('])
                stack.extend([')', '('])

        return ''.join(res)

# leetcode submit region end(Prohibit modification and deletion)
