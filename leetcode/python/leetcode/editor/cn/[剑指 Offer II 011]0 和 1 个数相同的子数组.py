# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。 
# 
#  示例 2: 
# 
#  
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] 不是 0 就是 1 
#  
# 
#  
# 
#  注意：本题与主站 525 题相同： https://leetcode-cn.com/problems/contiguous-array/ 
#  👍 35 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # def findMaxLength(self, nums: List[int]) -> int:
    #     """
    #     方法1：前缀和的方法。
    #     :param nums:
    #     :return:
    #     """
    #     result = 0
    #     # key为O的个数与1的个数的差值，value为当前的idx
    #     diff_dict = dict()
    #     zero_total, one_total = 0, 0
    #     for idx, num in enumerate(nums):
    #         if num == 0:
    #             zero_total += 1
    #         else:
    #             one_total += 1
    #         diff = zero_total - one_total
    #         # 把差值存入dict，同样的key只存下标最小的。
    #         if diff not in diff_dict:
    #             diff_dict[diff] = idx
    #         if diff == 0:
    #             # 0和1数量一样多
    #             result = max(result, idx + 1)
    #         else:
    #             # 0和1不一样多，则去key为差值的前缀数组。
    #             # 比如点前idx,0比1多3个，则把key为3的前缀数组去掉，剩下的数组0和1就一样多了。
    #             start_idx = diff_dict.get(diff, 0)
    #             result = max(result, idx - start_idx)
    #     return result

    def findMaxLength(self, nums: List[int]) -> int:
        """
        方法2：可把0看成-1，则此题可转化为和为0的最长子数组长度。用前缀和可解。
        :param nums:
        :return:
        """
        result = 0
        # key为前缀和，value为索引。
        pre_sum_dict = {0: -1}
        total = 0
        for idx, num in enumerate(nums):
            total += 1 if num == 1 else -1
            if total in pre_sum_dict:
                result = max(result, idx - pre_sum_dict[total])
            else:
                pre_sum_dict[total] = idx
        return result

# leetcode submit region end(Prohibit modification and deletion)
