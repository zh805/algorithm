# -*- coding: utf-8 -*-
#
# @Time           2022/5/1 10:42 AM
# @File           remove_digit.py
# @Description    周赛
# @Author         sevenhzhang
#

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        # 找出digit在number中的位置
        d_idx = [idx for idx, d in enumerate(number) if d == digit]
        # print(d_idx)
        res = float('-inf')
        for idx in d_idx:
            num = number[:idx] + number[idx+1:]
            res = max(res, int(num))
        return str(res)


if __name__ == '__main__':
    # number = "123"
    # digit = "3"
    # number = "1231"
    # digit = "1"
    number = "551"
    digit = "5"
    result = Solution().removeDigit(number, digit)
    print(result)
