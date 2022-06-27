# 一个专业的小偷，计划偷窃一个环形街道上沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同
# 时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组 nums ，请计算 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 1000 
#  
# 
#  
# 
#  注意：本题与主站 213 题相同： https://leetcode-cn.com/problems/house-robber-ii/ 
#  Related Topics 数组 动态规划 👍 9 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        方法1：动态规划
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        可以拆解为：分别偷[0, n-1]和[1, n], 取两者最大值。
        :param nums:
        :return:
        """
        if len(nums) <= 3:
            return max(nums)

        nums1 = nums[:-1]
        nums2 = nums[1:]

        def dynamic(nums):
            a, b, res = 0, 0, 0
            for num in nums:
                res = max(b, a + num)
                a, b = b, res
            return res

        return max(dynamic(nums1), dynamic(nums2))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # nums = [1]
    # nums = [1, 2]
    nums = [1, 2, 1, 1]
    # nums = [2, 3, 2]
    # nums = [1, 2, 3, 1]
    result = Solution().rob(nums)
    print(result)
