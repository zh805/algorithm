# 给你一个链表数组，每个链表都已经按升序排列。 
# 
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#  
# 
#  示例 2： 
# 
#  输入：lists = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  输入：lists = [[]]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  k == lists.length 
#  0 <= k <= 10^4 
#  0 <= lists[i].length <= 500 
#  -10^4 <= lists[i][j] <= 10^4 
#  lists[i] 按 升序 排列 
#  lists[i].length 的总和不超过 10^4 
#  
#  Related Topics 链表 分治 堆（优先队列） 归并排序 👍 1754 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     """
    #     方法2：堆。把各个链表的头结点入堆。
    #     :param lists:
    #     :return:
    #     """
    #     # 重载运算符
    #     def __lt__(a: ListNode, b: ListNode):
    #         return a.val < b.val
    #     ListNode.__lt__ = __lt__
    #
    #     import heapq
    #     min_heap = []
    #
    #     for head in lists:
    #         if head:
    #             heapq.heappush(min_heap, (head.val, head))
    #
    #     dummy = ListNode()
    #     cur = dummy
    #
    #     while min_heap:
    #         _, node = heapq.heappop(min_heap)
    #         cur.next = node
    #         if node.next:
    #             heapq.heappush(min_heap, (node.next.val, node.next))
    #         cur = cur.next
    #     return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        方法3：堆
        :param lists:
        :return:
        """
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
