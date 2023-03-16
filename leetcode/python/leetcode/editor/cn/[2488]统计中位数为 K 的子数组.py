# 给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。 
# 
#  统计并返回 nums 中的 中位数 等于 k 的非空子数组的数目。 
# 
#  注意： 
# 
#  
#  数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。 
#  
# 
#  
#  例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。 
#  
#  
#  子数组是数组中的一个连续部分。 
# 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,2,1,4,5], k = 4
# 输出：3
# 解释：中位数等于 4 的子数组有：[4]、[4,5] 和 [1,4,5] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,3,1], k = 3
# 输出：1
# 解释：[3] 是唯一一个中位数等于 3 的子数组。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 10⁵ 
#  1 <= nums[i], k <= n 
#  nums 中的整数互不相同 
#  
# 
#  👍 52 👎 0

from collections import Counter
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        方法1：前缀和+哈希表
        小于k的为-1，大于k的为1
        """
        res = 0
        c = Counter()
        k_index = nums.index(k)
        c[0] = 1
        s = 0

        def sign(n):
            return (n > 0) - (n < 0)

        for i, num in enumerate(nums):
            s += sign(num - k)
            if i < k_index:
                c[s] += 1
            else:
                pre_0 = c[s]
                pre_1 = c[s - 1]
                res += pre_0 + pre_1
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [3, 2, 1, 4, 5]
    k = 4
    result = Solution().countSubarrays(nums, k)
    print(result)

    nums = [2, 3, 1]
    k = 3
    result = Solution().countSubarrays(nums, k)
    print(result)
