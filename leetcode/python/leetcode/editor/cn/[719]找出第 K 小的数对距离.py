# 数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。 
# 
#  给你一个整数数组 nums 和一个整数 k ，数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length 。
# 返回 所有数对距离中 第 k 小的数对距离。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,3,1], k = 1
# 输出：0
# 解释：数对和对应的距离如下：
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# 距离第 1 小的数对是 (1,1) ，距离为 0 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,1,1], k = 2
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,6,1], k = 3
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  2 <= n <= 10⁴ 
#  0 <= nums[i] <= 10⁶ 
#  1 <= k <= n * (n - 1) / 2 
#  
#  👍 280 👎 0

from typing import List
import heapq

# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    # def smallestDistancePair(self, nums: List[int], k: int) -> int:
    #     """
    #     方法1：堆排序。 超时。
    #     """
    #     heap = []
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(i+1, n):
    #             heapq.heappush(heap, abs(nums[j]-nums[i]))
    #
    #     for i in range(k-1):
    #         heapq.heappop(heap)
    #
    #     return heapq.heappop(heap)

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        方法2：计数排序。超时
        """
        dis = [0 for _ in range(10 ** 6)]
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                dis[abs(nums[j]-nums[i])] += 1
        # print(dis)
        s, i = 0, -1
        while s < k and i < len(dis):
            i += 1
            s += dis[i]

        return i


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    # nums = [1, 3, 1]
    # k = 1
    # nums = [1, 6, 1]
    # k = 3
    result = Solution().smallestDistancePair(nums, k)
    print(result)
