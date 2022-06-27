# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  子数组 是数组中的一个连续部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
# 
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。 
#  👍 4448 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     """
    #     方法1：动态规划
    #     :param nums:
    #     :return:
    #     """
    #     n = len(nums)
    #     # dp[i]表示以nums[i]结尾的最大连续子数组的和。
    #     dp = [float('-inf') for _ in range(n)]
    #     dp[0] = nums[0]
    #
    #     for i in range(1, n):
    #         # nums[i]两种选择：1）自成一组  2）挂到前边的数组后边
    #         dp[i] = max(nums[i], dp[i-1]+nums[i])
    #
    #     return max(dp)

    def maxSubArray(self, nums: List[int]) -> int:
        """
        方法2：动态规划，优化空间，dp[i]只和dp[i-1]有关系
        :param nums:
        :return:
        """
        n = len(nums)
        pre = float('-inf')
        res = float('-inf')
        for i in range(n):
            cur = max(nums[i], pre + nums[i])
            pre = cur
            res = max(res, cur)
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = Solution().maxSubArray(nums)
    print(result)
