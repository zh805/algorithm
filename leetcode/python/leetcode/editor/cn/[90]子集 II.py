# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
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
#  
#  
#  
#  👍 778 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        方法1：回溯
        """
        res = []
        path = []
        n = len(nums)
        # make the same value together
        nums.sort()

        def traceback(start):
            res.append(path[:])

            for i in range(start, n):
                # jump the same value, pruning
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                traceback(i + 1)
                path.pop()

        traceback(0)
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    nums = [1, 2, 2]
    result = Solution().subsetsWithDup(nums)
    print(result)
