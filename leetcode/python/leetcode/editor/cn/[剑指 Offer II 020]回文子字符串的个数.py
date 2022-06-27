# 给定一个字符串 s ，请计算这个字符串中有多少个回文子字符串。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 由小写英文字母组成 
#  
# 
#  
# 
#  注意：本题与主站 647 题相同：https://leetcode-cn.com/problems/palindromic-substrings/ 
#  Related Topics 字符串 动态规划 👍 26 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        方法1：中心拓展法。从每个字符向两边拓展，找出所有的回文字符串。
        :param s:
        :return:
        """
        len_s = len(s)
        result = 0

        def calc_nums(left, right):
            nums = 0
            while left >= 0 and right < len_s:
                if s[left] == s[right]:
                    nums += 1
                    left -= 1
                    right += 1
                else:
                    break
            return nums

        for idx, c in enumerate(s):
            # 需要考虑回文字符串字符个数是奇数还是偶数
            # 奇数时
            result += calc_nums(idx, idx)
            # 偶数时
            result += calc_nums(idx, idx+1)

        return result
# leetcode submit region end(Prohibit modification and deletion)
