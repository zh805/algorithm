# 给你一个正整数 n ，生成一个包含 1 到 n² 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  
#  👍 634 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        方法1：模拟
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        i = 0
        j = n - 1
        k = n - 1
        l = 0
        num = 1
        max_num = n ** 2
        for idx in range(n, -1, -2):
            for x in range(l, j):
                matrix[i][x] = num
                num += 1
                if num > max_num:
                    return matrix

            for x in range(i, k):
                matrix[x][j] = num
                num += 1
                if num > max_num:
                    return matrix

            for x in range(j, l, -1):
                matrix[k][x] = num
                num += 1
                if num > max_num:
                    return matrix

            for x in range(k, i, -1):
                matrix[x][l] = num
                num += 1
                if num > max_num:
                    return matrix

            i += 1
            j -= 1
            k -= 1
            l += 1

        if n % 2 == 1:
            matrix[n // 2][n // 2] = n * n

        return matrix


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    n = 3
    # n = 4
    result = Solution().generateMatrix(n)
    print(result)
    for r in result:
        print(r)

