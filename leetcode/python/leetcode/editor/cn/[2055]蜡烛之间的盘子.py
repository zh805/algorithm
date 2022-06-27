# 给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，其中 '*' 表示一个 盘子 ，'|
# ' 表示一支 蜡烛 。 
# 
#  同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串 s[
# lefti...righti] （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在 子字符串中 左边和右边
#  都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。 
# 
#  
#  比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2 ，子字符
# 串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。 
#  
# 
#  请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  输入：s = "**|**|***|", queries = [[2,5],[5,9]]
# 输出：[2,3]
# 解释：
# - queries[0] 有两个盘子在蜡烛之间。
# - queries[1] 有三个盘子在蜡烛之间。
#  
# 
#  示例 2: 
# 
#  
# 
#  输入：s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16
# ]]
# 输出：[9,0,0,0,0]
# 解释：
# - queries[0] 有 9 个盘子在蜡烛之间。
# - 另一个查询没有盘子在蜡烛之间。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= s.length <= 10⁵ 
#  s 只包含字符 '*' 和 '|' 。 
#  1 <= queries.length <= 10⁵ 
#  queries[i].length == 2 
#  0 <= lefti <= righti < s.length 
#  
#  👍 41 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
    #     """
    #     方法1：遍历，统计每个子字符串中蜡烛间盘子的数量。 会超时。
    #     :param s:
    #     :param queries:
    #     :return:
    #     """
    #     res = []
    #     for query in queries:
    #         left, right = query[0], query[1] + 1
    #         sub = s[left: right]
    #
    #         # print(sub)
    #         # 统计子字符串s中，盘子在蜡烛中间的数量。
    #         n = len(sub)
    #         candle = []
    #         for i in range(n):
    #             if sub[i] == '|':
    #                 candle.append(i)
    #         # print(candle)
    #
    #         cnt = 0
    #         for i in range(len(candle) - 1):
    #             left, right = candle[i] + 1, candle[i+1]
    #             while left < right:
    #                 left += 1
    #                 cnt += 1
    #         # print(cnt)
    #
    #         res.append(cnt)
    #
    #     return res

    # def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
    #     """
    #     方法2：前缀和 （依然超时，需优化）
    #     1) 计算出最左侧和最右侧蜡烛的位置，中间的即为合法的盘子
    #     2）求出每个位置之前的盘子数量。
    #     :param s:
    #     :param queries:
    #     :return:
    #     """
    #     res = []
    #     pre_sum = []
    #     n = len(s)
    #     cnt = 0
    #     for i in range(n):
    #         if s[i] == '*':
    #             cnt += 1
    #         pre_sum.append(cnt)
    #
    #     for query in queries:
    #         left, right = query[0], query[1]
    #         while s[left] != '|' and left < right:
    #             left += 1
    #         while s[right] != '|' and left < right:
    #             right -= 1
    #
    #         cnt = pre_sum[right] - pre_sum[left]
    #         res.append(cnt)
    #
    #     return res

    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        方法3：前缀和。
        :param s:
        :param queries:
        :return:
        """
        n = len(s)
        preSum, sum = [0] * n, 0
        left, l = [0] * n, -1
        for i, ch in enumerate(s):
            if ch == '*':
                sum += 1
            else:
                l = i
            preSum[i] = sum
            left[i] = l

        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r

        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if x >= 0 and y >= 0 and x < y:
                ans[i] = preSum[y] - preSum[x]

        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # s = "||**||**|*"
    # queries = [[3, 8]]
    # s = "**|**|***|"
    # queries = [[2, 5], [5, 9]]
    s = "***|**|*****|**||**|*"
    queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
    result = Solution().platesBetweenCandles(s, queries)
    print(result)
