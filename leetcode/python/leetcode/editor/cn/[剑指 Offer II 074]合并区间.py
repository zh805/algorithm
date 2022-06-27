# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2： 
# 
#  
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= intervals.length <= 10⁴ 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 10⁴ 
#  
# 
#  
# 
#  注意：本题与主站 56 题相同： https://leetcode-cn.com/problems/merge-intervals/ 
#  Related Topics 数组 排序 👍 13 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        方法1：排序
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda item: item[0])

        # 默认的也是按照第一位排序
        # intervals.sort()

        res = []
        for interval in intervals:
            # res为空或者新interval与res无交集，则加入res
            if not res or res[-1][1] < interval[0]:
                res.append([interval[0], interval[1]])
            else:
                # 否则更新res最后一个interval的右边界为二者最大值
                res[-1][1] = max(res[-1][1], interval[1])
        return res

# leetcode submit region end(Prohibit modification and deletion)
