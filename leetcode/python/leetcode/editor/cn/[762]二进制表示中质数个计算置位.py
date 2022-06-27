# 给你两个整数 left 和 right ，在闭区间 [left, right] 范围内，统计并返回 计算置位位数为质数 的整数个数。 
# 
#  计算置位位数 就是二进制表示中 1 的个数。 
# 
#  
#  例如， 21 的二进制表示 10101 有 3 个计算置位。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：left = 6, right = 10
# 输出：4
# 解释：
# 6 -> 110 (2 个计算置位，2 是质数)
# 7 -> 111 (3 个计算置位，3 是质数)
# 9 -> 1001 (2 个计算置位，2 是质数)
# 10-> 1010 (2 个计算置位，2 是质数)
# 共计 4 个计算置位为质数的数字。
#  
# 
#  示例 2： 
# 
#  
# 输入：left = 10, right = 15
# 输出：5
# 解释：
# 10 -> 1010 (2 个计算置位, 2 是质数)
# 11 -> 1011 (3 个计算置位, 3 是质数)
# 12 -> 1100 (2 个计算置位, 2 是质数)
# 13 -> 1101 (3 个计算置位, 3 是质数)
# 14 -> 1110 (3 个计算置位, 3 是质数)
# 15 -> 1111 (4 个计算置位, 4 不是质数)
# 共计 5 个计算置位为质数的数字。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= left <= right <= 10⁶ 
#  0 <= right - left <= 10⁴ 
#  
#  👍 93 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def countPrimeSetBits(self, left: int, right: int) -> int:
    #     """
    #     方法1：1）求出1的个数  2）判断是否为质数，最大值为10**6，只需计算22以内的质数即可。
    #     """
    #
    #     def count_one(num: int) -> int:
    #         n = 0
    #         while num:
    #             if num & 1:
    #                 n += 1
    #             num >>= 1
    #         return n
    #
    #     def is_prime(num: int) -> bool:
    #         # if num < 6:
    #         #     if num in [2, 3, 5]:
    #         #         return True
    #         #     else:
    #         #         return False
    #         #
    #         # yu = num % 6
    #         # if yu in [0, 2, 3, 4]:
    #         #     return False
    #         # else:
    #         #     for i in range(2, int(num ** 0.5) + 1):
    #         #         if num % i == 0:
    #         #             return False
    #         #     return True
    #
    #         if num in {2, 3, 5, 7, 11, 13, 17, 19, 23}:
    #             return True
    #         else:
    #             return False
    #
    #     res = 0
    #     for i in range(left, right + 1):
    #         n = count_one(i)
    #         if is_prime(n):
    #             res += 1
    #     return res

    # def countPrimeSetBits(self, left: int, right: int) -> int:
    #     """
    #     方法2：使用Counter计算1的个数
    #     """
    #     res = 0
    #     from collections import Counter
    #     for num in range(left, right + 1):
    #         counter = Counter(bin(num))
    #         if counter['1'] in {2, 3, 5, 7, 11, 13, 17, 19, 23}:
    #             res += 1
    #     return res

    # def countPrimeSetBits(self, left: int, right: int) -> int:
    #     """
    #     方法3：字符串可以直接计算1的个数。
    #     """
    #     res = 0
    #     for num in range(left, right + 1):
    #         if bin(num).count('1') in {2, 3, 5, 7, 11, 13, 17, 19, 23}:
    #             res += 1
    #     return res

    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        方法4：用bit位表示此位是否为质数，right < 10**6 < 2**20，小于20的质数为（2， 3， 5， 7， 11， 13， 17， 19）， 因此使用
        mask=665772=10100010100010101100 来存储这些质数。
        """
        res = 0
        for num in range(left, right + 1):
            if (1 << bin(num).count('1')) & 665772:
                res += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # left = 6
    # right = 10
    left = 10
    right = 15
    result = Solution().countPrimeSetBits(left, right)
    print(result)
