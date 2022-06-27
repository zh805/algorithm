# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3], k = 0
# 输出：0 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  1 <= nums[i] <= 1000 
#  0 <= k <= 10⁶ 
#  
#  👍 442 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    #     """
    #     方法1：暴力遍历，超时
    #     """
    #     n = len(nums)
    #     res = 0
    #     for i in range(n):
    #         start = i
    #         product = 1
    #         while start < n and product * nums[start] < k:
    #             res += 1
    #             product *= nums[start]
    #             start += 1
    #     return res

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        方法2：滑动窗口
        """
        n = len(nums)
        left, right = 0, 0
        product = 1
        res = 0
        while right < n:
            product *= nums[right]
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            res += right - left + 1
            right += 1

        # print(left, right)
        # print(res)
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    nums = [10, 5, 2, 6]
    k = 100
    # nums = [1, 2, 3]
    # k = 0
    result = Solution().numSubarrayProductLessThanK(nums, k)
    print(result)
