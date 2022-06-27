# 给定一个由 0 和 1 组成的矩阵 matrix ，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  注意：此题 matrix 输入格式为一维 01 字符串数组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：matrix = ["10100","10111","11111","10010"]
# 输出：6
# 解释：最大矩形如上图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = ["0"]
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：matrix = ["1"]
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：matrix = ["00"]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == matrix.length 
#  cols == matrix[0].length 
#  0 <= row, cols <= 200 
#  matrix[i][j] 为 '0' 或 '1' 
#  
# 
#  
# 
#  注意：本题与主站 85 题相同（输入参数格式不同）： https://leetcode-cn.com/problems/maximal-
# rectangle/ 
#  Related Topics 栈 数组 动态规划 矩阵 单调栈 👍 23 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        方法1：计算每行到当前元素时1的数量
        """
        res = 0
        if not matrix:
            return res
        m = len(matrix)
        n = len(matrix[0])
        pre_sum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 第一列直接赋值
                if j == 0:
                    pre_sum[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    pre_sum[i][j] = pre_sum[i][j - 1] + 1
        # print(pre_sum)

        for i in range(m):
            for j in range(n):
                if pre_sum[i][j] == 0:
                    continue
                # 计算矩形宽的最小值，以及高。
                high = 0
                width = pre_sum[i][j]
                rec = 0
                for k in range(i, -1, -1):
                    if pre_sum[k][j] == 0:
                        break
                    high += 1
                    width = min(width, pre_sum[k][j])
                    # 计算以当前元素为右下角的矩形的最大值。
                    rec = max(rec, high * width)
                res = max(rec, res)

        return res


# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     # matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
#     #           ["1", "0", "0", "1", "0"]]
#     matrix = [["0", "0", "1", "0"], ["0", "0", "1", "0"], ["0", "0", "1", "0"], ["0", "0", "1", "1"],
#               ["0", "1", "1", "1"], ["0", "1", "1", "1"], ["1", "1", "1", "1"]]
#     result = Solution().maximalRectangle(matrix)
#     print(result)
