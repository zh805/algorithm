# 给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。 
# 
#  给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。 
# 
#  如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。 
# 
#  如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。 
# 
#  
# 
#  示例 1： 
# 
#  
#  
# 
#  
# 输入：head = [3,4,1], insertVal = 2
# 输出：[3,4,1,2]
# 解释：在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2 。新插入的节点应该在 1 和 3 之间，插入之后
# ，整个列表如上图所示，最后返回节点 3 。
# 
# 
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [], insertVal = 1
# 输出：[1]
# 解释：列表为空（给定的节点是 null），创建一个循环有序列表并返回这个节点。
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1], insertVal = 0
# 输出：[1,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= Number of Nodes <= 5 * 10^4 
#  -10^6 <= Node.val <= 10^6 
#  -10^6 <= insertVal <= 10^6 
#  
# 
#  
# 
#  注意：本题与主站 708 题相同： https://leetcode-cn.com/problems/insert-into-a-sorted-
# circular-linked-list/ 
#  Related Topics 链表 👍 23 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        """
        方法1：两种情况
        1）在链表内部找到插入点 cur.val <= insertVal <= cur.next.val
        2) 插入点在跳跃点，插入值比最大的大：cur.next.val < cur.val <= insertVal ，插入值比最小的值小: insertVal <= cur.next.val < cur.val
        :param head:
        :param insertVal:
        :return:
        """
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        cur = head
        # 遍历一遍，终止条件为下一个节点为head。
        while cur.next != head:
            if cur.val <= insertVal <= cur.next.val:
                break
            if (cur.val > cur.next.val) and ((insertVal <= cur.next.val) or (cur.val <= insertVal)):
                break
            cur = cur.next

        # 遍历完后未发现插入点，说明链表中值都相等，随便插入即可
        # 发现插入点，也插入cur之后即可。
        cur.next = Node(insertVal, cur.next)

        return head

# leetcode submit region end(Prohibit modification and deletion)
