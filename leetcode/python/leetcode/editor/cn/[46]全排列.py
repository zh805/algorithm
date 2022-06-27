# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
#  Related Topics 数组 回溯 👍 1770 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     """
    #     方法1：回溯
    #     """
    #     res = []
    #     n = len(nums)
    #     path = []
    #
    #     def traceback(path):
    #         if len(path) == n:
    #             res.append(path[:])
    #             return
    #
    #         for i in range(n):
    #             if nums[i] in path:
    #                 continue
    #             path.append(nums[i])
    #             traceback(path)
    #             path.pop()
    #     traceback(path)
    #     return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        方法2：回溯，使用visited记录已访问过的元素。
        """
        res = []
        n = len(nums)
        visited = [False for _ in range(n)]
        path = []

        def traceback(start):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                traceback(start)
                path.pop()
                visited[i] = False

        traceback(0)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = Solution().permute(nums)
    print(result)
