# -*- coding: utf-8 -*-
#
# @Time           2022/5/1 11:26 AM
# @File           count_distinct.py
# @Description     
# @Author         sevenhzhang
#

from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """
        方法1：滑动窗口
        """
        n = len(nums)
        s = set()
        for i in range(n):
            sub = ''
            cnt = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt += 1

                if cnt <= k:
                    # 需要加逗号，不然可能会出"19"与"1"+"9"相同的情况
                    sub += ','
                    sub += str(nums[j])
                    s.add(sub)
                else:
                    break
        # print(s)
        return len(s)


if __name__ == '__main__':
    # nums = [2, 3, 3, 2, 2]
    # k = 2
    # p = 2
    # nums = [1, 2, 3, 4]
    # k = 4
    # p = 1
    nums = [1, 9, 8, 7, 19]
    k = 1
    p = 6
    result = Solution().countDistinct(nums, k, p)
    print(result)
