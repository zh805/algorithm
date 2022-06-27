# 给定两个以升序排列的整数数组 nums1 和 nums2 , 以及一个整数 k 。 
# 
#  定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。 
# 
#  请找到和最小的 k 个数对 (u1,v1), (u2,v2) ... (uk,vk) 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
#     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
#      [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#  
# 
#  示例 3: 
# 
#  
# 输入: nums1 = [1,2], nums2 = [3], k = 3 
# 输出: [1,3],[2,3]
# 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums1.length, nums2.length <= 10⁴ 
#  -10⁹ <= nums1[i], nums2[i] <= 10⁹ 
#  nums1, nums2 均为升序排列 
#  1 <= k <= 1000 
#  
# 
#  
# 
#  注意：本题与主站 373 题相同：https://leetcode-cn.com/problems/find-k-pairs-with-smallest-
# sums/ 
#  Related Topics 数组 堆（优先队列） 👍 18 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     """
    #     方法1：暴力法：构建字典，然后排序。
    #     :param nums1:
    #     :param nums2:
    #     :param k:
    #     :return:
    #     """
    #     from collections import defaultdict
    #     d = defaultdict(list)
    #     for x in nums1:
    #         for y in nums2:
    #             d[x + y].append([x, y])
    #     d_l = sorted(d.items(), key=lambda item: item[0])
    #     res = []
    #     for item in d_l:
    #         for item_3 in item[1]:
    #             res.append(item_3)
    #             if len(res) == k:
    #                 break
    #     return res[:k]

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        方法2：堆排序
        :param nums1:
        :param nums2:
        :param k:
        :return:
        """
        import heapq
        # python内置的是小顶堆，可用于取最大的K个数；本题是和最小的K个，需要使用大顶堆。
        # 把值取负加入堆，即可实现大顶堆的效果。
        h = []
        for num1 in nums1:
            for num2 in nums2:
                s = -(num1 + num2)
                if len(h) == k:
                    if s > h[0][0]:
                        heapq.heappop(h)
                        heapq.heappush(h, (s, [num1, num2]))
                else:
                    heapq.heappush(h, (s, [num1, num2]))
        return [item[1] for item in h]

# leetcode submit region end(Prohibit modification and deletion)
