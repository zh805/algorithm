# 给定一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  nums 中的所有元素 互不相同 
#  
# 
#  
# 
#  注意：本题与主站 78 题相同： https://leetcode-cn.com/problems/subsets/ 
#  Related Topics 位运算 数组 回溯 👍 14 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     """
    #     方法1：
    #     :param nums:
    #     :return:
    #     """
    #     from itertools import combinations
    #     res = []
    #     for i in range(len(nums) + 1):
    #         for item in combinations(nums, i):
    #             res.append(list(item))
    #     return res

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     """
    #     方法2：每个元素都有 选 和 不选 两种情况。
    #     """
    #     res = []
    #     n = len(nums)
    #     path = []
    #
    #     def dfs(idx):
    #         if idx == n:
    #             res.append(path[:])
    #             return
    #
    #         # 选
    #         path.append(nums[idx])
    #         dfs(idx + 1)
    #         path.pop()
    #
    #         # 不选
    #         dfs(idx + 1)
    #
    #     dfs(0)
    #     return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        方法3：回溯
        """
        res = []

        def traceback(path, idx):
            res.append(path[:])

            for i in range(idx, len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                traceback(path, i+1)
                path.pop()

        traceback([], 0)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = Solution().subsets(nums)
    print(result)
