# 给定一个字符串 s ，验证 s 是否是 回文串 ，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  本题中，将空字符串定义为有效的 回文串 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "A man, a plan, a canal: Panama"
# 输出: true
# 解释："amanaplanacanalpanama" 是回文串 
# 
#  示例 2: 
# 
#  
# 输入: s = "race a car"
# 输出: false
# 解释："raceacar" 不是回文串 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2 * 10⁵ 
#  字符串 s 由 ASCII 字符组成 
#  
# 
#  
# 
#  注意：本题与主站 125 题相同： https://leetcode-cn.com/problems/valid-palindrome/ 
#  Related Topics 双指针 字符串 👍 15 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        方法1：双指针，自研
        :param s:
        :return:
        """
        left, right = 0, len(s) - 1

        s = s.lower()
        pattern = re.compile('[a-z0-9]')

        while left <= right:
            if not re.match(pattern, s[left]):
                left += 1
                continue
            if not re.match(pattern, s[right]):
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

    # def isPalindrome(self, s: str) -> bool:
    #     """
    #     方法2：正则表达式。 替换非字母和数字的字符，转小写，逆序后比较。
    #     :param s:
    #     :return:
    #     """
    #     s = re.sub('[^A-Za-z0-9]', '', s).lower()
    #     return s == s[::-1]
