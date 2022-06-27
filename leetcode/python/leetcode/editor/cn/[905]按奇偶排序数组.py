# 给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。 
# 
#  返回满足此条件的 任一数组 作为答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,1,2,4]
# 输出：[2,4,3,1]
# 解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  0 <= nums[i] <= 5000 
#  
#  👍 277 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        方法1：双指针
        """
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] & 1 == 0:
                left += 1
            while left < right and nums[right] & 1 == 1:
                right -= 1

            nums[left], nums[right] = nums[right], nums[left]

        return nums
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # nums = [3, 1, 2, 4]
    nums = [0]
    result = Solution().sortArrayByParity(nums)
    print(result)
