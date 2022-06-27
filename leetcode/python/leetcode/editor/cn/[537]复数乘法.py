# 复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件： 
# 
#  
#  实部 是一个整数，取值范围是 [-100, 100] 
#  虚部 也是一个整数，取值范围是 [-100, 100] 
#  i² == -1 
#  
# 
#  给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：num1 = "1+1i", num2 = "1+1i"
# 输出："0+2i"
# 解释：(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
#  
# 
#  示例 2： 
# 
#  
# 输入：num1 = "1+-1i", num2 = "1+-1i"
# 输出："0+-2i"
# 解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 
#  
# 
#  
# 
#  提示： 
# 
#  
#  num1 和 num2 都是有效的复数表示。 
#  
#  👍 88 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def complexNumberMultiply(self, num1: str, num2: str) -> str:
    #     """
    #     方法1：字符串处理
    #     :param num1:
    #     :param num2:
    #     :return:
    #     """
    #     def extract(num):
    #         # 提取实部和虚部
    #         num = num.split('+')
    #         a = num[0]
    #         b = num[-1][:-1]
    #         return int(a), int(b)
    #
    #     a, b = extract(num1)
    #     c, d = extract(num2)
    #
    #     res = f'{a*c-b*d}+{a*d+b*c}i'
    #     return res

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        方法2：字符串处理，代码简洁
        :param num1:
        :param num2:
        :return:
        """
        real1, imag1 = map(int, num1[:-1].split('+'))
        real2, imag2 = map(int, num2[:-1].split('+'))
        return f'{real1*real2 - imag1*imag2}+{real1*imag2+imag1*real2}i'


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # num1 = "1+1i"
    # num2 = "1+1i"
    num1 = "1+-1i"
    num2 = "1+-1i"
    result = Solution().complexNumberMultiply(num1, num2)
    print(result)

