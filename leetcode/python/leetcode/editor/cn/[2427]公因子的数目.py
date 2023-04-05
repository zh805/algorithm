# 给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。 
# 
#  如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：a = 12, b = 6
# 输出：4
# 解释：12 和 6 的公因子是 1、2、3、6 。
#  
# 
#  示例 2： 
# 
#  输入：a = 25, b = 30
# 输出：2
# 解释：25 和 30 的公因子是 1、5 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= a, b <= 1000 
#  
# 
#  👍 14 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        """
        方法1：模拟
        """
        # res = 0
        # s = {}
        # m = min(a, b)
        # for i in range(1, m+1):
        #     if a % i == 0 and b % i==0:
        #         res += 1
        # return res

        return sum(a % i == 0 and b % i == 0 for i in range(1, min(a, b) + 1))


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    a = 12
    b = 6
    result = Solution().commonFactors(a, b)
    print(result)
