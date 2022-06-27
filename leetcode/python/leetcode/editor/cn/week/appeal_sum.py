# -*- coding: utf-8 -*-
#
# @Time           2022/5/1 11:40 AM
# @File           appeal_sum.py
# @Description     
# @Author         sevenhzhang
#

class Solution:
    # def appealSum(self, s: str) -> int:
    #     """
    #     方法1：遍历,超时
    #     """
    #     n = len(s)
    #     res = 0
    #
    #     for i in range(n):
    #         for j in range(i, n):
    #             res += len(set(s[i:j + 1]))
    #
    #     # print(res)
    #     return res

    # def appealSum(self, s: str) -> int:
    #     """
    #     方法2: 分类讨论。记录每个字符最近出现的位置。
    #     s[i]添加到s[:i-1]时，看s[i]是否出现过及其最近出现的位置j。s[0:i]...s[j:i],添加s[i]引力不变。
    #     """
    #     n = len(s)
    #     pre = [-1 for _ in range(26)]
    #     res = 0
    #     cur_appeal = 0
    #     for i in range(n):
    #         ch = s[i]
    #         cur_appeal += i - pre[ord(ch) - ord('a')]
    #         res += cur_appeal
    #         pre[ord(ch)-ord('a')] = i
    #     return res

    def appealSum(self, s: str) -> int:
        """
        方法3: 动态规划
        dp[i]为以s[i]结尾的子串的引力，也需要记录字符上次出现的位置。
        """
        n = len(s)
        pre = {}
        dp = [0 for _ in range(n+1)]
        for i, ch in enumerate(s):
            dp[i+1] = dp[i] + i - pre.get(ch, -1)
            pre[ch] = i
        return sum(dp)


if __name__ == '__main__':
    s = "abbca"
    # s = "code"
    result = Solution().appealSum(s)
    print(result)

