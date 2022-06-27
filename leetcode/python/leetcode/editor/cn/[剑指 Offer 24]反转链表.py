# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。 
# 
#  
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/ 
#  👍 414 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     """
    #     方法1：迭代
    #     """
    #     pre, cur = None, head
    #     while cur:
    #         nxt = cur.next
    #         cur.next = pre
    #
    #         pre = cur
    #         cur = nxt
    #
    #     return pre

    def reverseList(self, head: ListNode) -> ListNode:
        """
        方法2：递归
        """
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head



# leetcode submit region end(Prohibit modification and deletion)
