# 给定两个单词 word1 和 word2 ，返回使得 word1 和 word2 相同所需的最小步数。 
# 
#  每步 可以删除任意一个字符串中的一个字符。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: word1 = "sea", word2 = "eat"
# 输出: 2
# 解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
#  
# 
#  示例 2: 
# 
#  
# 输入：word1 = "leetcode", word2 = "etco"
# 输出：4
#  
# 
#  
# 
#  提示： 
#  
# 
#  
#  1 <= word1.length, word2.length <= 500 
#  word1 和 word2 只包含小写英文字母 
#  
#  👍 380 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def minDistance(self, word1: str, word2: str) -> int:
    #     """
    #     方法1：动态规划
    #     删除后的结果即为word1和word2的最长公共子序列,求出其lcs长度即可。
    #     :param word1:
    #     :param word2:
    #     :return:
    #     """
    #     m, n = len(word1), len(word2)
    #     dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    #     for i in range(m + 1):
    #         dp[i][0] = 0
    #     for j in range(n + 1):
    #         dp[0][j] = 0
    #
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if word1[i-1] == word2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1] + 1
    #             else:
    #                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #     # print(dp)
    #     lcs = dp[-1][-1]
    #     res = m - lcs + n - lcs
    #     return res

    def minDistance(self, word1: str, word2: str) -> int:
        """
        方法2：正向解法。
        dp[i][j] means the times that make word1[0..i]==word2[0..j]
        when word1[i] == word2[j], dp[i][j] = dp[i-1][j-1]
        when word1[i] != word2[j]:
        1)
        2)
        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # base case
        # 当word2长度为0时，直接删除word1长度的字符。
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],  # 删除word1[i]
                                   dp[i][j-1]   # 删除word2[j]
                                   ) + 1
        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # word1 = "sea"
    # word2 = "eat"
    word1 = "leetcode"
    word2 = "etco"
    result = Solution().minDistance(word1, word2)
    print(result)
