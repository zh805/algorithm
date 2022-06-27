# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长连续子字符串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子字符串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子字符串是 "b"，所以其长度为 1。
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
#  示例 4: 
# 
#  
# 输入: s = ""
# 输出: 0
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
# 
#  
# 
#  注意：本题与主站 3 题相同： https://leetcode-cn.com/problems/longest-substring-without-
# repeating-characters/ 
#  Related Topics 哈希表 字符串 滑动窗口 👍 20 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        方法1：滑动窗口
        :param s:
        :return:
        """
        result = 0

        # key为字符，value为最近一次此字符出现的位置
        window = dict()
        left = 0
        # 窗口右边界持续右移，当字符出现过时，左边界移动。
        for right, c in enumerate(s):
            if c in window:
                # 当字符之前出现过时，移动左边界
                # 若left在字符最近一次出现位置的左边，则需要把left移动到此字符索引+1位置
                # 若left在字符最近一次出现位置的右边，表示重复的内容在左边界外，则left保持不动。
                left = max(left, window[c] + 1)

            result = max(result, right - left + 1)
            window[c] = right

        return result
# leetcode submit region end(Prohibit modification and deletion)
