# # # # 给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。 
# # # # 
# # # # 幸运数是指矩阵中满足同时下列两个条件的元素： 
# # # # 
# # # # 
# # # # 在同一行的所有元素中最小 
# # # # 在同一列的所有元素中最大 
# # # # 
# # # # 
# # # # 
# # # # 
# # # # 示例 1： 
# # # # 
# # # # 输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
# # # # 输出：[15]
# # # # 解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
# # # # 
# # # # 
# # # # 示例 2： 
# # # # 
# # # # 输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# # # # 输出：[12]
# # # # 解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
# # # # 
# # # # 
# # # # 示例 3： 
# # # # 
# # # # 输入：matrix = [[7,8],[1,2]]
# # # # 输出：[7]
# # # # 
# # # # 
# # # # 
# # # # 
# # # # 提示： 
# # # # 
# # # # 
# # # # m == mat.length 
# # # # n == mat[i].length 
# # # # 1 <= n, m <= 50 
# # # # 1 <= matrix[i][j] <= 10^5 
# # # # 矩阵中的所有元素都是不同的 
# # # # 
# # # # Related Topics 数组 矩阵 👍 73 👎 0
# # # 
# # 
# 


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        """
        方法1：遍历
        :param matrix:
        :return:
        """
        res = []
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                # if max(matrix[i][j] for i in range(len(matrix))) <= num <= min(row):
                if max(r[j] for r in matrix) == num == min(row):
                    res.append(num)
        return res

    # def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
    #     """
    #     方法2：预处理找出每行的最小数和每列的最大数。
    #     :param matrix:
    #     :return:
    #     """
    #     min_row = [min(row) for row in matrix]
    #     max_col = [max(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
    #     res = []
    #     for i, row in enumerate(matrix):
    #         for j, num in enumerate(row):
    #             if min_row[i] == max_col[j] == num:
    #                 res.append(num)
    #     return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    res = Solution().luckyNumbers(matrix)
    print(res)
