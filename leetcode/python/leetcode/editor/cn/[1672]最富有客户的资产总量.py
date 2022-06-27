# 给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥
# 有的 资产总量 。 
# 
#  客户的 资产总量 就是他们在各家银行托管的资产数量之和。最富有客户就是 资产总量 最大的客户。 
# 
#  
# 
#  示例 1： 
# 
#  输入：accounts = [[1,2,3],[3,2,1]]
# 输出：6
# 解释：
# 第 1 位客户的资产总量 = 1 + 2 + 3 = 6
# 第 2 位客户的资产总量 = 3 + 2 + 1 = 6
# 两位客户都是最富有的，资产总量都是 6 ，所以返回 6 。
#  
# 
#  示例 2： 
# 
#  输入：accounts = [[1,5],[7,3],[3,5]]
# 输出：10
# 解释：
# 第 1 位客户的资产总量 = 6
# 第 2 位客户的资产总量 = 10 
# 第 3 位客户的资产总量 = 8
# 第 2 位客户是最富有的，资产总量是 10 
# 
#  示例 3： 
# 
#  输入：accounts = [[2,8,7],[7,1,3],[1,9,5]]
# 输出：17
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == accounts.length 
#  n == accounts[i].length 
#  1 <= m, n <= 50 
#  1 <= accounts[i][j] <= 100 
#  
#  👍 57 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def maximumWealth(self, accounts: List[List[int]]) -> int:
    #     """
    #     Method 1:
    #     """
    #     return max(sum(account) for account in accounts)

    # def maximumWealth(self, accounts: List[List[int]]) -> int:
    #     """
    #     Method 2
    #     """
    #     res = 0
    #     for account in accounts:
    #         res = max(sum(account), res)
    #     return res

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Method 3: map
        """
        return max(map(sum, accounts))

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    result = Solution().maximumWealth(accounts)
    print(result)
