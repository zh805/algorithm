# 给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。 
# 
#  
# 
#  注意： 
# 
#  
#  整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2 
#  假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2³¹, 2³¹−1]。本题中，如果除法结果溢出，则返回 231 − 1 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：a = 15, b = 2
# 输出：7
# 解释：15/2 = truncate(7.5) = 7
#  
# 
#  示例 2： 
# 
#  
# 输入：a = 7, b = -3
# 输出：-2
# 解释：7/-3 = truncate(-2.33333..) = -2 
# 
#  示例 3： 
# 
#  
# 输入：a = 0, b = 1
# 输出：0 
# 
#  示例 4： 
# 
#  
# 输入：a = 1, b = 1
# 输出：1 
# 
#  
# 
#  提示: 
# 
#  
#  -2³¹ <= a, b <= 2³¹ - 1 
#  b != 0 
#  
# 
#  
# 
#  注意：本题与主站 29 题相同：https://leetcode-cn.com/problems/divide-two-integers/ 
# 
#  
#  Related Topics 位运算 数学 👍 78 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def divide(self, a: int, b: int) -> int:
    #     """
    #     方法1：循环法,超时无法通过
    #     :param a:
    #     :param b:
    #     :return:
    #     """
    #     flag = True if (a > 0 and b > 0) or (a < 0 and b < 0) else False
    #     a, b = abs(a), abs(b)
    #     if a < b:
    #         return 0
    #     if a == b:
    #         return 1 if flag else -1
    #     res = 0
    #     sum = 0
    #     while sum < a:
    #         sum += b
    #         if sum >= a:
    #             break
    #         res += 1
    #     return res if flag else 0-res

    def divide(self, a: int, b: int) -> int:
        """
        方法2：除数每次扩大两倍，减少循环次数
        :param a:
        :param b:
        :return:
        """
        flag = True if (a > 0 and b > 0) or (a < 0 and b < 0) else False
        a, b = abs(a), abs(b)

        def calc(x, y):
            cnt = 1
            while x > y << 1:
                y <<= 1
                cnt <<= 1
            return cnt, y

        res = 0
        while a >= b:
            cnt, y = calc(a, b)
            a -= y
            res += cnt

        res = res if flag else -res
        return res-1 if res >= 2 ** 31 else res

# leetcode submit region end(Prohibit modification and deletion)
