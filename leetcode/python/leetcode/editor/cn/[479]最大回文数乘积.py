# 给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入：n = 2
# 输出：987
# 解释：99 x 91 = 9009, 9009 % 1337 = 987
#  
# 
#  示例 2: 
# 
#  
# 输入： n = 1
# 输出： 9
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= n <= 8 
#  
#  👍 97 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def largestPalindrome(self, n: int) -> int:
    #     """
    #     方法1：暴力遍历,会超时。
    #     """
    #     def is_palindrome(num):
    #         # 判断一个数是否是回文数
    #         num = str(num)
    #         left, right = 0, len(num) - 1
    #         while left <= right:
    #             if num[left] != num[right]:
    #                 return False
    #             left += 1
    #             right -= 1
    #         return True
    #
    #     res = float('-inf')
    #     for i in range(10 ** n - 1, -1, -1):
    #         for j in range(10 ** n - 1, -1, -1):
    #             # print(i, j)
    #             num = i * j
    #             if num < res:
    #                 # 如果乘积比res还小，都不需要判断是否回文
    #                 continue
    #             if is_palindrome(num):
    #                 res = max(res, num)
    #                 break
    #     return res % 1337

    def largestPalindrome(self, n: int) -> int:
        """
        方法2：枚举回文数。
        n位数的乘积最大为2*n位，因此可以从大到小枚举回文数，然后看其是否为两数之积
        """
        if n == 1:
            return 9

        # 只要找到回文数左侧数字，就可以构造出整个回文数
        for left in range(10 ** n - 1, 0, -1):
            num, p = left, left
            while p:
                num = num * 10 + p % 10
                p //= 10
            # print(num)

            x = 10 ** n - 1
            # 乘法交换律，枚举到根号num即可。
            while x * x >= num:
                if num % x == 0:
                    return num % 1337
                x -= 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    n = 4
    result = Solution().largestPalindrome(n)
    print(result)
