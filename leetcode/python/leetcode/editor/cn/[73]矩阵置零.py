# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[0].length 
#  1 <= m, n <= 200 
#  -2³¹ <= matrix[i][j] <= 2³¹ - 1 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  一个直观的解决方案是使用 O(mn) 的额外空间，但这并不是一个好的解决方案。 
#  一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。 
#  你能想出一个仅使用常量空间的解决方案吗？ 
#  
#  👍 683 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     """
    #     方法1：遍历，找出需要删除的行和列
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     del_rows = set()
    #     del_cols = set()
    #     m = len(matrix)
    #     n = len(matrix[0])
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == 0:
    #                 del_rows.add(i)
    #                 del_cols.add(j)
    #
    #     for r in del_rows:
    #         matrix[r] = [0 for _ in range(n)]
    #
    #     for col in del_cols:
    #         for i in range(m):
    #             matrix[i][col] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        方法2：遍历时找到即修改
        Do not return anything, modify matrix in-place instead.
        """
        del_rows = set()
        del_cols = set()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:

                    if i not in del_rows:
                        del_rows.add(i)
                        matrix[i] = [0 for _ in range(n)]

                    if j not in del_cols:
                        del_cols.add(j)
                        for r in range(m):
                            matrix[r][j] = 0


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
