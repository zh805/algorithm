# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  进阶： 
# 
#  
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums 是一个非递减数组 
#  -10⁹ <= target <= 10⁹ 
#  
#  👍 1581 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        方法1：二分法
        """

        def bi_left(nums, target):
            n = len(nums)
            if n == 0:
                return -1
            # 找target的开始位置
            left, right = 0, n
            while left < right:
                # 左闭右开
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid

            # 因为循环终止前left会有一个+1的动作，故其取值在[0, n]
            if left == n:
                return -1
            return left if nums[left] == target else -1

        def bi_right(nums, target):
            if len(nums) == 0:
                return -1

            # 寻找右边界
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid

            if left == 0:
                return -1
            # 因为left加过一次1后，使left==right推出了循环，所以结果中要减去1。
            return left-1 if nums[left-1] == target else -1

        return [bi_left(nums, target), bi_right(nums, target)]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 6
    nums = [2, 3]
    target = 1
    result = Solution().searchRange(nums, target)
    print(result)
