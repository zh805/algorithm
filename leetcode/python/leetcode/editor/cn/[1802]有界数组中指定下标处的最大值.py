# 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）： 
# 
#  
#  nums.length == n 
#  nums[i] 是 正整数 ，其中 0 <= i < n 
#  abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1 
#  nums 中所有元素之和不超过 maxSum 
#  nums[index] 的值被 最大化 
#  
# 
#  返回你所构造的数组中的 nums[index] 。 
# 
#  注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 4, index = 2,  maxSum = 6
# 输出：2
# 解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
#  
# 
#  示例 2： 
# 
#  输入：n = 6, index = 1,  maxSum = 10
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= maxSum <= 10⁹ 
#  0 <= index < n 
#  
# 
#  👍 136 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        方法1：二分查找
        """
        def sum_x(x, cnt):
            if x >= cnt:
                return (x + x - cnt + 1) * cnt // 2
            else:
                return (x + 1) * x // 2 + cnt - x

        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) >> 1
            if sum_x(mid-1, index) + sum_x(mid, n - index) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left

# leetcode submit region end(Prohibit modification and deletion)
