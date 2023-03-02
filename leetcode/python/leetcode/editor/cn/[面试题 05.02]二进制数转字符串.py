# 二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字无法精确地用32位以内的二进制表示，则打印
# “ERROR”。 
# 
#  示例1: 
# 
#  
#  输入：0.625
#  输出："0.101"
#  
# 
#  示例2: 
# 
#  
#  输入：0.1
#  输出："ERROR"
#  提示：0.1无法被二进制准确表示
#  
# 
#  
# 
#  提示： 
# 
#  
#  32位包括输出中的 "0." 这两位。 
#  题目保证输入用例的小数位数最多只有 6 位 
#  
# 
#  👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def printBin(self, num: float) -> str:
        """
        方法1：每次乘以2，整数部分添加到二进制表示的末尾
        """
        res = '0.'
        while len(res) <= 32 and num != 0:
            num *= 2
            digit = int(num)
            res += str(digit)
            num -= digit
        return res if num == 0 else 'ERROR'

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # num = 0.625
    # num = 0.1
    num = 0.5625
    # num = 0.015625
    result = Solution().printBin(num)
    print(result)
