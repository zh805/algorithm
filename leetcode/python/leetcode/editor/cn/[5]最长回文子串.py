# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母组成 
#  
#  Related Topics 字符串 动态规划 👍 4715 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        方法1：遍历，从当前字符向两侧扩展
        :param s:
        :return:
        """
        length = len(s)
        start, end = 0, 0

        def expand(left, right):
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(length):
            # 两种情况
            # 当前字符为中心点，向两侧扩散
            l1, r1 = expand(i, i)
            # 无中心点，当前字符和下一个字符相同，分别从左右两个字符开始扩散
            l2, r2 = expand(i, i+1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end+1]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # s = "babad"
    s = "cbbd"
    result = Solution().longestPalindrome(s)
    print(result)
