# 给定一组正整数，相邻的整数之间将会进行浮点除法操作。例如， [2,3,4] -> 2 / 3 / 4 。 
# 
#  但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，才能得到最大的结果，并且返回相应的字符串格式的表达式。你的表达式不应
# 该含有冗余的括号。 
# 
#  示例： 
# 
#  
# 输入: [1000,100,10,2]
# 输出: "1000/(100/10/2)"
# 解释:
# 1000/(100/10/2) = 1000/((100/10)/2) = 200
# 但是，以下加粗的括号 "1000/((100/10)/2)" 是冗余的，
# 因为他们并不影响操作的优先级，所以你需要返回 "1000/(100/10/2)"。
# 
# 其他用例:
# 1000/(100/10)/2 = 50
# 1000/(100/(10/2)) = 50
# 1000/100/10/2 = 0.5
# 1000/100/(10/2) = 2
#  
# 
#  说明: 
# 
#  
#  输入数组的长度在 [1, 10] 之间。 
#  数组中每个元素的大小都在 [2, 1000] 之间。 
#  每个测试用例只有一个最优除法解。 
#  
#  👍 117 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def optimalDivision(self, nums: List[int]) -> str:
    #     """
    #     方法1：第一个数为分母，后边的都为分子，分子尽可能小。则第二个数除以后边所有的数即可使分子最小。
    #     :param nums:
    #     :return:
    #     """
    #     length = len(nums)
    #     if length == 1:
    #         return str(nums[0])
    #     if length == 2:
    #         return '/'.join([str(num) for num in nums])
    #
    #     return str(nums[0]) + '/' + '(' + '/'.join(str(num) for num in nums[1:]) + ')'

    def optimalDivision(self, nums: List[int]) -> str:
        """
        方法1：
        :param nums:
        :return:
        """
        if len(nums) <= 2:
            return '/'.join(map(str, nums))
        else:
            # return '/'.join([str(nums[0]), '({})'.format('/'.join(map(str, nums[1:])))])
            return f'''{nums[0]}/({'/'.join(map(str, nums[1:]))})'''


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    nums = [1000, 100, 10, 2]
    result = Solution().optimalDivision(nums)
    print(result)
