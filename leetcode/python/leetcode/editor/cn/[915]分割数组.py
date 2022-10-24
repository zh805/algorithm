# 给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得： 
# 
#  
#  left 中的每个元素都小于或等于 right 中的每个元素。 
#  left 和 right 都是非空的。 
#  left 的长度要尽可能小。 
#  
# 
#  在完成这样的分组后返回 left 的 长度 。 
# 
#  用例可以保证存在这样的划分方法。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,0,3,8,6]
# 输出：3
# 解释：left = [5,0,3]，right = [8,6]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,1,1,0,6,12]
# 输出：4
# 解释：left = [1,1,1,0]，right = [6,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 10⁶ 
#  可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。 
#  
# 
#  👍 137 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def partitionDisjoint(self, nums: List[int]) -> int:
    #     """
    #     方法1：三次遍历
    #     """
    #     n = len(nums)
    #     left_max = [nums[0]]
    #     right_min = [nums[-1] for _ in range(n)]
    #     for i in range(1, n):
    #         if nums[i] > left_max[-1]:
    #             left_max.append(nums[i])
    #         else:
    #             left_max.append(left_max[-1])
    #
    #     for i in range(n-2, -1, -1):
    #         if nums[i] < right_min[i+1]:
    #             right_min[i] = nums[i]
    #         else:
    #             right_min[i] = right_min[i+1]
    #
    #     # print(left_max)
    #     # print(right_min)
    #
    #     for i in range(n-1):
    #         if left_max[i] <= right_min[i+1]:
    #             res = i + 1
    #             return res

    def partitionDisjoint(self, nums: List[int]) -> int:
        """
        方法2：1次遍历
        """
        n = len(nums)
        cur_max, left_max = nums[0], nums[0]
        left_pos = 0
        for i in range(1, n-1):
            cur_max = max(nums[i], cur_max)
            if nums[i] < left_max:
                left_max, left_pos = cur_max, i
        return left_pos + 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # nums = [5, 0, 3, 8, 6]
    nums = [1, 1, 1, 0, 6, 12]
    # nums = [1, 1]
    result = Solution().partitionDisjoint(nums)
    print(result)
