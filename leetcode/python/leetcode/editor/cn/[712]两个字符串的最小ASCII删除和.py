# 给定两个字符串s1 和 s2，返回 使两个字符串相等所需删除字符的 ASCII 值的最小和 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s1 = "sea", s2 = "eat"
# 输出: 231
# 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
# 在 "eat" 中删除 "t" 并将 116 加入总和。
# 结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
#  
# 
#  示例 2: 
# 
#  
# 输入: s1 = "delete", s2 = "leet"
# 输出: 403
# 解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
# 将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
# 结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
# 如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
#  
# 
#  
# 
#  提示: 
# 
#  
#  0 <= s1.length, s2.length <= 1000 
#  s1 和 s2 由小写英文字母组成 
#  
#  👍 256 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        方法1：动态规划，LCS变种。自顶向下，备忘录。
        :param s1:
        :param s2:
        :return:
        """
        m, n = len(s1), len(s2)
        memo = {}

        def dp(i, j):
            # calculate the delete sum of s1[i..] and s2[j..]
            if i == m:
                res = 0
                while j < n:
                    res += ord(s2[j])
                    j += 1
                return res
            if j == n:
                res = 0
                while i < m:
                    res += ord(s1[i])
                    i += 1
                return res

            if (i, j) in memo:
                return memo[(i, j)]

            if s1[i] == s2[j]:
                memo[(i, j)] = dp(i+1, j+1)
            else:
                memo[(i, j)] = min(dp(i+1, j) + ord(s1[i]),
                                   dp(i, j+1) + ord(s2[j]))
            return memo[(i, j)]

        return dp(0, 0)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # s1 = "sea"
    # s2 = "eat"
    s1 = "delete"
    s2 = "leet"
    result = Solution().minimumDeleteSum(s1, s2)
    print(result)
