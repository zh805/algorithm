# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。 
# 
#  如果符合下列情况之一，则数组 A 就是 锯齿数组： 
# 
#  
#  每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ... 
#  或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ... 
#  
# 
#  返回将数组 nums 转换为锯齿数组所需的最小操作次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,3]
# 输出：2
# 解释：我们可以把 2 递减到 0，或把 3 递减到 1。
#  
# 
#  示例 2： 
# 
#  输入：nums = [9,6,1,6,2]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  1 <= nums[i] <= 1000 
#  
# 
#  👍 70 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        """
        方法1：模拟，遍历
        """
        n = len(nums)
        if n == 1:
            return 0
        # 两次遍历，先让奇数位置大，再让偶数位置大，最后取最小值。
        temp1 = 0
        # 遍历偶数位置，使其小于两边
        for i in range(0, n, 2):
            if i == 0:
                m = nums[i+1]
            elif i == n-1:
                m = nums[i-1]
            else:
                m = min(nums[i-1], nums[i+1])
            if nums[i] >= m:
                temp1 += nums[i] - m + 1

        temp2 = 0
        # 遍历奇数位置，使其小于两边
        for i in range(1, n , 2):
            if i == n-1:
                m = nums[i-1]
            else:
                m = min(nums[i-1], nums[i+1])
            if nums[i] >= m:
                temp2 += nums[i] - m + 1

        return min(temp1, temp2)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # nums = [1, 2, 3]
    # nums = [9, 6, 1, 6, 2]
    # nums = [1]
    nums = [2, 2]
    result = Solution().movesToMakeZigzag(nums)
    print(result)
