# 给定一个不含重复数字的整数数组 nums ，返回其 所有可能的全排列 。可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
# 
#  
# 
#  注意：本题与主站 46 题相同：https://leetcode-cn.com/problems/permutations/ 
#  Related Topics 数组 回溯 👍 11 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     """
    #     方法1：内置itertools
    #     :param nums:
    #     :return:
    #     """
    #     from itertools import permutations
    #     return list(list(item) for item in permutations(nums))

    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     """
    #     方法2: 实现itertools的permutations
    #     :param nums:
    #     :return:
    #     """
    #     def permutations(iterable, r=None):
    #         pool = tuple(iterable)
    #         n = len(pool)
    #         r = n if r is None else r
    #         if r > n:
    #             return
    #         indices = list(range(n))
    #         cycles = list(range(n, n - r, -1))
    #         yield tuple(pool[i] for i in indices[:r])
    #         while n:
    #             for i in reversed(range(r)):
    #                 cycles[i] -= 1
    #                 if cycles[i] == 0:
    #                     indices[i:] = indices[i + 1:] + indices[i:i + 1]
    #                     cycles[i] = n - i
    #                 else:
    #                     j = cycles[i]
    #                     indices[i], indices[-j] = indices[-j], indices[i]
    #                     yield tuple(pool[i] for i in indices[:r])
    #                     break
    #             else:
    #                 return
    # 
    #     return list(list(item) for item in permutations(nums))

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        方法3：
        :param nums: 
        :return: 
        """



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = Solution().permute(nums)
    print(result)

