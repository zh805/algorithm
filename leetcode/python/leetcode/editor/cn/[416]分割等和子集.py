# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
#  👍 1167 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def canPartition(self, nums: List[int]) -> bool:
    #     """
    #     方法1.1：转换为背包问题。
    #     target = sum(nums) / 2 ，即能否从nums中挑选物品塞满容量为target的背包
    #     dp[i][j]考虑前i个数字，其数字总和不超过j的最大价值。若最大价值为target，则满足。
    #     """
    #     n = len(nums)
    #     s = sum(nums)
    #     if s % 2 == 1:
    #         return False
    #     target = s // 2
    #     dp = [[0 for _ in range(target + 1)] for _ in range(n)]
    #
    #     # 初始化base case
    #     # 选第一件商品，看能否装进容量为j的背包。
    #     for j in range(target + 1):
    #         dp[0][j] = nums[0] if j >= nums[0] else 0
    #
    #     for i in range(1, n):
    #         num = nums[i]
    #         for j in range(target+1):
    #             # 商品比背包容量大，装不进去。
    #             if j < num:
    #                 dp[i][j] = dp[i-1][j]
    #             else:
    #                 # 能装进去，可以选择装，也可以不装
    #                 dp[i][j] = max(dp[i-1][j], dp[i-1][j - num] + num)
    #
    #     # print(dp)
    #     return dp[-1][-1] == target

    # def canPartition(self, nums: List[int]) -> bool:
    #     """
    #     方法1.2：转换为背包问题。空间优化，滚动数组方式。
    #     """
    #     n = len(nums)
    #     s = sum(nums)
    #     if s % 2 == 1:
    #         return False
    #     target = s // 2
    #     dp = [[0 for _ in range(target + 1)] for _ in range(2)]
    #
    #     # 初始化base case
    #     # 选第一件商品，看能否装进容量为j的背包。
    #     for j in range(target + 1):
    #         dp[0][j] = nums[0] if j >= nums[0] else 0
    #
    #     for i in range(1, n):
    #         num = nums[i]
    #         for j in range(1, target+1):
    #             # 商品比背包容量大，装不进去。
    #             if j < num:
    #                 dp[i & 1][j] = dp[(i-1) & 1][j]
    #             else:
    #                 # 能装进去，可以选择装，也可以不装
    #                 dp[i & 1][j] = max(dp[(i-1) & 1][j], dp[(i-1) & 1][j - num] + num)
    #
    #     # print(dp)
    #     return dp[(n-1) & 1][-1] == target

    def canPartition(self, nums: List[int]) -> bool:
        """
        方法1.3：转换为背包问题。空间优化，一维。
        """
        n = len(nums)
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        dp = [0 for _ in range(target + 1)]

        for i in range(1, n):
            num = nums[i]
            # 倒着遍历
            for j in range(target, -1, -1):
                # 不选第i个物品
                no = dp[j]
                # 选第i个物品
                yes = dp[j-num] + num if j >= num else 0
                dp[j] = max(yes, no)

        # print(dp)
        return dp[target] == target

    # def canPartition(self, nums: List[int]) -> bool:
    #     """
    #     方法2：动态规划，可转化为背包问题，即能否找到和为 sum(nums) 一半的子数组。
    #     :param nums:
    #     :return:
    #     """
    #     # dp[i][j]值为True或False，表示选取前i个数字，能否填满容量为j的背包。
    #     # base case dp[0][j]=False,没有装故填不满。dp[i][0]=True，背包没有容量，就是满。
    #
    #     total = sum(nums)
    #     if total % 2 != 0:
    #         return False
    #
    #     target = total // 2
    #
    #     n = len(nums)
    #     dp = [[False for _ in range(target+1)] for _ in range(n+1)]
    #     for i in range(n+1):
    #         dp[i][0] = True
    #
    #     for i in range(1, n+1):
    #         for j in range(1, target+1):
    #             if j - nums[i-1] < 0:
    #                 # 背包容量不足，不能装入第i件物品
    #                 dp[i][j] = dp[i-1][j]
    #             else:
    #                 # 装入或者不装入
    #                 dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    #
    #     return dp[-1][-1]

    # def canPartition(self, nums: List[int]) -> bool:
    #     """
    #     方法3：动态规划，二维压缩为一维
    #     :param nums:
    #     :return:
    #     """
    #     n = len(nums)
    #     total = sum(nums)
    #     if total % 2 == 1:
    #         return False
    #
    #     target = total // 2
    #     dp = [False for _ in range(target + 1)]
    #     dp[0] = True
    #     for i in range(n):
    #         for j in range(target, -1, -1):
    #             if j-nums[i] >= 0:
    #                 dp[j] = dp[j] or dp[j-nums[i]]
    #
    #     return dp[target]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    # nums = [1, 2, 3, 5]
    result = Solution().canPartition(nums)
    print(result)
