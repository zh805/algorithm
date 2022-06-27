# 给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 5
# 输出：true
# 解释：5 的二进制表示是：101
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 7
# 输出：false
# 解释：7 的二进制表示是：111. 
# 
#  示例 3： 
# 
#  
# 输入：n = 11
# 输出：false
# 解释：11 的二进制表示是：1011. 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
#  👍 138 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def hasAlternatingBits(self, n: int) -> bool:
    #     # 方法1：转换为二进制
    #     pre = None
    #     while n:
    #         bit = n % 2
    #         if pre is None:
    #             pre = bit
    #         else:
    #             if pre == bit:
    #                 return False
    #             else:
    #                 pre = bit
    #         n //= 2
    #     return True

    def hasAlternatingBits(self, n: int) -> bool:
        # 方法2：优化1
        pre = 2
        while n:
            bit = n % 2
            if bit == pre:
                return False
            pre = bit
            n //= 2
        return True


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # n = 5
    # n = 7
    # n = 11
    n = 4
    result = Solution().hasAlternatingBits(n)
    print(result)

