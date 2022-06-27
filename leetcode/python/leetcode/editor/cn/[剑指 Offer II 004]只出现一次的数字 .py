# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,2,3,2]
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,0,1,0,1,100]
# 输出：100
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 
#  
# 
#  
# 
#  进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？ 
# 
#  
# 
#  注意：本题与主站 137 题相同：https://leetcode-cn.com/problems/single-number-ii/ 
#  Related Topics 位运算 数组 👍 44 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

import collections
from typing import List


class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     """
    #     方法1：构建字典，key为num, value为次数；遍历取出次数为1的。
    #     :param nums:
    #     :return:
    #     """
    #     num_dict = {}
    #     for num in nums:
    #         if num not in num_dict:
    #             num_dict[num] = 1
    #         else:
    #             times = num_dict[num]
    #             num_dict[num] += times + 1
    #     for k, v in num_dict.items():
    #         if v != 1:
    #             continue
    #         else:
    #             return k

    # def singleNumber(self, nums: List[int]) -> int:
    #     """
    #     方法2：使用collections
    #     :param nums:
    #     :return:
    #     """
    #     counts = collections.Counter(nums)
    #     res = [k for k, v in counts.items() if v == 1][0]
    #     return res

    def singleNumber(self, nums: List[int]) -> int:
        """
        方法3：二进制位相加，对3取余。
        :param nums:
        :return:
        """
        ans = 0
        for i in range(32):
            # total = 0
            # for num in nums:
            #     total += num & (1 << i)
            total = sum(num & (1 << i) for num in nums)
            # 出现三次的数字，第i位的和与3取余为0。若共4次，则去余为1。
            if not total % 3:
                continue
            # python int包括正数和负数，最高位31位表示符号。
            if i == 31:
                ans -= (1 << i)
            else:
                # 第i位结果与之前已计算过的（i-1）位求和。
                ans |= (1 << i)
        return ans
    
# leetcode submit region end(Prohibit modification and deletion)
