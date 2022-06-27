# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。 
# 
#  如果反转后整数超过 32 位的有符号整数的范围 [−2³¹, 231 − 1] ，就返回 0。 
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 123
# 输出：321
#  
# 
#  示例 2： 
# 
#  
# 输入：x = -123
# 输出：-321
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 120
# 输出：21
#  
# 
#  示例 4： 
# 
#  
# 输入：x = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
#  Related Topics 数学 👍 3392 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def reverse(self, x: int) -> int:
    #     """
    #     方法1：字符串处理
    #     :param x: 
    #     :return: 
    #     """
    #     flag = 1 if x >= 0 else 0
    #     
    #     s = str(x).replace('-', '').strip()
    #     s_r = s[::-1]
    #     res = int(s_r) if flag else -int(s_r)
    #     if -2**31 <= res <= 2**31 - 1:
    #         return res
    #     else:
    #         return 0
        
    def reverse(self, x: int) -> int:
        """
        方法2：数学法
        :param x: 
        :return: 
        """
        # Note that in Python -1 / 10 = -1
        res, isPos = 0, 1
        if x < 0:
            isPos = -1
            x = -1 * x
        while x != 0:
            res = res * 10 + x % 10
            if res > 2147483647:
                return 0
            x = int(x/10)
        return res * isPos
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # x = 123
    # x = -123
    # x = 120
    x = 0
    res = Solution().reverse(x)
    print(res)

