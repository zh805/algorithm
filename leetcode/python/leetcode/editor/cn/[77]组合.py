# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 
# 
#  你可以按 任何顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, k = 1
# 输出：[[1]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
#  👍 917 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        方法1：回溯
        元素无重不可复选
        """
        res = []
        path = []

        def traceback(start):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n+1):
                path.append(i)
                traceback(i+1)
                path.pop()

        traceback(1)
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 4
    k = 2
    result = Solution().combine(n, k)
    print(result)
