# 给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。 
# 
#  全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目： 
# 
#  
#  0 <= i < j < n 
#  nums[i] > nums[j] 
#  
# 
#  局部倒置 的数目等于满足下述条件的下标 i 的数目： 
# 
#  
#  0 <= i < n - 1 
#  nums[i] > nums[i + 1] 
#  
# 
#  当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,2]
# 输出：true
# 解释：有 1 个全局倒置，和 1 个局部倒置。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,0]
# 输出：false
# 解释：有 2 个全局倒置，和 1 个局部倒置。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 10⁵ 
#  0 <= nums[i] < n 
#  nums 中的所有整数 互不相同 
#  nums 是范围 [0, n - 1] 内所有数字组成的一个排列 
#  
# 
#  👍 176 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def isIdealPermutation(self, nums: List[int]) -> bool:
    #     """
    #     方法1：遍历
    #     """
    #     n = len(nums)
    #     local_num = 0
    #     for i in range(n - 1):
    #         if nums[i] > nums[i + 1]:
    #             local_num += 1
    #     # print(local_num)
    #
    #     global_num = 0
    #     for j in range(1, n):
    #         for i in range(0, j):
    #             if nums[i] > nums[j]:
    #                 global_num += 1
    #     # print(global_num)
    #     return True if local_num == global_num else False

    def isIdealPermutation(self, nums: List[int]) -> bool:
        """
        方法2：局部倒置一定是一个全局倒置，因此只需判断有无全局倒置。
        从后向前遍历，维护后缀最小值。
        """
        n = len(nums)
        res = True
        if n < 3:
            return res
        min_suffix = nums[-1]
        for i in range(n-3, -1, -1):
            if nums[i] > min_suffix:
                res = False
                break
            else:
                min_suffix = min(min_suffix, nums[i+1])
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # nums = [1, 0, 2]
    nums = [1, 2, 0]
    # nums = [1, 0]
    result = Solution().isIdealPermutation(nums)
    print(result)
