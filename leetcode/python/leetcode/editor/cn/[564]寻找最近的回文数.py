# 给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。 
# 
#  “最近的”定义为两个整数差的绝对值最小。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = "123"
# 输出: "121"
#  
# 
#  示例 2: 
# 
#  
# 输入: n = "1"
# 输出: "0"
# 解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= n.length <= 18 
#  n 只由数字组成 
#  n 不含前导 0 
#  n 代表在 [1, 10¹⁸ - 1] 范围内的整数 
#  
#  👍 135 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """
        方法1：暴力遍历,会超时
        从n开始向两边扩散，判断是否是回文字符串
        :param n:
        :return:
        """
        def is_palindromic(num):
            # nums = []
            # while num:
            #     a = num % 10
            #     num = num // 10
            #     nums.append(a)
            # return nums == nums[::-1]

            return str(num) == str(num)[::-1]

        n = int(n)
        for i in range(1, n + 1):
            if is_palindromic(n-i):
                return str(n-i)
            if is_palindromic(n+i):
                return str(n+i)

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = "123"
    # n = '1'
    # n = '1631716361'
    n = '807045053224792883'
    result = Solution().nearestPalindromic(n)
    print(result)
