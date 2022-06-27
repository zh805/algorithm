# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：timePoints = ["23:59","00:00"]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：timePoints = ["00:00","23:59","00:00"]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= timePoints <= 2 * 10⁴ 
#  timePoints[i] 格式为 "HH:MM" 
#  
# 
#  
# 
#  注意：本题与主站 539 题相同： https://leetcode-cn.com/problems/minimum-time-difference/ 
#  Related Topics 数组 数学 字符串 排序 👍 8 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        方法1：排序
        :param timePoints:
        :return:
        """
        min_diff = 24 * 60
        one_day = 24 * 60

        if len(timePoints) > one_day:
            # 说明有重复的时间点，直接返回0
            return 0

        timePoints.sort()

        def t_m(t):
            return 60 * int(t[:2]) + int(t[-2:])

        for i in range(len(timePoints) - 1):
            t1, t2 = timePoints[i], timePoints[i + 1]
            t_diff = t_m(t2) - t_m(t1)
            min_diff = min(t_diff, min_diff)

        # 细节：需要把第一个时间加上one_day，减去最后一个时间，计算时间差
        first_last_diff = t_m(timePoints[0]) + one_day - t_m(timePoints[-1])
        return min(min_diff, first_last_diff)

# leetcode submit region end(Prohibit modification and deletion)
