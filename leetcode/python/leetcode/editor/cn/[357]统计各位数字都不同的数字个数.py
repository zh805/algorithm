# 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10ⁿ 。
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：91
# 解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。 
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 0
# 输出：1
#  
#  
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 8 
#  
#  👍 210 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def countNumbersWithUniqueDigits(self, n: int) -> int:
    #     """
    #     方法1：
    #     数学计算，排列组合。
    #     当n=0，1
    #     当n=1，[0,9], 1位数，10个。 每个位置
    #     当n=2，两位数时，9 * 9 = 81。最高位有9种选择（0不可以），次高位也有9种选择。 81 + 10 = 91
    #     当n=3，三位数。9 * 9 * 8
    #     """
    #     if n == 0:
    #         return 1
    #     if n == 1:
    #         return 10
    #
    #     res = 10
    #     for i in range(2, n + 1):
    #         temp = 9
    #         for j in range(9, 10 - i, -1):
    #             temp *= j
    #         res += temp
    #
    #     return res

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        方法1.2：优化方法1。计算n-1位数的结果，可用于计算n位数。
        """
        if n == 0:
            return 1
        if n == 1:
            return 10

        res = 10
        cur = 9
        for i in range(n-1):
            cur *= 9 - i
            res += cur

        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    n = 3
    result = Solution().countNumbersWithUniqueDigits(n)
    print(result)
