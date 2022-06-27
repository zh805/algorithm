# 给定两个字符串 s 和 p，找到 s 中所有 p 的 变位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。 
# 
#  变位词 指字母相同，但排列不同的字符串。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的变位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的变位词。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的变位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的变位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的变位词。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, p.length <= 3 * 10⁴ 
#  s 和 p 仅包含小写字母 
#  
# 
#  
# 
#  注意：本题与主站 438 题相同： https://leetcode-cn.com/problems/find-all-anagrams-in-a-
# string/ 
#  Related Topics 哈希表 字符串 滑动窗口 👍 12 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        方法1：滑动窗口
        :param s:
        :param p:
        :return:
        """
        result = []
        len_s, len_p = len(s), len(p)
        if len_p < len_p:
            return result
        # 统计字符串p中每个字符出现的次数
        p_num = [0 for _ in range(26)]
        for c in p:
            p_num[ord(c) - ord('a')] += 1

        window = [0 for _ in range(26)]
        for idx, c in enumerate(s):
            if idx < len_p:
                window[ord(c) - ord('a')] += 1
            else:
                # 窗口右进一个，左出一个
                window[ord(c) - ord('a')] += 1
                window[ord(s[idx-len_p]) - ord('a')] -= 1
            if p_num == window:
                result.append(idx - len_p + 1)
        return result

# leetcode submit region end(Prohibit modification and deletion)
