# 给定一个链表，返回链表开始入环的第一个节点。 从链表的头节点开始沿着 next 指针进入环的第一个节点为环的入口节点。如果链表无环，则返回 null。 
# 
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，
# pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。 
# 
#  说明：不允许修改给定的链表。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围在范围 [0, 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  pos 的值为 -1 或者链表中的一个有效索引 
#  
# 
#  
# 
#  进阶：是否可以使用 O(1) 空间解决此题？ 
# 
#  
# 
#  注意：本题与主站 142 题相同： https://leetcode-cn.com/problems/linked-list-cycle-ii/ 
#  Related Topics 哈希表 链表 双指针 👍 26 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        方法1：快慢指针。
        公式计算：头结点距离环入口为a, 相遇点距离头结点距离为b，剩余半圆距离为c, （b+c）为环长度
        则 a + n(b + c) + b = 2(a + b) => a = (n-1)(b+c) + c，可得从头结点和相遇点同时出发，最终可在环入口相遇。
        :param head:
        :return:
        """
        slow, fast = head, head
        # 先找到环中的相遇点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 此时slow为相遇点
            if slow == fast:
                cur = head
                while cur != slow:
                    cur = cur.next
                    slow = slow.next
                return cur
        return None

    # def detectCycle(self, head: ListNode) -> ListNode:
    #     """
    #     方法2: 哈希表。记录每次遍历过的节点。
    #     :param head:
    #     :return:
    #     """
    #     cur = head
    #     node_set = set()
    #     while cur:
    #         if cur not in node_set:
    #             node_set.add(cur)
    #             cur = cur.next
    #         else:
    #             return cur
    #     return None

# leetcode submit region end(Prohibit modification and deletion)
