# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。 
# 
#  当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。 
# 
#  请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。 
# 
#  注意：不允许旋转信封。 
#  
# 
#  示例 1： 
# 
#  
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。 
# 
#  示例 2： 
# 
#  
# 输入：envelopes = [[1,1],[1,1],[1,1]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= envelopes.length <= 10⁵ 
#  envelopes[i].length == 2 
#  1 <= wi, hi <= 10⁵ 
#  
#  👍 666 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    #     """
    #     方法1：动态规划, 会超时，需优化。
    #     :param envelopes:
    #     :return:
    #     """
    #     # dp[i]表示第i个信封的最大个数
    #     envelopes.sort(key=lambda item: item[0])
    #     # print(envelopes)
    #     dp = [1 for _ in range(len(envelopes))]
    #     for i in range(1, len(envelopes)):
    #         for j in range(i):
    #             if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     # print(dp)
    #     return max(dp)

    # def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    #     """
    #     方法2：动态规划。排序，w正序，h逆序，找出h的最大递增子序列。超时。
    #     :param envelopes:
    #     :return:
    #     """
    #     n = len(envelopes)
    #     envelopes.sort(key=lambda item: (item[0], -item[1]))
    #     # print(envelopes)
    #     dp = [1 for _ in range(n)]
    #     for i in range(n):
    #         for j in range(i):
    #             if envelopes[i][1] > envelopes[j][1]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     # print(dp)
    #     return max(dp)
    
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        方法3：动态规划。二分查找方式找LIS
        :param envelopes: 
        :return: 
        """
        envelopes.sort(key=lambda item: (item[0], -item[1]))
        nums = [envelope[1] for envelope in envelopes]

        def lis(nums):
            # 二分法求nums的最长递增子序列（扑克牌分堆）
            top = [0 for _ in range(len(nums))]
            # 牌堆初始化为0
            piles = 0

            for i in range(len(nums)):
                # 要处理的扑克牌
                poker = nums[i]

                # 搜索左侧边界的二分查找
                left, right = 0, piles
                while left < right:
                    mid = (left + right) // 2
                    if top[mid] > poker:
                        right = mid
                    elif top[mid] < poker:
                        left = mid + 1
                    else:
                        right = mid

                # 没找到合适的牌堆, 新建一堆
                if left == piles:
                    piles += 1
                top[left] = poker
            return piles

        return lis(nums)

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    envelopes = [[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]]
    # envelopes = [[7, 8], [12, 16], [12, 5], [1, 8], [4, 19], [3, 15], [4, 10], [9, 16]]
    result = Solution().maxEnvelopes(envelopes)
    print(result)
