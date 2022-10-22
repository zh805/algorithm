# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入:a = "11", b = "1"
# 输出："100" 
# 
#  示例 2： 
# 
#  
# 输入：a = "1010", b = "1011"
# 输出："10101" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= a.length, b.length <= 10⁴ 
#  a 和 b 仅由字符 '0' 或 '1' 组成 
#  字符串如果不是 "0" ，就不含前导零 
#  
# 
#  👍 901 👎 0

from itertools import zip_longest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def addBinary(self, a: str, b: str) -> str:
    #     """
    #     方法1：遍历
    #     """
    #     flag = 0
    #     m, n = len(a) - 1, len(b) - 1
    #     res = ''
    #     while m >= 0 or n >= 0 or flag != 0:
    #         s = flag
    #         if m >= 0:
    #             s += int(a[m])
    #         if n >= 0:
    #             s += int(b[n])
    #         if s == 1:
    #             flag = 0
    #         elif s == 2:
    #             s = 0
    #             flag = 1
    #         elif s == 3:
    #             s = 1
    #             flag = 1
    #         m -= 1
    #         n -= 1
    #         res = str(s) + res
    #     return res

    def addBinary(self, a: str, b: str) -> str:
        """
        方法2：先逆序再遍历
        """
        a = a[::-1]
        b = b[::-1]
        flag = 0
        res = ''
        for i, j in zip_longest(a, b, fillvalue=0):
            s = int(i) + int(j) + flag
            if s == 1:
                flag = 0
            elif s == 2:
                flag = 1
                s = 0
            elif s == 3:
                flag = 1
                s = 1
            res += str(s)
        if flag:
            res += str(flag)
        return res[::-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = "11"
    b = "1"
    # a = "1010"
    # b = "1011"
    result = Solution().addBinary(a, b)
    print(result)
