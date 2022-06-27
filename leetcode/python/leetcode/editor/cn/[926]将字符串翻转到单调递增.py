# 如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是单调
# 递增的。 
# 
#  我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。 
# 
#  返回使 S 单调递增的最小翻转次数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "00110"
# 输出：1
# 解释：我们翻转最后一位得到 00111.
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "010110"
# 输出：2
# 解释：我们翻转得到 011111，或者是 000111。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "00011000"
# 输出：2
# 解释：我们翻转得到 00000000。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  S 中只包含字符 '0' 和 '1' 
#  
#  👍 146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        方法1：动态规划
        状态：到第i个字符时需要的翻转次数为dp[i]。after trans, s[i]will be '0' or '1'。
        so we need the second dimension to express the result of s[i].
        when s[i]为'1'，if s[i-1]is '0', need trans

        when s[i] == '1':
        not trans: dp[i][1] = min(dp[i-1][0], dp[i-1][1])
        trans '1' to '0': dp[i][0] = dp[i-1][0] + 1

        when s[i] == '0':
        trans '0' to '1': dp[i][1] = min(dp[i - 1][0], dp[i-1][1]) + 1
        not trans: dp[i][0] = dp[i-1][0]

        base case, only one char, do not need trans: dp[0][0] = 0, dp[0][1] = 0
        """
        n = len(s)
        dp = [[0 for _ in range(2)] for _ in range(n)]

        dp[0][0] = 0 if s[0] == '0' else 1
        dp[0][1] = 0 if s[0] == '1' else 1

        for i in range(1, n):
            if s[i] == '1':
                dp[i][1] = min(dp[i - 1][0], dp[i - 1][1])
                dp[i][0] = dp[i - 1][0] + 1
            elif s[i] == '0':
                dp[i][1] = min(dp[i - 1][0], dp[i-1][1]) + 1
                dp[i][0] = dp[i - 1][0]
        # print(dp)
        return min(dp[-1][0], dp[-1][1])

# leetcode submit region end(Prohibit modification and deletion)
