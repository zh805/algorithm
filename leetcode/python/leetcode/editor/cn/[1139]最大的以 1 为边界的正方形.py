# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0
# 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
#  
# 
#  示例 2： 
# 
#  输入：grid = [[1,1,0,0]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 100 
#  1 <= grid[0].length <= 100 
#  grid[i][j] 为 0 或 1 
#  
# 
#  👍 127 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        """
        方法1：前缀和+枚举
        """
        m, n = len(grid), len(grid[0])
        # 每个位置下侧和右侧连续1的个数
        down = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j]:
                    down[i][j] = down[i+1][j] + 1 if i+1 < m else 1
                    right[i][j] = right[i][j+1] + 1 if j+1 < n else 1
        for k in range(min(m, n), 0, -1):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    if down[i][j] >= k and right[i][j] >= k and right[i+k-1][j] >= k and down[i][j+k-1] >= k:
                        return k*k

        return 0


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    grid = [[1, 1, 0, 0]]
    result = Solution().largest1BorderedSquare(grid)
    print(result)
