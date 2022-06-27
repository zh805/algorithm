# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。 
# 
#  请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。 
# 
#  假设每一种面额的硬币有无限个。 
# 
#  题目数据保证结果符合 32 位带符号整数。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：amount = 5, coins = [1, 2, 5]
# 输出：4
# 解释：有四种方式可以凑成总金额：
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#  
# 
#  示例 2： 
# 
#  
# 输入：amount = 3, coins = [2]
# 输出：0
# 解释：只用面额 2 的硬币不能凑成总金额 3 。
#  
# 
#  示例 3： 
# 
#  
# 输入：amount = 10, coins = [10] 
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 300 
#  1 <= coins[i] <= 5000 
#  coins 中的所有值 互不相同 
#  0 <= amount <= 5000 
#  
#  👍 734 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def change(self, amount: int, coins: List[int]) -> int:
    #     """
    #     方法1：动态规划，完全背包问题。
    #     :param amount:
    #     :param coins:
    #     :return:
    #     """
    #     # dp[i][j] 表示只是用前i个硬币能凑出金额j的方案数。
    #     # dp[...][0] = 1
    #     n = len(coins)
    #     dp = [[0 for _ in range(amount + 1)] for i in range(n+1)]
    #     for i in range(n+1):
    #         dp[i][0] = 1
    #
    #     for i in range(1, n+1):
    #         for j in range(1, amount+1):
    #             if j - coins[i-1] >= 0:
    #                 # 能放进去 1) 不放 2)放
    #                 dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
    #             else:
    #                 # 放不进去
    #                 dp[i][j] = dp[i-1][j]
    #     return dp[n][amount]

    # def change(self, amount: int, coins: List[int]) -> int:
    #     """
    #     方法2：动态规划，完全背包问题。优化为一维数组。
    #     :param amount:
    #     :param coins:
    #     :return:
    #     """
    #     # dp[i][j] 表示只是用前i个硬币能凑出金额j的方案数。
    #     # dp[...][0] = 1
    #     n = len(coins)
    #     dp = [0 for _ in range(amount + 1)]
    #     dp[0] = 1
    #
    #     for i in range(0, n):
    #         for j in range(1, amount + 1):
    #             if j - coins[i] >= 0:
    #                 # 能放进去 1) 不放 2)放
    #                 dp[j] = dp[j] + dp[j - coins[i]]
    #     return dp[amount]

    def change(self, amount: int, coins: List[int]) -> int:
        """
        方法3：动态规划
        :param amount:
        :param coins:
        :return:
        """
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j-coin]
        return dp[amount]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    result = Solution().change(amount, coins)
    print(result)
