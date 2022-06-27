# 给定一个单链表 L 的头节点 head ，单链表 L 表示为： 
# 
#  L0 → L1 → … → Ln-1 → Ln 
# 请将其重新排列后变为： 
# 
#  L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → … 
# 
#  不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: head = [1,2,3,4]
# 输出: [1,4,2,3] 
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: head = [1,2,3,4,5]
# 输出: [1,5,2,4,3] 
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 5 * 10⁴] 
#  1 <= node.val <= 1000 
#  
# 
#  
# 
#  注意：本题与主站 143 题相同：https://leetcode-cn.com/problems/reorder-list/ 
#  Related Topics 栈 递归 链表 双指针 👍 32 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reorderList(self, head: ListNode) -> None:
    #     """
    #     Do not return anything, modify head in-place instead.
    #     """
    #     # 把所有节点存入python list,遍历重组
    #     node_list = list()
    #     node = head
    #     while node:
    #         node_list.append(node)
    #         node = node.next
    #
    #     nums = len(node_list)
    #
    #     i, j = 0, nums - 1
    #     while i < j:
    #         node_list[i].next = node_list[j]
    #         i += 1
    #
    #         if i == j:
    #             break
    #
    #         node_list[j].next = node_list[i]
    #         j -= 1
    #
    #     node_list[i].next = None

    def reorderList(self, head: ListNode) -> None:
        """
        方法2：快慢指针找到中间节点，后半部分链表逆序，然后合并链表
        :param head:
        :return:
        """
        mid = self.find_middle(head)
        l1 = head
        l2 = mid.next
        # 把链表打断
        mid.next = None
        reversed_l2 = self.reverse_list(l2)
        self.merge_list(l1, reversed_l2)

    def find_middle(self, head: ListNode) -> ListNode:
        """
        寻找中间节点
        :param head:
        :return:
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head: ListNode) -> ListNode:
        """
        反转链表
        :param head:
        :return:
        """
        pre, cur = None, head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre

    def merge_list(self, l1: ListNode, l2: ListNode) -> None:
        """
        合并两个链表
        :param l2:
        :param l1:
        :return:
        """
        while l1 and l2:
            # l1和l2的下个节点先暂存
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l1 = l1_next

            l2.next = l1_next
            l2 = l2_next

# leetcode submit region end(Prohibit modification and deletion)
