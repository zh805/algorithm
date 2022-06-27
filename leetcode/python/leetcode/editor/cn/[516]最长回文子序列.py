# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。 
# 
#  子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由小写英文字母组成 
#  
#  👍 731 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def longestPalindromeSubseq(self, s: str) -> int:
    #     """
    #     方法1：动态规划：子串s[i..j]中最长回文子序列长度为dp[i][j]
    #     :param s:
    #     :return:
    #     """
    #     n = len(s)
    #     dp = [[0 for _ in range(n)] for _ in range(n)]
    #     for i in range(n):
    #         # base case，至少一个字符回文
    #         # 矩阵斜线上为1
    #         dp[i][i] = 1
    #
    #     # 当i>j时，肯定不存在，d[i][j] == 0,即矩阵左下部分都为0。
    #     # 当s[i] == s[j]时，长度为dp[i+1][j-1] + 2
    #     # 当s[i] != s[j]时，取dp[i][j-1], dp[i+1][j]的最大值。
    #
    #     # 为了保证计算d[i][j]时，dp[i+1][j-1]，dp[i][j-1], dp[i+1][j]都有值，则需倒序遍历i
    #     for i in range(n-1, -1, -1):
    #         for j in range(i+1, n):
    #             if s[i] == s[j]:
    #                 dp[i][j] = dp[i+1][j-1] + 2
    #             else:
    #                 dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    #     return dp[0][n-1]

    def longestPalindromeSubseq(self, s: str) -> int:
        """
        方法2：动态规划。状态压缩，二维dp矩阵投影为一维
        :param s:
        :return:
        """
        n = len(s)
        dp = [1 for _ in range(n)]

        for i in range(n-2, -1, -1):
            pre = 0
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre + 2
                else:
                    dp[j] = max(dp[j-1], dp[j])
                pre = temp
        return dp[n-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = "bbbab"
    result = Solution().longestPalindromeSubseq(s)
    print(result)
