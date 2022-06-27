# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。 
# 
#  换句话说，s1 的排列之一是 s2 的 子串 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#  
# 
#  示例 2： 
# 
#  
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 10⁴ 
#  s1 和 s2 仅包含小写字母 
#  
#  👍 617 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     """
    #     方法1：滑动窗口。
    #     """
    #     n1, n2 = len(s1), len(s2)
    #     if n1 > n2:
    #         return False
    #
    #     from collections import defaultdict
    #     need = defaultdict(int)
    #     for ch in s1:
    #         need[ch] += 1
    #
    #     left, right = 0, 0
    #     # 匹配上的字符个数
    #     matched = 0
    #     window = defaultdict(int)
    #     while right < n2:
    #
    #         # 把s2的前n1个字符先放入window中。
    #         while right < n1:
    #             ch = s2[right]
    #             if ch in need:
    #                 window[ch] += 1
    #                 if window[ch] == need[ch]:
    #                     matched += 1
    #             if matched == len(need):
    #                 return True
    #
    #             right += 1
    #
    #         if right == n2:
    #             return False
    #
    #         ch_l = s2[left]
    #         ch_r = s2[right]
    #
    #         if ch_l in need:
    #             if window[ch_l] == need[ch_l]:
    #                 matched -= 1
    #             window[ch_l] -= 1
    #
    #         if ch_r in need:
    #             window[ch_r] += 1
    #             if window[ch_r] == need[ch_r]:
    #                 matched += 1
    #
    #         if matched == len(need):
    #             return True
    #
    #         left += 1
    #         right += 1
    #
    #     return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        方法2：滑动窗口
        """

        n1, n2 = len(s1), len(s2)
        left, right = 0, 0

        from collections import defaultdict
        need = defaultdict(int)
        for c in s1:
            need[c] += 1

        matched = 0
        window = defaultdict(int)
        while right < n2:
            ch = s2[right]
            right += 1

            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    matched += 1

            while right - left >= n1:
                if matched == len(need):
                    return True

                ch_l = s2[left]
                left += 1
                if ch_l in need:
                    if window[ch_l] == need[ch_l]:
                        matched -= 1
                    window[ch_l] -= 1

        return False


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # s1 = "ab"
    # s2 = "eidbaooo"
    # s1 = "ab"
    # s2 = "eidboaoo"
    s1 = "a"
    s2 = "ab"
    result = Solution().checkInclusion(s1, s2)
    print(result)
