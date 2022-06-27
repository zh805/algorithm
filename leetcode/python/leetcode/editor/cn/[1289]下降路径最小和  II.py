# 给你一个 n x n 整数矩阵 arr ，请你返回 非零偏移下降路径 数字和的最小值。 
# 
#  非零偏移下降路径 定义为：从 arr 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：arr = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：13
# 解释：
# 所有非零偏移下降路径包括：
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# 下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[7]]
# 输出：7
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == grid.length == grid[i].length 
#  1 <= n <= 200 
#  -99 <= grid[i][j] <= 99 
#  
#  👍 63 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def minFallingPathSum(self, grid: List[List[int]]) -> int:
    #     """
    #     方法1：动态规划,时间复杂度高 N^3
    #     :param grid:
    #     :return:
    #     """
    #     n = len(grid)
    #     dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    #     dp[0] = grid[0]
    #
    #     for i in range(1, n):
    #         for j in range(n):
    #             # 遍历上一行与当前元素不在同一列的元素
    #             val = grid[i][j]
    #             for k in range(n):
    #                 if k != j:
    #                     dp[i][j] = min(dp[i][j], dp[i-1][k] + val)
    #     # print(dp)
    #     return min(dp[n - 1])

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """
        方法2：动态规划
        遍历上一行的所有列时，只需要知道上一行的最小值和次小值即可。
        因为有可能上一行的最小值可能和下一行的元素同一列。
        :param grid:
        :return:
        """
        n = len(grid)
        first_sum, first_pos, second_sum = 0, -1, 0
        for i in range(n):
            fs, fp, ss = float('inf'), -1, float('inf')
            for j in range(n):
                cur_sum = (first_sum if first_pos != j else second_sum) + grid[i][j]
                if cur_sum < fs:
                    fs, fp, ss = cur_sum, j, fs
                elif cur_sum < ss:
                    ss = cur_sum
            first_sum, first_pos, second_sum = fs, fp, ss
        return first_sum


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # arr = [[7]]
    arr = [[-73, 61, 43, -48, -36], [3, 30, 27, 57, 10], [96, -76, 84, 59, -15], [5, -49, 76, 31, -7],
           [97, 91, 61, -46, 67]]
    result = Solution().minFallingPathSum(arr)
    print(result)
