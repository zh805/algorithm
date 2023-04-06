# 给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base -2）表示。 
# 
#  注意，除非字符串就是 "0"，否则返回的字符串中不能含有前导零。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出："110"
# 解释：(-2)² + (-2)¹ = 2
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 3
# 输出："111"
# 解释：(-2)² + (-2)¹ + (-2)⁰ = 3
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 4
# 输出："100"
# 解释：(-2)² = 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 10⁹ 
#  
# 
#  👍 82 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def baseNeg2(self, n: int) -> str:
        """
        方法1：模拟
        """
        k = 1
        res = []
        while n:
            if n % 2:
                res.append('1')
                n -= k
            else:
                res.append('0')
            n //= 2
            k *= -1
        return ''.join(res[::-1]) or '0'


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 2
    result = Solution().baseNeg2(n)
    print(result)
