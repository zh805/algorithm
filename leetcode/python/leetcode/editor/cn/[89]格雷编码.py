# n 位格雷码序列 是一个由 2ⁿ 个整数组成的序列，其中：
#  
#  每个整数都在范围 [0, 2ⁿ - 1] 内（含 0 和 2ⁿ - 1） 
#  第一个整数是 0 
#  一个整数在序列中出现 不超过一次 
#  每对 相邻 整数的二进制表示 恰好一位不同 ，且 
#  第一个 和 最后一个 整数的二进制表示 恰好一位不同 
#  
# 
#  给你一个整数 n ，返回任一有效的 n 位格雷码序列 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：[0,1,3,2]
# 解释：
# [0,1,3,2] 的二进制表示是 [00,01,11,10] 。
# - 00 和 01 有一位不同
# - 01 和 11 有一位不同
# - 11 和 10 有一位不同
# - 10 和 00 有一位不同
# [0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
# - 00 和 10 有一位不同
# - 10 和 11 有一位不同
# - 11 和 01 有一位不同
# - 01 和 00 有一位不同
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 16 
#  
#  👍 482 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        方法1 ：镜像法
        https://baike.baidu.com/item/%E6%A0%BC%E9%9B%B7%E7%A0%81/6510858 格雷码，百度百科
        """
        res = [0]
        for i in range(n):
            m = len(res)
            for j in range(m - 1, -1, -1):
                res[j] = res[j] << 1
                res.append(res[j] + 1)
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    n = 2
    result = Solution().grayCode(n)
    print(result)
