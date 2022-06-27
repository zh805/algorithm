# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 
# 
#  请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
#  👍 1604 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     """
    #     方法1：堆
    #     """
    #     import heapq
    #     h = []
    #     for num in nums:
    #         if len(h) == k:
    #             if num >= h[0]:
    #                 heapq.heappop(h)
    #                 heapq.heappush(h, num)
    #         else:
    #             heapq.heappush(h, num)
    #     return h[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        方法1.2：堆
        """
        import heapq
        h = []
        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)
        return h[0]



# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # nums = [3,2,1,5,6,4]
    # k = 2
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    result = Solution().findKthLargest(nums, k)
    print(result)
