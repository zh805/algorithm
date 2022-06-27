# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。 
# 
#  在「杨辉三角」中，每个数是它左上方和右上方的数的和。 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  
# 
#  示例 2: 
# 
#  
# 输入: numRows = 1
# 输出: [[1]]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= numRows <= 30 
#  
#  👍 741 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        方法1：模拟
        """
        res = []
        for i in range(numRows):
            row = [0 for _ in range(i+1)]
            for j in range(i+1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    numRows = 1
    result = Solution().generate(numRows)
    print(result)
