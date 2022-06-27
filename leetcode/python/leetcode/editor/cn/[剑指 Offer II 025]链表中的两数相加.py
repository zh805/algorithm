# 给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。 
# 
#  可以假设除了数字 0 之外，这两个数字都不会以零开头。 
# 
#  
# 
#  示例1： 
# 
#  
# 
#  
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
#  
# 
#  示例2： 
# 
#  
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
#  
# 
#  示例3： 
# 
#  
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 100] 
#  0 <= node.val <= 9 
#  输入数据保证链表代表的数字无前导 0 
#  
# 
#  
# 
#  进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。 
# 
#  
# 
#  注意：本题与主站 445 题相同：https://leetcode-cn.com/problems/add-two-numbers-ii/ 
#  Related Topics 栈 链表 数学 👍 25 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     """
    #     方法1：先反转l1和l2，相加后再反转；（能解，但不符合题目要求）
    #     :param l1:
    #     :param l2:
    #     :return:
    #     """
    #     l1_r, l2_r = self.reverse_list(l1), self.reverse_list(l2)
    #     cur_1, cur_2 = l1_r, l2_r
    #     flag = 0
    #
    #     # 哑节点留着用于取头结点
    #     dummy = ListNode()
    #     new_node = dummy
    #     while cur_1 or cur_2 or flag:
    #         v1 = cur_1.val if cur_1 else 0
    #         v2 = cur_2.val if cur_2 else 0
    #
    #         s = v1 + v2 + flag
    #         res = s % 10
    #         flag = s // 10
    #
    #         new_node.next = ListNode(res)
    #         new_node = new_node.next
    #
    #         cur_1 = cur_1.next if cur_1 else None
    #         cur_2 = cur_2.next if cur_2 else None
    #
    #     new_head = self.reverse_list(dummy.next)
    #     return new_head
    #
    # def reverse_list(self, head):
    #     """
    #     反转链表
    #     :param head:
    #     :return:
    #     """
    #     after, pre = None, head
    #     while pre:
    #         next = pre.next
    #         pre.next = after
    #
    #         after = pre
    #         pre = next
    #     return after

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        方法2：遍历l1和l2，用两个栈存节点
        :param l1:
        :param l2:
        :return:
        """
        stack_1, stack_2 = list(), list()
        cur_1, cur_2 = l1, l2
        while cur_1:
            stack_1.append(cur_1.val)
            cur_1 = cur_1.next

        while cur_2:
            stack_2.append(cur_2.val)
            cur_2 = cur_2.next

        stack_3 = list()
        flag = 0
        while stack_1 or stack_2 or flag:
            v1 = stack_1.pop() if stack_1 else 0
            v2 = stack_2.pop() if stack_2 else 0

            s = v1 + v2 + flag

            res = s % 10
            flag = s // 10
            stack_3.append(res)

        dummy = ListNode
        cur = dummy
        while stack_3:
            cur.next = ListNode(stack_3.pop())
            cur = cur.next
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
