# 有效数字（按顺序）可以分成以下几个部分： 
# 
#  
#  一个 小数 或者 整数 
#  （可选）一个 'e' 或 'E' ，后面跟着一个 整数 
#  
# 
#  小数（按顺序）可以分成以下几个部分： 
# 
#  
#  （可选）一个符号字符（'+' 或 '-'） 
#  下述格式之一：
#  
#  至少一位数字，后面跟着一个点 '.' 
#  至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字 
#  一个点 '.' ，后面跟着至少一位数字 
#  
#  
#  
# 
#  整数（按顺序）可以分成以下几个部分： 
# 
#  
#  （可选）一个符号字符（'+' 或 '-'） 
#  至少一位数字 
#  
# 
#  部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7
# ", "+6e-1", "53.5e93", "-123.456e789"] 
# 
#  部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"] 
# 
#  给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "0"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "e"
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "."
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 20 
#  s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。 
#  
#  👍 298 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isNumber(self, s: str) -> bool:
        """
        方法1：遍历
        """
        if 'e' in s or 'E' in s:
            s_p = s.split('e') if 'e' in s else s.split('E')

            if len(s_p) != 2:
                return False
            if not self.is_decimal(s_p[0]) and not self.is_integer(s_p[0]):
                return False
            if not self.is_integer(s_p[1]):
                return False

        else:
            if not self.is_decimal(s) and not self.is_integer(s):
                return False
        return True

    def is_decimal(self, s):
        # 判断是否是小数
        if len(s) == 0:
            return False
        if '.' not in s:
            return False

        if s[0] == '-' or s[0] == '+':
            s = s[1:]

        s_p = s.split('.')
        if len(s_p) != 2:
            return False
        if s_p[0].isnumeric() and s_p[1] == '':
            return True
        elif s_p[0].isnumeric() and s_p[1].isnumeric():
            return True
        elif s_p[0] == '' and s_p[1].isnumeric():
            return True
        else:
            return False

    def is_integer(self, s):
        # 判断是否是整数
        if len(s) == 0:
            return False
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        if not s.isnumeric():
            return False
        else:
            return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # s = "0"
    # s = "e"
    # s = "."
    s = "+3.14"
    result = Solution().isNumber(s)
    print(s, result)

    # s_l = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    s_l = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    for s in s_l:
        result = Solution().isNumber(s)
        print(s, result)
