# 给你一个整数数组 nums ，返回出现最频繁的偶数元素。 
# 
#  如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [0,1,2,2,4,4,1]
# 输出：2
# 解释：
# 数组中的偶数元素为 0、2 和 4 ，在这些元素中，2 和 4 出现次数最多。
# 返回最小的那个，即返回 2 。 
# 
#  示例 2： 
# 
#  输入：nums = [4,4,4,9,2,4]
# 输出：4
# 解释：4 是出现最频繁的偶数元素。
#  
# 
#  示例 3： 
# 
#  输入：nums = [29,47,21,41,13,37,25,7]
# 输出：-1
# 解释：不存在偶数元素。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2000 
#  0 <= nums[i] <= 10⁵ 
#  
# 
#  👍 26 👎 0

from collections import Counter
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        """
        方法1：哈希计数
        """
        res = -1
        t = 0
        c = Counter(nums)
        for k, v in c.items():
            if not k & 1:
                if v > t:
                    res = k
                    t = v
                elif v == t:
                    res = min(k, res)
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 4, 4, 1]
    result = Solution().mostFrequentEven(nums)
    print(result)

    # nums = [4, 4, 4, 9, 2, 4]
    nums = [29, 47, 21, 41, 13, 37, 25, 7]
    result = Solution().mostFrequentEven(nums)
    print(result)
