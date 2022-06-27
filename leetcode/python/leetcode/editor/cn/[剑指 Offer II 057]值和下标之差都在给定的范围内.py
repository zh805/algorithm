# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= 
# t ，同时又满足 abs(i - j) <= k 。 
# 
#  如果存在则返回 true，不存在返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 2 * 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  0 <= k <= 10⁴ 
#  0 <= t <= 2³¹ - 1 
#  
# 
#  
# 
#  注意：本题与主站 220 题相同： https://leetcode-cn.com/problems/contains-duplicate-iii/ 
#  👍 34 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import bisect
from typing import List


class Solution:
    # def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    #     """
    #     方法1：滑动窗口,遍历。会超时。
    #     """
    #     n = len(nums)
    #     left, right = 0, 0
    #     while right < n:
    #         left = 0 if right <= k else right - k
    #         for i in range(left, right):
    #             # print(nums[right], nums[i])
    #             if abs(nums[right] - nums[i]) <= t:
    #                 return True
    #         right += 1
    #     return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        方法2：滑动窗口+有序集合
        """
        from sortedcontainers import SortedList
        window = SortedList()
        n = len(nums)

        for i in range(n):
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if 0 < idx and abs(window[idx] - window[idx - 1]) <= t:
                return True
            if idx < len(window)-1 and abs(window[idx+1] - window[idx]) <= t:
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1,2,3,1]
    k = 3
    t = 0
    # nums = [1, 0, 1, 1]
    # k = 1
    # t = 2
    # nums = [1, 5, 9, 1, 5, 9]
    # k = 2
    # t = 3

    result = Solution().containsNearbyAlmostDuplicate(nums, k, t)
    print(result)
