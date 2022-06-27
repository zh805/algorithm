# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s 由英文字母、数字、符号和空格组成 
#  
#  Related Topics 哈希表 字符串 滑动窗口 👍 6915 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     """
    #     方法1：哈希
    #     :param s:
    #     :return:
    #     """
    #     # 记录每个字符出现的位置
    #     window = dict()
    #     left = -1
    #     max_len = 0
    #     for idx, c in enumerate(s):
    #         if c in window:
    #             left = max(window[c], left)
    #         window[c] = idx
    #         max_len = max(max_len, idx - left)
    #     return max_len

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     """
    #     方法2：滑动窗口
    #     :param s:
    #     :return:
    #     """
    #     res = 0
    #     s_len = len(s)
    #     char_s = set()
    #     right = -1
    #     for i in range(s_len):
    #         # 左边界向右移动，移出之前添加的元素
    #         if i != 0:
    #             char_s.remove(s[i-1])
    #         # 持续移动右边界，直到集合中出现重复元素
    #         while right+1 < s_len and s[right+1] not in char_s:
    #             right += 1
    #             char_s.add(s[right])
    #             res = max(res, right - i + 1)
    #     return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        方法3：滑动窗口
        """
        n = len(s)
        left, right = 0, 0
        # window中存每个字符出现的次数
        from collections import defaultdict
        window = defaultdict(int)
        res = 0
        while right < n:
            ch = s[right]
            right += 1
            window[ch] += 1

            while window[ch] > 1:
                ch_l = s[left]
                left += 1
                window[ch_l] -= 1

            res = max(res, right - left)

        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"
    s = "tmmzuxt"
    result = Solution().lengthOfLongestSubstring(s)
    print(result)
