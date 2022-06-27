# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下： 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# } 
# 
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。 
# 
#  初始状态下，所有 next 指针都被设置为 NULL。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,2,3,4,5,6,7]
# 输出：[1,#,2,3,#,4,5,6,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 
# next 指针连接，'#' 标志着每一层的结束。
#  
# 
#  
# 
#  示例 2: 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数量在 [0, 2¹² - 1] 范围内 
#  -1000 <= node.val <= 1000 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你只能使用常量级额外空间。 
#  使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 链表 二叉树 👍 678 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    #     """
    #     方法1：层序遍历
    #     :param root:
    #     :return:
    #     """
    #     if not root:
    #         return root
    #
    #     from collections import deque
    #     d = deque()
    #     d.append(root)
    #     while d:
    #         d_size = len(d)
    #         for i in range(d_size):
    #             node = d.popleft()
    #             if i != d_size - 1:
    #                 node.next = d[0]
    #
    #             if node.left:
    #                 d.append(node.left)
    #             if node.right:
    #                 d.append(node.right)
    #     return root

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        方法2：递归，前序遍历
        :param root:
        :return:
        """
        if not root:
            return root

        def connect_node(node1, node2):
            # 连接两个节点
            if not node1 or not node2:
                return

            node1.next = node2
            # 连接左右子节点
            connect_node(node1.left, node1.right)
            connect_node(node2.left, node2.right)
            # 连接node1的右子节点与node2的左子节点
            connect_node(node1.right, node2.left)

        connect_node(root.left, root.right)
        return root

# leetcode submit region end(Prohibit modification and deletion)
