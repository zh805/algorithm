# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
#  👍 1018 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     """
    #     方法1：回溯。
    #     全排列类型：元素重复，不可复选。
    #     """
    #     # nums.sort()
    #     res = []
    #     n = len(nums)
    #     used = [False for _ in range(n)]
    #
    #     def traceback(path: List[int]):
    #         nonlocal n
    #         if len(path) == n:
    #             if path not in res:
    #                 res.append(path[:])
    #             return
    #
    #         for i in range(n):
    #             if used[i]:
    #                 continue
    #             used[i] = True
    #             path.append(nums[i])
    #             traceback(path)
    #             used[i] = False
    #             path.pop()
    #
    #     traceback([])
    #     return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        方法1：回溯。
        全排列类型：元素重复，不可复选。
        """
        nums.sort()
        res = []
        n = len(nums)
        used = [False for _ in range(n)]

        def traceback(path: List[int]):
            nonlocal n
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                # 新添加的剪枝逻辑，固定相同的元素在排列中的相对位置
                # 如果前面的相邻相等元素没有用过，则跳过
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])
                traceback(path)
                used[i] = False
                path.pop()

        traceback([])
        return res

# leetcode submit region end(Prohibit modification and deletion)
