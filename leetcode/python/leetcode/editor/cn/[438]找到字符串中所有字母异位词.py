# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。 
# 
#  异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
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
#  👍 823 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     """
    #     方法1：把p全排列，然后遍历看s子串是否是异位词。 能解，但会超时。
    #     """
    #     res = []
    #     s_l, p_l = len(s), len(p)
    #     # 找出p的全排列
    #     pp = self.permunate(p)
    #     # print(pp)
    #
    #     for i in range(s_l-p_l+1):
    #         if s[i:i+p_l] in pp:
    #             res.append(i)
    #
    #     return res
    #
    # def permunate(self, p):
    #     p = sorted(p)
    #     n = len(p)
    #     used = [False for _ in range(n)]
    #     res = []
    #     path = []
    #
    #     def traceback():
    #         if len(path) == n:
    #             res.append(''.join(path[:]))
    #             return
    #
    #         for i in range(n):
    #             if used[i]:
    #                 continue
    #
    #             if i > 0 and p[i-1] == p[i] and not used[i-1]:
    #                 continue
    #
    #             used[i] = True
    #             path.append(p[i])
    #             traceback()
    #             used[i] = False
    #             path.pop()
    #
    #     traceback()
    #     return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        方法2：滑动窗口。
        先统计p中各个单词出现的次数，然后滑窗s。
        """
        s_len, p_len = len(s), len(p)

        from collections import defaultdict
        p_cnt = defaultdict(int)
        for ch in p:
            p_cnt[ch] += 1
        window = defaultdict(int)

        res = []
        left, right, matched, need = 0, 0, 0, len(p_cnt)
        while right < s_len:

            ch = s[right]
            right += 1
            if ch in p_cnt:
                window[ch] += 1
                if window[ch] == p_cnt[ch]:
                    matched += 1

            while right - left >= p_len:

                if matched == need:
                    res.append(left)

                ch_l = s[left]
                left += 1
                if ch_l in p_cnt:
                    if window[ch_l] == p_cnt[ch_l]:
                        matched -= 1
                    window[ch_l] -= 1

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # s = "cbaebabacd"
    # p = "abc"
    # s = "abab"
    # p = "ab"
    s = "cbaebabacd"
    p = "abb"
    result = Solution().findAnagrams(s, p)
    print(result)
