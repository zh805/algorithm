# 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: num = 100
# 输出: "202"
#  
# 
#  示例 2: 
# 
#  
# 输入: num = -7
# 输出: "-10"
#  
# 
#  
# 
#  提示： 
# 
#  
#  -10⁷ <= num <= 10⁷ 
#  
#  👍 134 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        方法1：除法取余
        :param num: 
        :return: 
        """
        if num == 0:
            return '0'

        flag = 1 if num > 0 else 0
        res = []
        num = abs(num)
        while num:
            res.append(str(num % 7))
            num = num // 7
        return ''.join(res[::-1]) if flag else '-'+''.join(res[::-1])
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    num = 100
    # num = -7
    # num = 30
    result = Solution().convertToBase7(num)
    print(result)
