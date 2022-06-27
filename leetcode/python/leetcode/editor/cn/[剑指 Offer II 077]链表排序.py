# 给定链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
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
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
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
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
# 
#  
# 
#  注意：本题与主站 148 题相同：https://leetcode-cn.com/problems/sort-list/ 
#  Related Topics 链表 双指针 分治 排序 归并排序 👍 28 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def sortList(self, head: ListNode) -> ListNode:
    #     """
    #     方法1：内置排序算法。
    #     把链表节点放入list，排序后再按顺序连接在一起
    #     :param head:
    #     :return:
    #     """
    #     node_list = []
    #     while head:
    #         node_list.append(head)
    #         head = head.next
    # 
    #     node_list.sort(key=lambda node: node.val)
    # 
    #     dummy = ListNode()
    #     new_node = dummy
    #     for node in node_list:
    #         node.next = None
    #         new_node.next = node
    # 
    #         new_node = new_node.next
    #     return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        """
        方法2：归并排序。
        可拆解为3个小问题：1）找链表中间节点   2）合并两个有序链表   3）归并排序
        :param head: 
        :return: 
        """
        if not head or not head.next:
            return head
        head1 = head
        head2 = self.find_middle(head)

        head1 = self.sortList(head1)
        head2 = self.sortList(head2)

        return self.merge_list(head1, head2)

    def find_middle(self, head: ListNode) -> ListNode:
        """
        找链表的中间节点（快慢指针）
        :param head: 
        :return: 
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 把链表打断，返回第二个链表的头
        head2 = slow.next
        slow.next = None
        return head2

    def merge_list(self, head1: ListNode, head2: ListNode) -> ListNode:
        """
        合并两个有序链表
        :param head1: 
        :param head2: 
        :return: 
        """
        dummy = ListNode()
        cur = dummy
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        cur.next = head1 if head1 else head2
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
