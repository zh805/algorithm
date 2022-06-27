# 给定一个链表的 头节点 head ，请判断其是否为回文链表。 
# 
#  如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: head = [1,2,3,3,2,1]
# 输出: true 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入: head = [1,2]
# 输出: false
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表 L 的长度范围为 [1, 10⁵] 
#  0 <= node.val <= 9 
#  
# 
#  
# 
#  进阶：能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
# 
#  
# 
#  注意：本题与主站 234 题相同：https://leetcode-cn.com/problems/palindrome-linked-list/ 
#  Related Topics 栈 递归 链表 双指针 👍 27 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def isPalindrome(self, head: ListNode) -> bool:
    #     """
    #     方法1：遍历存入list，逆序后相同。（空间复杂度o(n)，不够优秀）
    #     :param head:
    #     :return:
    #     """
    #     cur = head
    #     val_list = list()
    #     while cur:
    #         val_list.append(cur.val)
    #         cur = cur.next
    #     return val_list == val_list[::-1]

    def isPalindrome(self, head: ListNode) -> bool:
        """
        方法2：双指针找出中间节点，然后逆序链表后半部分，最后比较两个链表。
        :param head:
        :return:
        """
        l1 = head
        mid = self.find_middle(head)
        l2 = mid.next

        l2 = self.reverse_list(l2)

        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        # 比较完后把链表恢复原状
        mid.next = self.reverse_list(l2)

        return True

    def find_middle(self, head: ListNode) -> ListNode:
        """
        寻找链表中间节点。
        节点数为偶数时，如（0，1，2，3），返回的中间节点为 1；
        节点数为奇数时，如(0, 1, 2, 3, 4),返回的中间节点为 2；
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
            node_next = cur.next
            cur.next = pre
            pre = cur
            cur = node_next
        return pre

# leetcode submit region end(Prohibit modification and deletion)
