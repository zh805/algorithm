# 给定一个二维矩阵 matrix，以下类型的多个请求： 
# 
#  
#  计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。 
#  
# 
#  实现 NumMatrix 类： 
# 
#  
#  NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化 
#  int sumRegion(int row1, int col1, int row2, int col2) 返回左上角 (row1, col1) 、右下角
#  (row2, col2) 的子矩阵的元素总和。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: 
# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
# [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,
# 1,2,2],[1,2,2,4]]
# 输出: 
# [null, 8, 11, 12]
# 
# 解释:
# NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,
# 0,1,7],[1,0,3,0,5]]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 200 
#  -10⁵ <= matrix[i][j] <= 10⁵ 
#  0 <= row1 <= row2 < m 
#  0 <= col1 <= col2 < n 
#  最多调用 10⁴ 次 sumRegion 方法 
#  
# 
#  
# 
#  注意：本题与主站 304 题相同： https://leetcode-cn.com/problems/range-sum-query-2d-
# immutable/ 
#  Related Topics 设计 数组 矩阵 前缀和 👍 18 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class NumMatrix:

    # def __init__(self, matrix: List[List[int]]):
    #     self.matrix = matrix

    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     """
    #     方法1: 切分，然后计算；能解，但超时。
    #     :param row1:
    #     :param col1:
    #     :param row2:
    #     :param col2:
    #     :return:
    #     """
    #     sub_row = self.matrix[row1: row2 + 1]
    #     result = 0
    #     for row in sub_row:
    #         result += sum(row[col1: col2 + 1])
    #     return result

    # def __init__(self, matrix: List[List[int]]):
    #     """
    #     方法2: 初始化时，按行计算每行的前缀和
    #     :param matrix:
    #     """
    #     self.matrix = matrix
    #
    #     matrix_pre_sum_dict = {}
    #     for idx_row, row in enumerate(self.matrix):
    #         pre_sum = 0
    #         row_pre_sum_dict = {}
    #         for idx, num in enumerate(row):
    #             pre_sum += num
    #             row_pre_sum_dict[idx] = pre_sum
    #         matrix_pre_sum_dict[idx_row] = row_pre_sum_dict
    #     self.matrix_pre_sum_dict = matrix_pre_sum_dict
    #
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     result = 0
    #     for r in range(row1, row2 + 1):
    #         row_pre_sum_dict = self.matrix_pre_sum_dict[r]
    #         result += row_pre_sum_dict[col2] - row_pre_sum_dict[col1] + self.matrix[r][col1]
    #     return result

    def __init__(self, matrix: List[List[int]]):
        """
        方法3: 初始化时，计算每个元素的前缀和，即计算从坐标（0，0）到当前坐标的所有坐标的和。
        计算时，右下角坐标前缀和减去左上角前缀和即可。
        :param matrix:
        """
        self.matrix = matrix

        # 前缀和字典。key为(i, j)坐标，value为: (0, 0)到此坐标矩形框的和。
        matrix_pre_sum_dict = {}
        for row_idx, row in enumerate(self.matrix):
            row_pre_sum = 0
            for idx, num in enumerate(row):
                row_pre_sum += num
                matrix_pre_sum_dict[(row_idx, idx)] = row_pre_sum + matrix_pre_sum_dict.get((row_idx - 1, idx), 0)
        self.matrix_pre_sum_dict = matrix_pre_sum_dict

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 右下角最大前缀和 - 左下角 - 右上角 + （左上角多减去的）
        big = self.matrix_pre_sum_dict[(row2, col2)]
        left_down = self.matrix_pre_sum_dict.get((row2, col1 - 1), 0)
        right_up = self.matrix_pre_sum_dict.get((row1 - 1, col2), 0)
        small = self.matrix_pre_sum_dict.get((row1 - 1, col1 - 1), 0)
        result = big - left_down - right_up + small
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# leetcode submit region end(Prohibit modification and deletion)
