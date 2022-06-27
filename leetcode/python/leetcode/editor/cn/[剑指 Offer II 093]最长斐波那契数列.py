# 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的： 
# 
#  
#  n >= 3 
#  对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2} 
#  
# 
#  给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回 0 。 
# 
#  （回想一下，子序列是从原序列 arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 
# 是 [3, 4, 5, 6, 7, 8] 的一个子序列） 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入: arr = [1,2,3,4,5,6,7,8]
# 输出: 5
# 解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。
#  
# 
#  示例 2： 
# 
#  
# 输入: arr = [1,3,7,11,12,14,18]
# 输出: 3
# 解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= arr.length <= 1000 
#  
#  1 <= arr[i] < arr[i + 1] <= 10^9 
#  
#  
# 
#  
# 
#  注意：本题与主站 873 题相同： https://leetcode-cn.com/problems/length-of-longest-
# fibonacci-subsequence/ 
#  👍 29 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        Method 1: Dynamic Programming + Hash, O(N^2)
        A[i] = A[j] + A[k], i > j > k
        dp[i][j] means the number of fib subsequences when choose A[i] and A[j]
        when we know A[i] and A[j], wo should find (A[i]-A[j]) if exists in arr, dict is useful.
        """
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        data = {}
        for idx, num in enumerate(arr):
            data[num] = idx

        res = 0
        for i in range(1, n):
            for j in range(i):
                diff = arr[i] - arr[j]
                if diff in data and data[diff] < j:
                    # found k
                    k = data[diff]
                    dp[i][j] = dp[j][k] + 1
                else:
                    # not found k, dp[i][j] = 2, because when we calculate A[x] (x > i), A[x] = A[i][j] + 1,
                    # A[x] should be 3.
                    dp[i][j] = 2
                res = max(res, dp[i][j])

        return res if res > 2 else 0

    # def lenLongestFibSubseq(self, arr: List[int]) -> int:
    #     """
    #     Method 1: Dynamic Programming + Binary Search . N^2logN, time limit exceeded.
    #     A[i] = A[j] + A[k], i > j > k
    #     dp[i][j] means the number of fib subsequences when choose A[i] and A[j]
    #     when we know A[i] and A[j], wo should find (A[i]-A[j]) if exists in arr, bisect is useful.
    #     """
    #     n = len(arr)
    #     dp = [[0 for _ in range(n)] for _ in range(n)]
    #
    #     def find(target, right):
    #         left = 0
    #         while left <= right:
    #             mid = left + (right - left) // 2
    #             if arr[mid] == target:
    #                 return mid
    #             if arr[mid] > target:
    #                 right = mid - 1
    #             elif arr[mid] < target:
    #                 left = mid + 1
    #         return -1
    #
    #     res = 0
    #     for i in range(1, n):
    #         for j in range(i):
    #             diff = arr[i] - arr[j]
    #
    #             idx = find(diff, j-1)
    #             if idx != -1:
    #                 # found k
    #                 dp[i][j] = dp[j][idx] + 1
    #             else:
    #                 # not found k, dp[i][j] = 2, because when we calculate A[x] (x > i), A[x] = A[i][j] + 1,
    #                 # A[x] should be 3.
    #                 dp[i][j] = 2
    #             res = max(res, dp[i][j])
    #
    #     return res if res > 2 else 0


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # arr = [1, 3, 7, 11, 12, 14, 18]
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    result = Solution().lenLongestFibSubseq(arr)
    print(result)
