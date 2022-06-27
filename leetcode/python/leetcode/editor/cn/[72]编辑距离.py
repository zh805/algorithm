# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数 。 
# 
#  你可以对一个单词进行如下三种操作： 
# 
#  
#  插入一个字符 
#  删除一个字符 
#  替换一个字符 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#  
# 
#  示例 2： 
# 
#  
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= word1.length, word2.length <= 500 
#  word1 和 word2 由小写英文字母组成 
#  
#  👍 2145 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def minDistance(self, word1: str, word2: str) -> int:
    #     """
    #     方法1：自顶向下。备忘录
    #     """
    #     m, n = len(word1), len(word2)
    #     memo = dict()
    #
    #     def dp(i: int, j: int):
    #         """
    #         dp(i, j) : the steps of make word1[0..i]==word2[0..j]
    #         when word1[i]==word[j], do not need change, move forward
    #         """
    #         # base case
    #         # word1 为空，故需要插入word2长度的字符
    #         if i == -1:
    #             return j + 1
    #         # word2 为空，故需要删除word1长度的字符
    #         if j == -1:
    #             return i + 1
    #
    #         if (i, j) in memo:
    #             return memo[(i, j)]
    #
    #         if word1[i] == word2[j]:
    #             memo[(i, j)] = dp(i - 1, j - 1)
    #         else:
    #             memo[(i, j)] = min(dp(i - 1, j),  # 把word1[i]删除，前移i
    #                                dp(i, j - 1),  # word1[i]后边插入word2[j],因此需要前移j
    #                                dp(i - 1, j - 1),  # 把word1[i]替换成word2[j]，因此i，j都需要前移。
    #                                ) + 1
    #
    #         return memo[(i, j)]
    #
    #     return dp(m-1, n-1)

    def minDistance(self, word1: str, word2: str) -> int:
        """
        方法1：动态规划
        dp[i][j] 表示word1中前i个字符变换为word2中前j个字符需要的最小步数
        :param word1:
        :param word2:
        :return:
        """
        len1, len2 = len(word1), len(word2)
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        # base case
        # when len(word2)==0, delete the length of word1
        for i in range(len1 + 1):
            dp[i][0] = i
        # delete word2
        for j in range(len2 + 1):
            dp[0][j] = j
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    # 相同时不需修改
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],  # 把word1[i]替换成word2[j]
                                   dp[i][j-1],  # 在i后插入word2[j]
                                   dp[i-1][j]) + 1  # 删除word1[i]
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    result = Solution().minDistance(word1, word2)
    print(result)
