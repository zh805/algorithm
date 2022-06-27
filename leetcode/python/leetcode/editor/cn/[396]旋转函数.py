# 给定一个长度为 n 的整数数组 nums 。 
# 
#  假设 arrk 是数组 nums 顺时针旋转 k 个位置后的数组，我们定义 nums 的 旋转函数 F 为： 
# 
#  
#  F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1] 
#  
# 
#  返回 F(0), F(1), ..., F(n-1)中的最大值 。 
# 
#  生成的测试用例让答案符合 32 位 整数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [4,3,2,6]
# 输出: 26
# 解释:
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
# 所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [100]
# 输出: 0
#  
# 
#  
# 
#  提示: 
# 
#  
#  n == nums.length 
#  1 <= n <= 10⁵ 
#  -100 <= nums[i] <= 100 
#  
#  👍 140 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def maxRotateFunction(self, nums: List[int]) -> int:
    #     """
    #     方法1：遍历
    #     """
    #     n = len(nums)
    #     res = float('-inf')
    #
    #     for start in range(n):
    #         ans = 0
    #         j = 1
    #         for i in range(1, n):
    #             ans += j * nums[start + i - n]
    #             j += 1
    #         # print(ans)
    #         res = max(ans, res)
    #     return res

    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        方法2：数学计算
        """
        n = len(nums)
        s = sum(nums)

        ans = 0
        for i in range(n):
            ans += i * nums[i]
        # print(ans)
        res = ans

        for i in range(n - 1, 0, -1):
            ans = ans - n * nums[i] + s
            # print(ans)
            res = max(res, ans)
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # nums = [4, 3, 2, 6]
    # nums = [100]
    nums = [4, 15, 14, 3, 14, -8, 12, -9, 17, -1, 15, 1, 10, 19, -7, 15, 8, 7, -8, 11]
    result = Solution().maxRotateFunction(nums)
    print(result)
