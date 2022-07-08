# 有 n 个筹码。第 i 个筹码的位置是 position[i] 。 
# 
#  我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个筹码的位置从 position[i] 改变为: 
# 
#  
# 
#  
#  position[i] + 2 或 position[i] - 2 ，此时 cost = 0 
#  position[i] + 1 或 position[i] - 1 ，此时 cost = 1 
#  
# 
#  返回将所有筹码移动到同一位置上所需要的 最小代价 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：position = [1,2,3]
# 输出：1
# 解释：第一步:将位置3的筹码移动到位置1，成本为0。
# 第二步:将位置2的筹码移动到位置1，成本= 1。
# 总成本是1。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：position = [2,2,2,3,3]
# 输出：2
# 解释：我们可以把位置3的两个筹码移到位置2。每一步的成本为1。总成本= 2。
#  
# 
#  示例 3: 
# 
#  
# 输入：position = [1,1000000000]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= chips.length <= 100 
#  1 <= chips[i] <= 10^9 
#  
#  👍 143 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def minCostToMoveChips(self, position: List[int]) -> int:
    #     """
    #     方法1：遍历
    #     :param position:
    #     :return:
    #     """
    #     res = float('inf')
    #     p_s = set(position)
    #     for p in p_s:
    #         tmp = 0
    #         is_odd = p & 1
    #         for pos in position:
    #             if pos & 1 != is_odd:
    #                 tmp += 1
    #         res = min(res, tmp)
    #
    #     return res

    def minCostToMoveChips(self, position: List[int]) -> int:
        """
        方法2：贪心。
        两种情况会有开销：1. 奇数位置筹码最后都移动到了偶数位置  2. 偶数位置筹码最后都移动到了奇数位置
        :param position:
        :return:
        """
        odd, even = 0, 0
        for pos in position:
            if pos & 1 == 1:
                odd += 1
            else:
                even += 1
        return min(odd, even)

        # from collections import Counter
        # c = Counter(p & 1 for p in position)
        # return min(c[1], c[0])

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # position = [1, 2, 3]
    # position = [2, 2, 2, 3, 3]
    position = [1, 1000000000]
    result = Solution().minCostToMoveChips(position)
    print(result)
