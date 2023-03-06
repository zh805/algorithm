# 给你一个字符串 s ，它仅包含字符 'a' 和 'b' 。 
# 
#  你可以删除 s 中任意数目的字符，使得 s 平衡 。当不存在下标对 (i,j) 满足 i < j ，且 s[i] = 'b' 的同时 s[j]= 'a' 
# ，此时认为 s 是 平衡 的。 
# 
#  请你返回使 s 平衡 的 最少 删除次数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aababbab"
# 输出：2
# 解释：你可以选择以下任意一种方案：
# 下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
# 下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "bbaaaaabb"
# 输出：2
# 解释：唯一的最优解是删除最前面两个字符。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] 要么是 'a' 要么是 'b' 。 
#  
# 
#  👍 147 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        方法1：遍历
        """
        n = len(s)
        # 从前往后数，到当前位置时a出现的次数
        a_count = [0 for _ in range(n)]
        # 从后往前数，到当前位置时b出现的次数
        b_count = [0 for _ in range(n)]
        i = 0
        while i < n:
            if s[i] == 'a':
                if i == 0:
                    a_count[i] = 1
                else:
                    a_count[i] = a_count[i-1] + 1
            else:
                if i == 0:
                    a_count[i] = 0
                else:
                    a_count[i] = a_count[i-1]

            if s[n-i-1] == 'b':
                if i == 0:
                    b_count[n-i-1] = 1
                else:
                    b_count[n-i-1] = b_count[n-i] + 1
            else:
                if i == 0:
                    b_count[n-i-1] = 0
                else:
                    b_count[n-i-1] = b_count[n-i]

            i += 1
        # 总长度减去某个位置ab出现的最大次数。
        m = max(a + b for a, b in zip(a_count, b_count))
        return n - m

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # s = "aababbab"
    s = "bbaaaaabb"
    result = Solution().minimumDeletions(s)
    print(result)
