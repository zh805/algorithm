# 数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。 
# 
#  每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。 
# 
#  请找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：cost = [10, 15, 20]
# 输出：15
# 解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
#  
# 
#  示例 2： 
# 
#  
# 输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出：6
# 解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= cost.length <= 1000 
#  0 <= cost[i] <= 999 
#  
# 
#  
# 
#  注意：本题与主站 746 题相同： https://leetcode-cn.com/problems/min-cost-climbing-stairs/ 
# 
#  Related Topics 数组 动态规划 👍 25 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     """
    #     方法1：动态规划
    #     动态规划特点：1）问题可以分为若干步，每步都面临多个选择   2）大问题可以拆解为小问题  3）求问题的最优解   4）状态转移方程
    #     :param cost:
    #     :return:
    #     """
    #     # 楼顶为下标n
    #     # f(i)为到达第i层的最小成本，要到达第i层，可以从第i-1和i-2层到达，取最小值。
    #     # 可以从第0和1层出发，即f(0)=f(1)=0，
    #     # f(i) = min(f(i-1)+cost(i-1),f(i-2)+cost(i-2))
    #     # 记录到达每层的花费
    #     dp = [0 for _ in range(len(cost) + 1)]
    #     for i in range(2, len(cost) + 1):
    #         dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    #     return dp[-1]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        方法2：动态规划
        只需要保存到达上个和上上个楼层的最小花费即可，节省空间。
        :param cost:
        :return:
        """
        step1, step2, res = 0, 0, 0
        for i in range(2, len(cost) + 1):
            res = min(step1 + cost[i-2], step2 + cost[i-1])
            step1 = step2
            step2 = res
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    cost = [10, 15]
    # cost = [10, 15, 20]
    # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result = Solution().minCostClimbingStairs(cost)
    print(result)
