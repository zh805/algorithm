# 给定一个整数数组和一个整数 k ，请找到该数组中和为 k 的连续子数组的个数。 
# 
#  
# 
#  示例 1 : 
# 
#  
# 输入:nums = [1,1,1], k = 2
# 输出: 2
# 解释: 此题 [1,1] 与 [1,1] 为两种不同的情况
#  
# 
#  示例 2 : 
# 
#  
# 输入:nums = [1,2,3], k = 3
# 输出: 2
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -1000 <= nums[i] <= 1000 
#  
#  -10⁷ <= k <= 10⁷ 
#  
#  
# 
#  
# 
#  注意：本题与主站 560 题相同： https://leetcode-cn.com/problems/subarray-sum-equals-k/ 
#  Related Topics 数组 哈希表 前缀和 👍 38 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     """
    #     方法1：遍历(能解，但会超时)
    #     :param nums:
    #     :param k:
    #     :return:
    #     """
    #     ret = 0
    #     r_total = 0
    #     length = len(nums)
    #     for right in range(length):
    #         r_total += nums[right]
    #         l_total = r_total
    #         for left in range(right + 1):
    #             if l_total == k:
    #                 ret += 1
    #             l_total -= nums[left]
    #     return ret

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        方法2：前缀和
        :param nums:
        :param k:
        :return:
        """
        result = 0
        total = 0
        # 前缀和字典，key为sum(nums[0:i]), value为前缀和出现的次数；
        pre_sum_dict = {0: 1}
        for idx, num in enumerate(nums):
            total += num
            result += pre_sum_dict.get(total - k, 0)
            pre_sum_dict[total] = pre_sum_dict.get(total, 0) + 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
