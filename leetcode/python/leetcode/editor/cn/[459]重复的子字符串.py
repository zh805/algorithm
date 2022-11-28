# 给定一个非空的字符串
#  s ，检查是否可以通过由它的一个子串重复多次构成。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abab"
# 输出: true
# 解释: 可由子串 "ab" 重复两次构成。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "aba"
# 输出: false
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "abcabcabcabc"
# 输出: true
# 解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
#  
# 
#  
# 
#  提示： 
# 
#  
#  
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 由小写英文字母组成 
#  
# 
#  👍 825 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        i = 1
        while i < n:
            if n % 1 != 0:
                i += 1
                continue
            else:
                t = n // i
                new_s = s[:i] * t
                if new_s == s:
                    return True
                else:
                    i += 1
                    continue
        return False


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = "abab"
    result = Solution().repeatedSubstringPattern(s)
    print(result)

    s = "aba"
    result = Solution().repeatedSubstringPattern(s)
    print(result)

    s = "abcabcabcabc"
    result = Solution().repeatedSubstringPattern(s)
    print(result)
