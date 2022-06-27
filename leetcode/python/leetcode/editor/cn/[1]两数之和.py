# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  只会存在一个有效答案 
#  
# 
#  进阶：你可以想出一个时间复杂度小于 O(n²) 的算法吗？ 
#  Related Topics 数组 哈希表 👍 13445 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import functools
from typing import List

import time


def time_calc(func):
    @functools.wraps(func)
    def deco(*args, **kwargs):
        begin = time.perf_counter()
        print(func.__name__)
        print(*args, **kwargs)
        res = func(*args, **kwargs)
        time.sleep(1)
        cost = time.perf_counter() - begin
        print(cost)
        return res

    return deco


def singleton(cls):
    single = {}

    def get_instance(*args, **kwargs):
        if cls not in single:
            single[cls] = cls(*args, *kwargs)
        return single[cls]
    return get_instance


@singleton
class A:
    def __init__(self, x):
        self.x = x


class Solution:

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     """
    #     方法1：暴力遍历
    #     :param nums:
    #     :param target:
    #     :return:
    #     """
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        方法2：哈希
        :param nums:
        :param target:
        :return:
        """
        d = {}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [i, d[target-nums[i]]]
            else:
                d[nums[i]] = i

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    # target = 9
    nums = [3, 2, 4]
    target = 6
    result = Solution().twoSum(nums, target)
    print(result)

    # a1 = A(1)
    # print(a1.x)
    # a2 = A(2)
    # print(a2.x)
    # print(a1 == a2)
