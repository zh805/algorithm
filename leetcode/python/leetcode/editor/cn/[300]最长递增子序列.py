# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。 
# 
#  子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子
# 序列。 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2500 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你能将算法的时间复杂度降低到 O(n log(n)) 吗? 
#  
#  👍 2262 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     """
    #     方法1：动态规划
    #     最优子结构 + 重叠子问题
    #     已知dp[0,1,,,i-1],求dp[i]
    #     :param nums:
    #     :return:
    #     """
    #     # dp[i] 表示以nums[i]结尾的最长递增子序列的长度
    #     # base case dp数组全初始化为1，因为至少有1个递增子序列。
    #     dp = [1 for _ in range(len(nums))]
    #     for i in range(1, len(nums)):
    #         # 遍历小于索引i的元素j，看从j到i是不是递增。
    #         for j in range(0, i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        方法2：扩展，找出最长递增子序列。
        """
        n = len(nums)
        # dp[i] 表示到数组从头到索引i时的LIS长度
        dp = [1 for _ in range(n)]
        # path 存储当前位置符合递增的上一个元素的索引。
        path = [-1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    path[i] = j

        idx = dp.index(max(dp))
        res = []
        while idx != -1:
            res.append(nums[idx])
            idx = path[idx]
        res.reverse()
        print(res)
        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [0, 1, 0, 3, 2, 3]
    result = Solution().lengthOfLIS(nums)
    print(result)
