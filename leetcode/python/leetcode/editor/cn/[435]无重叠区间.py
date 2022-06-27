# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重
# 叠 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
#  
# 
#  示例 2: 
# 
#  
# 输入: intervals = [ [1,2], [1,2], [1,2] ]
# 输出: 2
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
#  
# 
#  示例 3: 
# 
#  
# 输入: intervals = [ [1,2], [2,3] ]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= intervals.length <= 10⁵ 
#  intervals[i].length == 2 
#  -5 * 10⁴ <= starti < endi <= 5 * 10⁴ 
#  
#  👍 667 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     """
    #     方法1：动态规划。超时。
    #     dp[i]为以区间i为结尾，能选出的区间的最大值
    #     """
    #     n = len(intervals)
    #     intervals.sort()
    #     # print(intervals)
    #     dp = [1 for _ in range(n)]
    #
    #     for i in range(1, n):
    #         for j in range(i):
    #             if intervals[j][1] <= intervals[i][0]:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #
    #     return n - max(dp)

    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     """
    #     方法1.2：列表推导式优化1; 还超时。
    #     """
    #     dp = [1]
    #     intervals.sort()
    #     n = len(intervals)
    #     for i in range(1, n):
    #         dp.append(max((dp[j] for j in range(i) if intervals[j][1] <= intervals[i][0]), default=0) + 1)
    #     return n - max(dp)

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        方法2：贪心
        """



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    intervals = [[1, 2], [1, 2], [1, 2]]
    result = Solution().eraseOverlapIntervals(intervals)
    print(result)
