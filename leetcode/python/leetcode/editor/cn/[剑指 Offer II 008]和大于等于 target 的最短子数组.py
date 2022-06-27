# 给定一个含有 n 个正整数的数组和一个正整数 target 。 
# 
#  找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长
# 度。如果不存在符合条件的子数组，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#  
# 
#  示例 2： 
# 
#  
# 输入：target = 4, nums = [1,4,4]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= target <= 10⁹ 
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁵ 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。 
#  
# 
#  
# 
#  注意：本题与主站 209 题相同：https://leetcode-cn.com/problems/minimum-size-subarray-sum/ 
# 
#  Related Topics 数组 二分查找 前缀和 滑动窗口 👍 37 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    #     """
    #     方法1：遍历，（能解，但会超时）
    #     :param target:
    #     :param nums:
    #     :return:
    #     """
    #     if sum(nums) < target:
    #         return 0
    #     nums_length = len(nums)
    #     res = nums_length
    #     for i in range(nums_length):
    #         s = 0
    #         for j in range(i, nums_length):
    #             # s = sum(nums[i:j+1])
    #             s += nums[j]
    #             if s >= target:
    #                 res = min(res, (j - i + 1))
    #     return res

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        方法2：双指针滑动窗口；右指针向右移动，窗口符合要求时，右指针右移逼近。
        :param target:
        :param nums:
        :return:
        """
        length = len(nums)
        s, left = 0, 0
        ret = float('inf')  # python最大值表示法
        for right, num in enumerate(nums):
            s += num
            while s >= target:
                ret = min(ret, (right - left + 1))
                s -= nums[left]
                left += 1
        return 0 if ret > length else ret


if __name__ == '__main__':
    # target = 7
    # nums = [2, 3, 1, 2, 4, 3]
    # target = 4
    # nums = [1, 4, 4]
    # target = 11
    # nums = [1, 1, 1, 1, 1, 1, 1, 1]
    target = 15
    nums = [1, 2, 3, 4, 5]
    res = Solution().minSubArrayLen(target, nums)
    print(res)
# leetcode submit region end(Prohibit modification and deletion)
