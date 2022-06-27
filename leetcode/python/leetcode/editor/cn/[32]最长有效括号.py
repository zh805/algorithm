# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ""
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3 * 10⁴ 
#  s[i] 为 '(' 或 ')' 
#  
#  
#  
#  👍 1785 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        方法1：动态规划
        思路：最值问题，思考用动态规划去解决。
        定义dp：dp[i]表示以下标i结尾的最长有效子串长度。
        base case:
        分析：when s[i] is '(', s[i] not in subs, so dp[i] = 0
        when s[i] is ')', should look s[i-1]:
        if s[i-1] is '(', then dp[i] = dp[i-2] + 2
        if s[i-1] is ')', if s[i-dp[i-1]-1] is '(', then dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        """
        if not s:
            return 0
        n = len(s)
        dp = [0 for _ in range(n)]

        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2 if i > 1 else 2
                elif s[i-1] == ')':
                    if i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                        if i - dp[i-1] >= 2:
                            dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                        else:
                            dp[i] = dp[i-1] + 2

        return max(dp)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # s = "(()"
    s = ")()())"
    result = Solution().longestValidParentheses(s)
    print(result)
