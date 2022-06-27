# 请根据每日 气温 列表 temperatures ，重新生成一个列表，要求其对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不
# 会升高，请在该位置用 0 来代替。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
#  
# 
#  示例 2: 
# 
#  
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
#  
# 
#  示例 3: 
# 
#  
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= temperatures.length <= 10⁵ 
#  30 <= temperatures[i] <= 100 
#  
# 
#  
# 
#  注意：本题与主站 739 题相同： https://leetcode-cn.com/problems/daily-temperatures/ 
#  Related Topics 栈 数组 单调栈 👍 26 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     """
    #     方法1：暴力遍历; 能解，但会超时；
    #     :param temperatures:
    #     :return:
    #     """
    #     res = []
    #     for i, t in enumerate(temperatures):
    #         for j in range(i, len(temperatures)):
    #             if temperatures[j] > t:
    #                 res.append(j - i)
    #                 break
    #             elif j == len(temperatures) - 1:
    #                 res.append(0)
    #                 break
    #     return res

    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     """
    #     方法2：单调栈。此题实际上是找每个数右边第一个比它大的数，即单调栈问题。
    #     :param temperatures:
    #     :return:
    #     """
    #     ret = [0 for _ in range(len(temperatures))]
    #     # 栈中存放数组下标，栈中下标表示的温度按照降序排列。当温度大于栈顶温度时，即出栈。
    #     stack = []
    #     for idx, t in enumerate(temperatures):
    #         # 栈为空或者栈顶温度小于当前温度时，计算栈顶与当前日期的时间差，把栈顶弹出；
    #         while stack and temperatures[stack[-1]] < t:
    #             ret[stack[-1]] = idx - stack[-1]
    #             stack.pop()
    #         # 把当前温度的日期入栈。
    #         stack.append(idx)
    #     return ret

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        方法3：单调栈。倒着遍历。
        """
        n = len(temperatures)
        res = [0 for _ in range(n)]

        stack = []
        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    result = Solution().dailyTemperatures(temperatures)
    print(result)
