# 在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。例如，在数组{5, 8, 4, 2, 3, 4, 6}中，{8
# , 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。 
# 
#  示例: 
# 
#  输入: [5, 3, 1, 2, 3]
# 输出: [5, 1, 3, 2, 3]
#  
# 
#  提示： 
# 
#  
#  nums.length <= 10000 
#  
#  👍 40 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        方法1：先确定数组是峰-谷-峰-谷-峰的排列方式，即偶数索引位为峰，奇数索引位为谷。
        从索引1开始遍历
        """
        for i in range(1, len(nums)):
            if i & 1 == 1:
                # 奇数索引位，应为谷。
                if nums[i - 1] >= nums[i]:
                    # 满足谷的条件
                    continue
                else:
                    # 不满足时，交换二者位置，即可。
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
            else:
                # 偶数索引位，应为封
                if nums[i - 1] <= nums[i]:
                    continue
                else:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # nums = [5, 3, 1, 2, 3]
    nums = [3, 5, 2, 1, 6, 4]
    result = Solution().wiggleSort(nums)
    print(result)
