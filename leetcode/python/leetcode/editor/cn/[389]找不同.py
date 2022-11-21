# 给定两个字符串 s 和 t ，它们只包含小写字母。 
# 
#  字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。 
# 
#  请找出在 t 中被添加的字母。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "", t = "y"
# 输出："y"
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 1000 
#  t.length == s.length + 1 
#  s 和 t 只包含小写字母 
#  
# 
#  👍 366 👎 0

from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        方法1：字典
        """
        s_c, t_c = Counter(s), Counter(t)
        for k, v in t_c.items():
            if k not in s_c:
                return k
            if v != s_c[k]:
                return k

# leetcode submit region end(Prohibit modification and deletion)
