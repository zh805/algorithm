# 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。 
# 
#  请你找出并返回只出现一次的那个数。 
# 
#  你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,2,3,3,4,4,8,8]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  
# 输入: nums =  [3,3,7,7,10,11,11]
# 输出: 10
#  
# 
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 10⁵ 
#  
#  👍 502 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        方法1：异或
        """
        num = nums[0]
        for i in range(1, len(nums)):
            num ^= nums[i]
        return num


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    nums = [3, 3, 7, 7, 10, 11, 11]
    result = Solution().singleNonDuplicate(nums)
    print(result)
