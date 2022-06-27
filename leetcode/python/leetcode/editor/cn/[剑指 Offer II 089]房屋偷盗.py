# 一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响小偷偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被
# 小偷闯入，系统会自动报警。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组 nums ，请计算 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 400 
#  
# 
#  
# 
#  注意：本题与主站 198 题相同： https://leetcode-cn.com/problems/house-robber/ 
#  Related Topics 数组 动态规划 👍 12 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        方法1：动态规划
        dp，dp[i]为偷完第i个房子时获得的最高金额。
        当前房子可能偷也可能不偷，共两种情况，取最大值: 1)从偷过的最大值的地方，再投当前房子。 2）只偷到上一个房子
        状态转移方程：dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        :param nums:
        :return:
        """
        # dp 第0位：只偷第一个房子，第1位：偷前两个房子中钱最多的。
        dp = [nums[0], max(nums[0:2])] + [0 for _ in range(len(nums) - 2)]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]

    # def rob(self, nums: List[int]) -> int:
    #     """
    #     方法2：动态规划，优化空间
    #     dp[n] = max(dp[n-1], dp[n-2] + num)
    #     :param nums:
    #     :return:
    #     """
    #     a, b, res = 0, 0, 0
    #     for num in nums:
    #         res = max(b, a + num)
    #         a, b = b, res
    #     return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1]
    # nums = [2, 1, 1, 2]
    # nums = [1, 2, 3, 1]
    # nums = [2, 7, 9, 3, 1]
    result = Solution().rob(nums)
    print(result)
