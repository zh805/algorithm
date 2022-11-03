# 给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的 重复值为
#  k 。单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence 的子串，那么重复值 k 
# 为 0 。 
# 
#  给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：sequence = "ababc", word = "ab"
# 输出：2
# 解释："abab" 是 "ababc" 的子字符串。
#  
# 
#  示例 2： 
# 
#  
# 输入：sequence = "ababc", word = "ba"
# 输出：1
# 解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
#  
# 
#  示例 3： 
# 
#  
# 输入：sequence = "ababc", word = "ac"
# 输出：0
# 解释："ac" 不是 "ababc" 的子字符串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= sequence.length <= 100 
#  1 <= word.length <= 100 
#  sequence 和 word 都只包含小写英文字母。 
#  
# 
#  👍 112 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def maxRepeating(self, sequence: str, word: str) -> int:
    #     """
    #     方法1： 暴力法
    #     """
    #     res = 0
    #     temp = word
    #     # while temp in sequence:
    #     #     res += 1
    #     #     temp += word
    #     # return res
    #
    #     while sequence.find(temp) >= 0:
    #         res += 1
    #         temp += word
    #     return res

    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        方法2：动态规划。
        f(i)为sequence以索引i结尾的字符串的最大重复值
        f(i) = f(i-m) + 1
        """
        res = 0
        n, m = len(sequence), len(word)
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            if i - m < 0:
                continue
            if sequence[i-m:i] == word:
                dp[i] = dp[i-m] + 1
                res = max(dp[i], res)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # sequence = 'ababc'
    # word = 'ab'
    sequence = 'aaabaaaabaaabaaaabaaaabaaaabaaaaba'
    word = 'aaaba'
    result = Solution().maxRepeating(sequence, word)
    print(result)
