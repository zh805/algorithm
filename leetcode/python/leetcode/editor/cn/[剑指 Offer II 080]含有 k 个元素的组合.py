# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2: 
# 
#  
# 输入: n = 1, k = 1
# 输出: [[1]] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
# 
#  
# 
#  注意：本题与主站 77 题相同： https://leetcode-cn.com/problems/combinations/ 
#  Related Topics 数组 回溯 👍 12 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import itertools
from typing import List


class Solution:
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     """
    #     方法1：内置itertools
    #     :param n:
    #     :param k:
    #     :return:
    #     """
    #     # res = []
    #     # nums = list(i for i in range(1, n + 1))
    #     # for item in itertools.combinations(nums, k):
    #     #     res.append(list(item))
    #     # return res
    # 
    #     return [list(item) for item in itertools.combinations((i for i in range(1, n + 1)), k)]

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        方法2：回溯法
        元素无重复不可复选，组合问题。
        :param n:
        :param k:
        :return:
        """
        res = []

        def traceback(start: int, path: List[int]):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                traceback(i + 1, path)
                path.pop()

        traceback(1, [])
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 4
    k = 2
    # n = 1
    # k = 1
    res = Solution().combine(n, k)
    print(res)
