# 给定两个字符串 s 和 t ，编写一个函数来判断它们是不是一组变位词（字母异位词）。 
# 
#  注意：若 s 和 t 中每个字符出现的次数都相同且字符顺序不完全相同，则称 s 和 t 互为变位词（字母异位词）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "rat", t = "car"
# 输出: false 
# 
#  示例 3: 
# 
#  
# 输入: s = "a", t = "a"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s and t 仅包含小写字母 
#  
# 
#  
# 
#  进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
# 
#  
# 
#  注意：本题与主站 242 题相似（字母异位词定义不同）：https://leetcode-cn.com/problems/valid-anagram/ 
#  Related Topics 哈希表 字符串 排序 👍 13 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     """
    #     方法1：排序
    #     :param s:
    #     :param t:
    #     :return:
    #     """
    #     if len(s) != len(t) or s == t:
    #         return False
    #     return ''.join(sorted(s)) == ''.join(sorted(t))

    def isAnagram(self, s: str, t: str) -> bool:
        """
        方法2：哈希
        :param s:
        :param t:
        :return:
        """
        from collections import Counter
        if len(s) != len(t) or s == t:
            return False
        return Counter(s) == Counter(t)

# leetcode submit region end(Prohibit modification and deletion)
