# 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 0
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 1
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 5 * 10⁶ 
#  
#  👍 836 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        方法1：埃氏筛，一个数字的倍数肯定不是素数。
        :param n:
        :return:
        """
        flag = [False for _ in range(n)]

        res = 0
        for num in range(2, n):
            if not flag[num]:
                # 第一次出现，肯定为素数
                res += 1
                for i in range(num * num, n, num):
                    flag[i] = True
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = 10
    # n = 0
    # n = 1
    n = 1000
    result = Solution().countPrimes(n)
    print(result)
