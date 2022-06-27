# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [], l2 = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  两个链表的节点数目范围是 [0, 50] 
#  -100 <= Node.val <= 100 
#  l1 和 l2 均按 非递减顺序 排列 
#  
#  Related Topics 递归 链表 👍 2200 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        方法1：遍历
        :param l1:
        :param l2:
        :return:
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        cur = dummy = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

        cur.next = l1 if l1 else l2
        return dummy.next

    def build_list(self, nums: List):
        dummy = ListNode()
        cur = dummy
        for num in nums:
            node = ListNode(num)
            cur.next = node
            cur = cur.next

        return dummy.next

    def print_list(self, head: ListNode):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(res)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    head1 = Solution().build_list(l1)
    head2 = Solution().build_list(l2)
    new_head = Solution().mergeTwoLists(head1, head2)
    Solution().print_list(new_head)

