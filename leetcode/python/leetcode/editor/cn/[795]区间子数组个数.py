# 给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组
# ，并返回满足条件的子数组的个数。 
# 
#  生成的测试用例保证结果符合 32-bit 整数范围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,1,4,3], left = 2, right = 3
# 输出：3
# 解释：满足条件的三个子数组：[2], [2, 1], [3]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,9,2,5,6], left = 2, right = 8
# 输出：7
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 10⁹ 
#  0 <= left <= right <= 10⁹ 
#  
# 
#  👍 307 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans, i0, i1 = 0, -1, -1
        for i, x in enumerate(nums):
            if x > right:
                i0 = i
            if x >= left:
                i1 = i
            ans += i1 - i0
        return ans

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [2, 1, 4, 3]
    left = 2
    right = 3
    result = Solution().numSubarrayBoundedMax(nums, left, right)
    print(result)
