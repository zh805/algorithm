# 给定两个字符串 s 和 t 。返回 s 中包含 t 的所有字符的最短子字符串。如果 s 中不存在符合条件的子字符串，则返回空字符串 "" 。 
# 
#  如果 s 中存在多个符合条件的子字符串，返回任意一个。 
# 
#  
# 
#  注意： 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC" 
# 解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C' 
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a", t = "aa"
# 输出：""
# 解释：t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 10⁵ 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 
#  进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ 
# 
#  
# 
#  注意：本题与主站 76 题相似（本题答案不唯一）：https://leetcode-cn.com/problems/minimum-window-
# substring/ 
#  Related Topics 哈希表 字符串 滑动窗口 👍 21 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        方法1：滑动窗口
        :param s:
        :param t:
        :return:
        """
        result = ''

        len_s, len_t = len(s), len(t)
        if len_s < len_t:
            return result

        # 统计所有字符出现的频率,
        window = [0 for _ in range(ord('z') - ord('A') + 1)]

        # 字符在t中出现一次，频率+1；在s中出现一次，频率减去1；因此当window中所有值都小于等于0时，满足子串条件。
        for i in range(len_t):
            window[ord(t[i]) - ord('A')] += 1
            window[ord(s[i]) - ord('A')] -= 1

        if self.is_sub(window):
            return s[:len_t]

        left = 0
        min_length = len_s + 1
        for right in range(len_t, len_s):
            window[ord(s[right]) - ord('A')] -= 1
            while self.is_sub(window):
                # 满足子串条件时，取最小的子串长度
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left: right + 1]

                # 左边界左移，最左侧元素移出窗口；因为之前减去过1，所以移出时要再加回来。
                window[ord(s[left]) - ord('A')] += 1
                left += 1

        return result

    def is_sub(self, widow):
        """
        判断window是否包含子串
        :param widow:
        :return:
        """
        for item in widow:
            if item > 0:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
