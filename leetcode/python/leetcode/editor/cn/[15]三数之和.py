# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 双指针 排序 👍 4320 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        方法1：排序，遍历数组，双指针
        :param nums:
        :return:
        """
        res = []
        nums_length = len(nums)
        if len(nums) <= 2:
            return res

        nums.sort()
        for i in range(nums_length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                return res
            left, right = i + 1, nums_length - 1
            while left < right:
                # 难点在于去重
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 1, -1]
    # nums = [1, -1, -1, 0]
    # nums = [-2, 0, 0, 2, 2]
    result = Solution().threeSum(nums)
    print(result)
