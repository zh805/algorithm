# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: num = 38
# 输出: 2 
# 解释: 各位相加的过程为：
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# 由于 2 是一位数，所以返回 2。
#  
# 
#  示例 1: 
# 
#  
# 输入: num = 0
# 输出: 0 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= num <= 2³¹ - 1 
#  
# 
#  
# 
#  进阶：你可以不使用循环或者递归，在 O(1) 时间复杂度内解决这个问题吗？ 
#  👍 426 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def addDigits(self, num: int) -> int:
    #     """
    #     方法1：遍历取各个位，相加。递归。
    #     :param num:
    #     :return:
    #     """
    #     if num < 10:
    #         return num
    # 
    #     res = 0
    #     while num:
    #         res += num % 10
    #         num = num // 10
    #     return self.addDigits(res)

    # def addDigits(self, num: int) -> int:
    #     """
    #     方法2：迭代
    #     :param num:
    #     :return:
    #     """
    #     while num >= 10:
    #         total = 0
    #         while num:
    #             total += num % 10
    #             num = num // 10
    #         num = total
    #     return num

    def addDigits(self, num: int) -> int:
        """
        方法3：数学法
        :param num:
        :return:
        """
        return (num - 1) % 9 + 1 if num else 0


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    num = 38
    result = Solution().addDigits(num)
    print(result)
