# 给定一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28. 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [2,4]
# 输出：6
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [8,10,2]
# 输出：10
#  
# 
#  示例 5： 
# 
#  
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  0 <= nums[i] <= 2³¹ - 1 
#  
#  
#  
# 
#  
# 
#  进阶：你可以在 O(n) 的时间解决这个问题吗？ 
# 
#  
# 
#  注意：本题与主站 421 题相同： https://leetcode-cn.com/problems/maximum-xor-of-two-
# numbers-in-an-array/ 
#  👍 25 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def findMaximumXOR(self, nums: List[int]) -> int:
    #     """
    #     方法1：暴力遍历，O（N**2），会超时。
    #     """
    #     res = 0
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(i+1, n):
    #             res = max(res, nums[i] ^ nums[j])
    #     return res

    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        方法2：异或，相同为0，不同为1。
        """
        n = len(nums)




# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # nums = [3, 10, 5, 25, 2, 8]
    # nums = [0]
    # nums = [2, 4]
    nums = [8, 10, 2]
    result = Solution().findMaximumXOR(nums)
    print(result)
