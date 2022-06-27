# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的
# 根节点的引用。 
# 
#  一般来说，删除节点可分为两个步骤： 
# 
#  
#  首先找到需要删除的节点； 
#  如果找到了，删除它。 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：root = [5,3,6,2,4,null,7], key = 3
# 输出：[5,4,6,2,null,null,7]
# 解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
# 另一个正确答案是 [5,2,6,null,4,null,7]。
# 
# 
#  
# 
#  示例 2: 
# 
#  
# 输入: root = [5,3,6,2,4,null,7], key = 0
# 输出: [5,3,6,2,4,null,7]
# 解释: 二叉树不包含值为 0 的节点
#  
# 
#  示例 3: 
# 
#  
# 输入: root = [], key = 0
# 输出: [] 
# 
#  
# 
#  提示: 
# 
#  
#  节点数的范围 [0, 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  节点值唯一 
#  root 是合法的二叉搜索树 
#  -10⁵ <= key <= 10⁵ 
#  
# 
#  
# 
#  进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。 
#  👍 648 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional, Tuple, Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        self.bfs(root)

        if not root:
            return

        def search(node: TreeNode, parent) -> Tuple[Any, Any]:
            nonlocal key
            if not node:
                return None, None
            elif node.val == key:
                return node, parent
            elif node.val < key:
                return search(node.right, node)
            else:
                return search(node.left, node)


        def find_smallest(node: TreeNode):
            if not node.left:
                return node
            return find_smallest(node.left)

        del_node, parent = search(root, None)
        # 没找到
        if not del_node:
            return root

        if parent:
            print(parent.val)
        print(del_node.val)

        if del_node == root:
            # 删除的是root
            if not del_node.right:
                return del_node.left

            smallest = find_smallest(del_node.right)
            smallest.left = del_node.left
            return del_node.right

        if del_node.val < parent.val:
            # 删除的是parent的左子节点
            # 删除点没有右子树，让其父节点指向其左子节点即可
            if not del_node.right:
                parent.left = del_node.left
                return root
            # 删除节点有右子树，右子树的最小节点的左子树指向删除节点的左子节点
            smallest = find_smallest(del_node.right)
            smallest.left = del_node.left
            # 父节点的左子树指向删除节点的右子节点
            parent.left = del_node.right
            return root
        else:
            # 删除的是parent的右子节点
            if not del_node.right:
                parent.right = del_node.left
                return root

            smallest = find_smallest(del_node.right)
            smallest.left = del_node.left
            parent.right = del_node.right
            return root

    def bfs(self, root: TreeNode):
        from collections import deque
        q = deque([root])
        res = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    res.append(node.val)
                else:
                    res.append("#")
        print(res)

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    root = TreeNode(val=5,
                    left=TreeNode(val=3,
                                  left=TreeNode(val=2),
                                  right=TreeNode(val=4)),
                    right=TreeNode(val=6,
                                   right=TreeNode(val=7)))

    result = Solution().deleteNode(root, 7)
    Solution().bfs(result)
