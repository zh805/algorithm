# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。 
# 
#  由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。 
# 
#  注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 4
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= x <= 2³¹ - 1 
#  
#  👍 967 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        方法1：二分法
        """
        if x == 0:
            return 0
        if x == 1:
            return 1

        left, right, res = 0, x, -1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    x = 1
    result = Solution().mySqrt(x)
    print(result)
