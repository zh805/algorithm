# 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且全部数字和（3 * k 项）最大的子数组，并返回这三个子数组。 
# 
#  以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,1,2,6,7,5,1], k = 2
# 输出：[0,3,5]
# 解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
# 也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
# 输出：[0,2,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  1 <= nums[i] < 2¹⁶ 
#  1 <= k <= floor(nums.length / 3) 
#  
#  👍 309 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        方法1：前缀和+遍历。会超时。
        """
        # print(nums)
        res = []
        pre = nums
        n = len(nums)
        # 先求一个前缀和数组
        for i in range(n - k + 1):
            pre[i] = sum(nums[i:i + k])
        # print(pre)

        max_s = float('-inf')
        for i in range(n - k * 3 + 1):
            for j in range(i + k, n - k * 2 + 1):
                for l in range(j + k, n - k + 1):
                    s = pre[i] + pre[j] + pre[l]
                    # print(i, j, l)
                    # print(s)
                    if s > max_s:
                        max_s = s
                        res = [i, j, l]
        # print(max_s)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # nums = [1, 2, 1, 2, 6, 7, 5, 1]
    # k = 2
    nums = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    k = 2
    result = Solution().maxSumOfThreeSubarrays(nums, k)
    print(result)
