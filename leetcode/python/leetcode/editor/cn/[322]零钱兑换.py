# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。 
# 
#  计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。 
# 
#  你可以认为每种硬币的数量是无限的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  
# 输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：coins = [1], amount = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 2³¹ - 1 
#  0 <= amount <= 10⁴ 
#  
#  👍 1744 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     """
    #     方法1：暴力法，超时。
    #     :param coins:
    #     :param amount:
    #     :return:
    #     """
    #     if amount == 0:
    #         return 0
    #     if amount < 0:
    #         return -1
    #     res = float('inf')
    #     for coin in coins:
    #         sub_problem = self.coinChange(coins, amount-coin)
    #         if sub_problem == -1:
    #             continue
    #         res = min(res, sub_problem + 1)
    #     return -1 if res == float('inf') else res

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     """
    #     方法2：备忘录
    #     :param coins:
    #     :param amount:
    #     :return:
    #     """
    #     memo = [999 for _ in range(amount + 1)]
    #
    #     def dp(coins, amount):
    #         if amount == 0:
    #             return 0
    #         if amount < 0:
    #             return -1
    #
    #         if memo[amount] != 999:
    #             return memo[amount]
    #
    #         res = float('inf')
    #         for coin in coins:
    #             sub_problem = dp(coins, amount-coin)
    #             if sub_problem == -1:
    #                 continue
    #             res = min(res, sub_problem + 1)
    #         memo[amount] = -1 if res == float('inf') else res
    #
    #         return memo[amount]
    #
    #     return dp(coins, amount)

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     """
    #     方法3：dp数组迭代，自底向上
    #     :param coins:
    #     :param amount:
    #     :return:
    #     """
    #     # dp[i] 表示amount为i时所需的最少硬币数量
    #     dp = [float('inf') for _ in range(amount + 1)]
    #
    #     dp[0] = 0
    #     for i in range(1, amount+1):
    #         for coin in coins:
    #             if i - coin < 0:
    #                 continue
    #             dp[i] = min(dp[i], 1 + dp[i-coin])
    #
    #     return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        方法3：完全背包，一维优化。
        :param coins:
        :param amount:
        :return:
        """
        # dp[i] 表示amount为i时所需的最少硬币数量
        dp = [float('inf') for _ in range(amount + 1)]

        n = len(coins)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(n):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 30
    result = Solution().coinChange(coins, amount)
    print(result)
