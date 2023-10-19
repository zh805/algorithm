# 给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组 (a, b, c, d) 的数量。其中 a、b、c 和 
# d 都是 nums 中的元素，且 a != b != c != d 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,4,6]
# 输出：8
# 解释：存在 8 个满足题意的元组：
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,4,5,10]
# 输出：16
# 解释：存在 16 个满足题意的元组：
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  1 <= nums[i] <= 10⁴ 
#  nums 中的所有元素 互不相同 
#  
# 
#  👍 77 👎 0

from typing import List
from collections import defaultdict

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        m = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                m[nums[i] * nums[j]] += 1

        for _, v in m.items():
            res += v * (v-1) // 2 * 8
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [2, 3, 4, 6]
    result = Solution().tupleSameProduct(nums)
    print(result)

    nums = [1, 2, 4, 5, 10]
    result = Solution().tupleSameProduct(nums)
    print(result)
