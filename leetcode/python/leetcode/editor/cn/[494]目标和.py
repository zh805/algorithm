# 给你一个整数数组 nums 和一个整数 target 。 
# 
#  向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ： 
# 
#  
#  例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。 
#  
# 
#  返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], target = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 20 
#  0 <= nums[i] <= 1000 
#  0 <= sum(nums[i]) <= 1000 
#  -1000 <= target <= 1000 
#  
#  👍 1085 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     """
    #     方法1：回溯是暴力遍历，找出所有的可能情况，会超时。
    #     :param nums:
    #     :param target:
    #     :return:
    #     """
    #     res = 0
    #
    #     def track_back(nums, i, total):
    #         if i == len(nums):
    #             if total == target:
    #                 nonlocal res
    #                 res += 1
    #             return
    #
    #         total += nums[i]
    #         track_back(nums, i+1, total)
    #         total -= nums[i]
    #
    #         total -= nums[i]
    #         track_back(nums, i+1, total)
    #         total += nums[i]
    #
    #     track_back(nums, 0, 0)
    #     return res

    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     """
    #     方法2：回溯；超时。
    #     :param nums:
    #     :param target:
    #     :return:
    #     """
    #     res = 0
    #
    #     def track_back(i, path):
    #         if i == len(nums):
    #             if sum(path) == target:
    #                 nonlocal res
    #                 res += 1
    #             return
    #
    #         path.append(nums[i])
    #         track_back(i+1, path)
    #         path.pop()
    #
    #         path.append(-nums[i])
    #         track_back(i+1, path)
    #         path.pop()
    #
    #     track_back(0, [])
    #     return res

    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     """
    #     方法3：二叉树遍历
    #     :param nums:
    #     :param target:
    #     :return:
    #     """
    #     res = 0
    #
    #     def traverse(nums, i, total):
    #         if i == len(nums):
    #             if total == target:
    #                 nonlocal res
    #                 res += 1
    #             return
    #
    #         traverse(nums, i + 1, total + nums[i])
    #         traverse(nums, i + 1, total - nums[i])
    #
    #     traverse(nums, 0, 0)
    #     return res

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        方法4：动态规划
        :param nums:
        :param target:
        :return:
        """
        pass


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # nums = [1, 1, 1, 1, 1]
    # target = 3
    # nums = [1]
    # target = 1
    # nums = [1, 2, 3]
    # target = 4
    # nums = [7, 46, 36, 49, 5, 34, 25, 39, 41, 38, 49, 47, 17, 11, 1, 41, 7, 16, 23, 13]
    # target = 3
    result = Solution().findTargetSumWays(nums, target)
    print(result)
