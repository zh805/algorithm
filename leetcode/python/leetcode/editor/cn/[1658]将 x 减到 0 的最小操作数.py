# coding=utf-8
# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改
#  数组以供接下来的操作使用。 
# 
#  如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,6,7,8,9], x = 4
# 输出：-1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,2,20,1,1,3], x = 10
# 输出：5
# 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁴ 
#  1 <= x <= 10⁹ 
#  
# 
#  👍 237 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        方法1：从nums中找到最长的连续子数组，其和为sum(nums)-x
        """
        if sum(nums) < x:
            return -1

        target = sum(nums) - x
        n = len(nums)
        left, right = 0, 0
        res = -1
        cur = 0
        while right < n:
            cur += nums[right]
            while cur > target:
                cur -= nums[left]
                left += 1

            if cur == target:
                res = max(res, right - left + 1)

            right += 1
        return -1 if res < 0 else n - res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1, 1, 4, 2, 3]
    x = 5
    result = Solution().minOperations(nums, x)
    print(result)
    assert result == 2

    nums = [5, 6, 7, 8, 9]
    x = 4
    result = Solution().minOperations(nums, x)
    print(result)
    assert result == -1

    nums = [3, 2, 20, 1, 1, 3]
    x = 10
    result = Solution().minOperations(nums, x)
    print(result)
    assert result == 5
