# 给定一个整数 n ，返回 n! 结果中尾随零的数量。 
# 
#  提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：0
# 解释：3! = 6 ，不含尾随 0
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 5
# 输出：1
# 解释：5! = 120 ，有一个尾随 0
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 10⁴ 
#  
# 
#  
# 
#  进阶：你可以设计并实现对数时间复杂度的算法来解决此问题吗？ 
#  👍 584 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    # def trailingZeroes(self, n: int) -> int:
    #     """
    #     方法1：求出阶乘后，计算0的个数。复杂度高，超时。
    #     """
    #     num = 1
    #     for i in range(1, n+1):
    #         num *= i
    #
    #     res = 0
    #     while num:
    #         a = num % 10
    #         if a == 0:
    #             res += 1
    #         else:
    #             break
    #         num //= 10
    #
    #     return res

    # def trailingZeroes(self, n: int) -> int:
    #     """
    #     方法2：计算结果，转成字符串后，遍历找0。
    #     """
    #     num = str(math.factorial(n))
    #     n = len(num)
    #     res = 0
    #     for i in range(n-1, -1, -1):
    #         if num[i] != '0':
    #             res = n - i - 1
    #             break
    #     return res

    # def trailingZeroes(self, n: int) -> int:
    #     """
    #     方法3：数学法，找5的倍数的个数。
    #     """
    #     res = 0
    #     for i in range(5, n+1, 5):
    #         while i % 5 == 0:
    #             i //= 5
    #             res += 1
    #     return res

    def trailingZeroes(self, n: int) -> int:
        """
        方法4：数学法
        """
        res = 0
        while n:
            n //= 5
            res += n
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 30
    result = Solution().trailingZeroes(n)
    print(result)

