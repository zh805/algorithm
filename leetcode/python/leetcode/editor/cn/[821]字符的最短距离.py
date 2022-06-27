# 给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。 
# 
#  返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的
# 字符 c 的 距离 。 
# 
#  两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "loveleetcode", c = "e"
# 输出：[3,2,1,0,1,0,0,1,2,2,1,0]
# 解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
# 距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
# 距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。
# 对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
# 距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aaab", c = "b"
# 输出：[3,2,1,0]
#  
# 
#  
# 提示：
# 
#  
#  1 <= s.length <= 10⁴ 
#  s[i] 和 c 均为小写英文字母 
#  题目数据保证 c 在 s 中至少出现一次 
#  
#  👍 259 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def shortestToChar(self, s: str, c: str) -> List[int]:
    #     """
    #     方法1：遍历s，从当前字符向两边扩散去匹配c
    #     """
    #     n = len(s)
    #     res = [0 for _ in range(n)]
    #
    #     def find_c(idx):
    #         left, right = idx, idx
    #         while left >= 0 and right <= n-1:
    #             if s[left] == c:
    #                 return abs(idx-left)
    #             if s[right] == c:
    #                 return abs(idx-right)
    #             left -= 1
    #             right += 1
    #
    #         if left < 0:
    #             while right < n:
    #                 if s[right] == c:
    #                     return abs(idx-right)
    #                 right += 1
    #
    #         if right > n-1:
    #             while left >= 0:
    #                 if s[left] == c:
    #                     return abs(idx-left)
    #                 left -= 1
    #
    #     for i in range(n):
    #         if s[i] == c:
    #             continue
    #         res[i] = find_c(i)
    #
    #     return res

    # def shortestToChar(self, s: str, c: str) -> List[int]:
    #     """
    #     方法2：从s中遍历出c，将其位置保存到列表中。然后再遍历s，二分法从列表中找到最近的下标。
    #     """
    #     s_i = []
    #     for idx, ch in enumerate(s):
    #         if ch == c:
    #             s_i.append(idx)
    #
    #     n = len(s)
    #     m = len(s_i)
    #     import bisect
    #     res = [0 for _ in range(n)]
    #     for idx, ch in enumerate(s):
    #         if ch == c:
    #             continue
    #         i = bisect.bisect_left(s_i, idx)
    #         ans = float('inf')
    #         if i == 0:
    #             ans = min(ans, abs(s_i[i]-idx))
    #         elif i == m:
    #             ans = min(ans, abs(s_i[i-1]-idx))
    #         else:
    #             ans = min(abs(s_i[i]-idx), abs(s_i[i-1]-idx))
    #         res[idx] = ans
    #     return res

    def shortestToChar(self, s: str, c: str) -> List[int]:
        """
        方法3: 正反两次遍历
        """
        n = len(s)
        res = [n for _ in range(n)]

        i = -n
        for idx, ch in enumerate(s):
            if ch == c:
                i = idx
            res[idx] = idx - i

        # idx = 0
        # while idx < n:
        #     if s[idx] == c:
        #         i = idx
        #     res[idx] = idx - i
        #     idx += 1

        i = n * 2
        # for idx in range(n-1, -1, -1):
        #     if s[idx] == c:
        #         i = idx
        #     res[idx] = min(res[idx], i-idx)

        # while 循环更快
        idx = n-1
        while idx >= 0:
            if s[idx] == c:
                i = idx
            res[idx] = min(res[idx], i-idx)
            idx -= 1

        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # s = "loveleetcode"
    # c = "e"
    # s = "aaab"
    # c = "b"
    # s = 'aaba'
    # c = 'b'
    s = 'abaa'
    c = 'b'
    result = Solution().shortestToChar(s, c)
    print(result)
