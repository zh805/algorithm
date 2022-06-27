# 给你一个下标从 0 开始的整数数组 nums ，请你找到 最左边 的中间位置 middleIndex （也就是所有可能中间位置下标最小的一个）。 
# 
#  中间位置 middleIndex 是满足 nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[
# middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1] 的数组下标。 
# 
#  如果 middleIndex == 0 ，左边部分的和定义为 0 。类似的，如果 middleIndex == nums.length - 1 ，右边部分
# 的和定义为 0 。 
# 
#  请你返回满足上述条件 最左边 的 middleIndex ，如果不存在这样的中间位置，请你返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,-1,8,4]
# 输出：3
# 解释：
# 下标 3 之前的数字和为：2 + 3 + -1 = 4
# 下标 3 之后的数字和为：4 = 4
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,-1,4]
# 输出：2
# 解释：
# 下标 2 之前的数字和为：1 + -1 = 0
# 下标 2 之后的数字和为：0
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [2,5]
# 输出：-1
# 解释：
# 不存在符合要求的 middleIndex 。
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [1]
# 输出：0
# 解释：
# 下标 0 之前的数字和为：0
# 下标 0 之后的数字和为：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  -1000 <= nums[i] <= 1000 
#  
# 
#  
# 
#  注意：本题与主站 724 题相同：https://leetcode-cn.com/problems/find-pivot-index/ 
#  👍 17 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        """
        方法1：前缀和。
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return 0

        # 正序前缀和
        pre_sum = [0 for _ in range(len(nums))]
        total = 0
        for i, num in enumerate(nums):
            total += num
            pre_sum[i] = total

        # 逆序前缀和
        pre_sum_reverse = [0 for _ in range(len(nums))]
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            total += nums[i]
            pre_sum_reverse[i] = total

        # 遍历，索引左右两侧前缀和相等则找到。
        for i in range(len(nums)):
            if i == 0:
                if pre_sum_reverse[i + 1] == 0:
                    return i
            elif i == len(nums) - 1:
                if pre_sum[i - 1] == 0:
                    return i
            else:
                if pre_sum[i - 1] == pre_sum_reverse[i + 1]:
                    return i
        return -1

    def findMiddleIndex(self, nums: List[int]) -> int:
        """
        方法2：前缀和
        前缀和  pre_sum * 2 + nums[i] = total
        :param nums:
        :return:
        """
        pre_sum, total = 0, sum(nums)
        for i in range(len(nums)):
            if pre_sum * 2 + nums[i] == total:
                return i
            pre_sum += nums[i]
        return -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [2, 3, -1, 8, 4]
    # nums = [2, 5]
    # nums = [1,-1,4]
    # nums = [2]
    # nums = [0, 0]
    result = Solution().findMiddleIndex(nums)
    print(result)
