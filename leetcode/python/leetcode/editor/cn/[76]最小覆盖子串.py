# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  
# 
#  注意： 
# 
#  
#  对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。 
#  如果 s 中存在这样的子串，我们保证它是唯一的答案。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。 
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
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ 👍 1750 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        方法1：滑动窗口
        """
        from collections import defaultdict
        t_c = defaultdict(int)
        for ch in t:
            t_c[ch] += 1
        # t中不同字符的总数量，即需要全部匹配的总数。
        need = len(t_c)

        # 窗口中每个字符的数量
        w_c = defaultdict(int)

        n = len(s)
        left, right = 0, 0
        matched = 0

        # 子串的起始位置与长度
        start, length = 0, float('inf')
        while right < n:
            ch = s[right]
            if ch in t_c:
                w_c[ch] += 1
                # 若窗口中字符数量与t中相同，匹配数加一。
                if w_c[ch] == t_c[ch]:
                    matched += 1

            right += 1

            # 当窗口包含t时，右移左边界。
            while matched == need:
                if right - left < length:
                    length = right - left
                    start = left

                ch_left = s[left]
                left += 1
                if ch_left in t_c:
                    w_c[ch_left] -= 1
                    if w_c[ch_left] < t_c[ch_left]:
                        matched -= 1

        # print(start, length)
        return '' if length == float('inf') else s[start:start+length]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    result = Solution().minWindow(s, t)
    print(result)
