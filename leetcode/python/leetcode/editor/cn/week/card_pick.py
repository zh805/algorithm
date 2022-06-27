# -*- coding: utf-8 -*-
#
# @Time           2022/5/1 10:53 AM
# @File           card_pick.py
# @Description     
# @Author         sevenhzhang
#
from typing import List


class Solution:
    # def minimumCardPickup(self, cards: List[int]) -> int:
    #     """
    #     方法1：遍历,会超时。
    #     """
    #     n = len(cards)
    #     res = float('inf')
    #     for i in range(n):
    #         s = {cards[i]}
    #         for j in range(i+1, n):
    #             if cards[j] in s:
    #                 ans = j - i + 1
    #                 res = min(res, ans)
    #     return -1 if res == float('inf') else res

    def minimumCardPickup(self, cards: List[int]) -> int:
        """
        方法2: 滑动窗口
        """
        res = float('inf')
        n = len(cards)
        left, right = 0, 0
        s = set()
        while right < n:
            card = cards[right]
            if card not in s:
                s.add(card)
                right += 1
            else:
                while cards[left] != card:
                    s.remove(cards[left])
                    left += 1
                ans = right - left + 1
                res = min(res, ans)
                left += 1
                right += 1
                s.add(card)

        return -1 if res == float('inf') else res


if __name__ == '__main__':
    # cards = [3, 4, 2, 3, 4, 7]
    # cards = [1, 0, 5, 3]
    # cards = [3, 4, 2, 3, 4, 7, 4, 3]
    # result = Solution().minimumCardPickup(cards)
    # print(result)

    a = {(1, 2)}
    b = (1,2)
    print(b in a)
