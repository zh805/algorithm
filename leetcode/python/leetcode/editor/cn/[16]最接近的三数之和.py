# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。 
# 
#  返回这三个数的和。 
# 
#  假定每组输入只存在恰好一个解。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,0], target = 1
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 1000 
#  -1000 <= nums[i] <= 1000 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics 数组 双指针 排序 👍 1046 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        方法1：排序后，双指针
        :param nums:
        :param target:
        :return:
        """
        ls = len(nums)
        sort_nums = sorted(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(ls-2):
            j = i + 1
            k = ls -1
            while j < k:
                temp = sort_nums[i] + sort_nums[j] + sort_nums[k]
                if abs(target - temp) < abs(target - res):
                    res = temp
                if temp < target:
                    j += 1
                else:
                    k -= 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
