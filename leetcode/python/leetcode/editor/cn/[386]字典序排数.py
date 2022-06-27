# 给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。 
# 
#  你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 13
# 输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 2
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 5 * 10⁴ 
#  
#  👍 324 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def lexicalOrder(self, n: int) -> List[int]:
    #     """
    #     方法1：DFS. 数字排列顺序可抽象为多叉树，深度优先遍历即可。
    #     没有0，所以从第二层开始遍历。
    #     """
    #     res = []
    #
    #     def dfs(cur):
    #         if cur > n:
    #             return
    #         res.append(cur)
    #         for i in range(10):
    #             num = cur * 10 + i
    #             dfs(num)
    #
    #     for i in range(1, 10):
    #         dfs(i)
    #     return res

    def lexicalOrder(self, n: int) -> List[int]:
        """
        方法2：迭代
        """
        res = []

        num = 1
        for i in range(n):
            res.append(num)
            if num * 10 <= n:
                # 优先在num后附加0
                num *= 10
            else:
                # 末位的数搜索完毕，回退到上一位
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 100
    result = Solution().lexicalOrder(n)
    print(result)
