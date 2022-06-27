# 多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生
# 成多级数据结构，如下面的示例所示。 
# 
#  给定位于列表第一级的头节点，请扁平化列表，即将这样的多级双向链表展平成普通的双向链表，使所有结点出现在单级双链表中。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# 输出：[1,2,3,7,8,11,12,9,10,4,5,6]
# 解释：
# 
# 输入的多级列表如下图所示：
# 
# 
# 
# 扁平化后的链表如下图：
# 
# 
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,2,null,3]
# 输出：[1,3,2]
# 解释：
# 
# 输入的多级列表如下图所示：
# 
#   1---2---NULL
#   |
#   3---NULL
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  如何表示测试用例中的多级链表？ 
# 
#  以 示例 1 为例： 
# 
#  
#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL 
# 
#  序列化其中的每一级之后： 
# 
#  
# [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]
#  
# 
#  为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。 
# 
#  
# [1,2,3,4,5,6,null]
# [null,null,7,8,9,10,null]
# [null,11,12,null]
#  
# 
#  合并所有序列化结果，并去除末尾的 null 。 
# 
#  
# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12] 
# 
#  
# 
#  提示： 
# 
#  
#  节点数目不超过 1000 
#  1 <= Node.val <= 10^5 
#  
# 
#  
# 
#  注意：本题与主站 430 题相同： https://leetcode-cn.com/problems/flatten-a-multilevel-
# doubly-linked-list/ 
#  Related Topics 深度优先搜索 链表 双向链表 👍 17 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    # def flatten(self, head: 'Node') -> 'Node':
    #     """
    #     方法1：深度优先。遍历后再构建链表，构造的链表不合法，未通过。
    #     """
    #     res = []
    #     if not head:
    #         return res
    #
    #     def dfs(node):
    #         if not node:
    #             return
    #         res.append(node.val)
    #         if node.child:
    #             dfs(node.child)
    #         dfs(node.next)
    #     dfs(head)
    #
    #     dummy = Node(None, None, None, None)
    #     cur = dummy
    #     for val in res:
    #         node = Node(val, cur, None, None)
    #         cur.next = node
    #         cur = cur.next
    #
    #     return dummy.next

    # def flatten(self, head: 'Node') -> 'Node':
    #     """
    #     方法2：遍历子节点时，需要存当前node的next节点，以便遍历完子链表后再接上。
    #     """
    #
    #     def dfs(node):
    #         cur = node
    #         last = None
    #
    #         while cur:
    #             nxt = cur.next
    #             if cur.child:
    #                 # 深度优先，找到子链表的最后一个节点
    #                 child_last = dfs(cur.child)
    #
    #                 # 把当前节点与其next节点断开，连上child节点。
    #                 nxt = cur.next
    #                 cur.next = cur.child
    #                 cur.child.prev = cur
    #
    #                 # 若nxt节点不为空，把child的尾节点与其连上。
    #                 if nxt:
    #                     child_last.next = nxt
    #                     nxt.prev = child_last
    #
    #                 # child节点置空
    #                 cur.child = None
    #                 # 更新last节点
    #                 last = child_last
    #
    #             else:
    #                 last = cur
    #
    #             cur = nxt
    #
    #         # 返回尾节点，需要与父节点的next节点相连
    #         return last
    #
    #     dfs(head)
    #     return head

    def flatten(self, head: 'Node') -> 'Node':
        """
        方法2：使用栈。当node有child节点时，将其next节点压入栈。
        """
        stack = []
        cur = head
        pre = None
        while cur or stack:
            if not cur:
                cur = stack.pop()
                pre.next = cur
                cur.prev = pre

            if cur.child:
                if cur.next:
                    stack.append(cur.next)

                cur.next = cur.child
                cur.child = None
                cur.next.prev = cur

            pre = cur
            cur = cur.next

        return head



# leetcode submit region end(Prohibit modification and deletion)
