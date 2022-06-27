# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。 
# 
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4 
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10⁴ 
#  
#  👍 1275 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def numSquares(self, n: int) -> int:
    #     """
    #     方法1：可转化为完全背包问题，即从[1, 4, ...]的物品中，每个物品不限选择次数，装到容量为n的背包中。
    #     dp[i][j]为考虑前i个数字，所能凑出容量j的所需数字的最小数量。
    #     选0个数字i，dp[i][j] = dp[i-1][j]
    #     选1个数字i，dp[i][j] = dp[i-1][j-t*1] + 1
    #     选2个数字i，dp[i][j] = dp[i-1][j-t*2] + 2
    #     选k个数字i，dp[i][j] = dp[i-1][j-t*k] + k
    #     状态转移方程为：
    #     dp[i][j] = min(dp[i-1][j-t*k] + k), 0<=k*t<=j
    #
    #     会超时
    #     """
    #     nums = []
    #     i = 1
    #     while i * i <= n:
    #         nums.append(i * i)
    #         i += 1
    #     # print(nums)
    #
    #     l = len(nums)
    #     dp = [[0 for _ in range(n + 1)] for _ in range(l)]
    #
    #     # for j in range(n + 1):
    #     #     t = nums[0]
    #     #     k = j // t
    #     #     if k ** t == j:
    #     #         dp[0][j] = k
    #     #     else:
    #     #         dp[0][j] = -1
    #
    #     # 只选nums[0]装入背包，由于nums[0]为1，可简化以上步骤。
    #     for j in range(n + 1):
    #         dp[0][j] = j
    #
    #     for i in range(1, l):
    #         t = nums[i]
    #         for j in range(n + 1):
    #             # 不选第i个数的情况
    #             dp[i][j] = dp[i-1][j]
    #             # 选第i个数的情况
    #             k = 1
    #             while k * t <= j:
    #                 if dp[i-1][j - k*t] != -1:
    #                     dp[i][j] = min(dp[i][j], dp[i-1][j-k*t] + k)
    #                 k += 1
    #     # print(dp)
    #     return dp[l-1][n]

    # def numSquares(self, n: int) -> int:
    #     """
    #     方法1.2：优化空间
    #     """
    #     nums = []
    #     i = 1
    #     while i * i <= n:
    #         nums.append(i * i)
    #         i += 1
    #     # print(nums)
    #
    #     l = len(nums)
    #     dp = [j for j in range(n + 1)]
    #
    #     for i in range(1, l):
    #         t = nums[i]
    #         for j in range(t, n + 1):
    #             if dp[j-t] != -1:
    #                 dp[j] = min(dp[j], dp[j-t] + 1)
    #
    #     # print(dp)
    #     return dp[n]

    def numSquares(self, n: int) -> int:
        """
        方法2：动态规划
        """
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            minn = float('inf')
            j = 1
            while j * j <= i:
                minn = min(minn, dp[i - j*j])
                j += 1
            dp[i] = minn + 1

        return dp[n]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 12
    # n = 13
    # n = 7168
    result = Solution().numSquares(n)
    print(result)
