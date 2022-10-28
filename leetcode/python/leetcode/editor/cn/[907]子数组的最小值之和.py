# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。 
# 
#  由于答案可能很大，因此 返回答案模 10^9 + 7 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。 
# 
#  示例 2： 
# 
#  
# 输入：arr = [11,81,94,43,3]
# 输出：444
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 3 * 10⁴ 
#  1 <= arr[i] <= 3 * 10⁴ 
#  
# 
#  
# 
#  👍 549 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def sumSubarrayMins(self, arr: List[int]) -> int:
    #     n = len(arr)
    #     result = 0
    #     dn = [[0 for _ in range(n)] for _ in range(n)]
    #     for i in range(n):
    #         for j in range(i, n):
    #             if i == j:
    #                 dn[i][j] = arr[j]
    #                 temp = arr[j]
    #             else:
    #                 temp = min(dn[i][j-1], arr[j])
    #                 dn[i][j] = temp
    #             result += temp
    #     return result % (10 ** 9 + 7)

    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        monoStack = []
        dp = [0] * n
        ans = 0
        for i, x in enumerate(arr):
            while monoStack and arr[monoStack[-1]] > x:
                monoStack.pop()
            k = i - monoStack[-1] if monoStack else i + 1
            dp[i] = k * x + (dp[i - k] if monoStack else 0)
            ans = (ans + dp[i]) % (10 ** 9 + 7)
            monoStack.append(i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    # arr = [11, 81, 94, 43, 3]
    result = Solution().sumSubarrayMins(arr)
    print(result)
