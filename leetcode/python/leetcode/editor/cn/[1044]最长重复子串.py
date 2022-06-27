# 给你一个字符串 s ，考虑其所有 重复子串 ：即 s 的（连续）子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。 
# 
#  返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "banana"
# 输出："ana"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abcd"
# 输出：""
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= s.length <= 3 * 10⁴ 
#  s 由小写英文字母组成 
#  
#  👍 307 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def longestDupSubstring(self, s: str) -> str:
    #     """
    #     方法1：找出所有重复的子串。n**2，超时。
    #     """
    #     res = ""
    #     # key为子串，value为子串长度
    #     sub_d = {}
    #
    #     max_len = float('-inf')
    #     for i in range(len(s)+1):
    #         for j in range(i):
    #             sub = s[j:i]
    #             # print(sub)
    #             if sub not in sub_d:
    #                 sub_d[sub] = len(sub)
    #             else:
    #                 if len(sub) > max_len:
    #                     max_len = len(sub)
    #                     res = sub
    #     return res

    def longestDupSubstring(self, s: str) -> str:
        """

        """


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = "banana"
    result = Solution().longestDupSubstring(s)
    print(result)
