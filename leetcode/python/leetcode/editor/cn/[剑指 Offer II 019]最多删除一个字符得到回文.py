# 给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "aba"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abca"
# 输出: true
# 解释: 可以删除 "c" 字符 或者 "b" 字符
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "abc"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 由小写英文字母组成 
#  
# 
#  
# 
#  注意：本题与主站 680 题相同： https://leetcode-cn.com/problems/valid-palindrome-ii/ 
#  Related Topics 贪心 双指针 字符串 👍 21 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        方法1：双指针。
        :param s:
        :return:
        """
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # 只能移动一次。分别判断左指针移动一次和右指针移动一次后，剩余的字符是否为回文字符串。
                return self.is_palindrome(s, left+1, right) or self.is_palindrome(s, left, right-1)
        return True

    def is_palindrome(self, s, left, right):
        """
        判断字符串s[left: right]是否回文
        :param s:
        :param left:
        :param right:
        :return:
        """
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# leetcode submit region end(Prohibit modification and deletion)
