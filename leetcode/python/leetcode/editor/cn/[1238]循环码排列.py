# 给你两个整数 n 和 start。你的任务是返回任意 (0,1,2,,...,2^n-1) 的排列 p，并且满足： 
# 
#  
#  p[0] = start 
#  p[i] 和 p[i+1] 的二进制表示形式只有一位不同 
#  p[0] 和 p[2^n -1] 的二进制表示形式也只有一位不同 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2, start = 3
# 输出：[3,2,0,1]
# 解释：这个排列的二进制表示是 (11,10,00,01)
#      所有的相邻元素都有一位是不同的，另一个有效的排列是 [3,1,0,2]
#  
# 
#  示例 2： 
# 
#  输出：n = 3, start = 2
# 输出：[2,6,7,5,4,0,1,3]
# 解释：这个排列的二进制表示是 (010,110,111,101,100,000,001,011)
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 16 
#  0 <= start < 2^n 
#  
# 
#  👍 64 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        """
        方法1：归纳法。求出的每一位与start异或
        """
        res = [start]
        for i in range(1, n + 1):
            for j in range(len(res) - 1, -1, -1):
                res.append(((res[j] ^ start) | (1 << (i - 1))) ^ start)
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    n = 2
    start = 3
    result = Solution().circularPermutation(n, start)
    print(result)
