# 假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。 
# 
#  你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = [
# "Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# 输出: ["Shogun"]
# 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
#  
# 
#  示例 2: 
# 
#  
# 输入:list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["KFC",
#  "Shogun", "Burger King"]
# 输出: ["Shogun"]
# 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= list1.length, list2.length <= 1000 
#  1 <= list1[i].length, list2[i].length <= 30 
#  list1[i] 和 list2[i] 由空格 ' ' 和英文字母组成。 
#  list1 的所有字符串都是 唯一 的。 
#  list2 中的所有字符串都是 唯一 的。 
#  
#  👍 161 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    #     """
    #     方法1：暴力遍历
    #     :param list1:
    #     :param list2:
    #     :return:
    #     """
    #     res = []
    #     min_s = float('inf')
    #     for idx1, item1 in enumerate(list1):
    #         for idx2, item2 in enumerate(list2):
    #             if item1 == item2:
    #                 s = idx1 + idx2
    #                 if s < min_s:
    #                     min_s = s
    #                     res = [item1]
    #                 elif s == min_s:
    #                     res.append(item1)
    #     return res

    # def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    #     """
    #     方法2：餐厅列表转化为字典
    #     :param list1:
    #     :param list2:
    #     :return:
    #     """
    #     d1 = {item: idx for idx, item in enumerate(list1)}
    #     d2 = {item: idx for idx, item in enumerate(list2)}
    #
    #     res = []
    #     min_s = float('inf')
    #     for k, v in d1.items():
    #         if k in d2:
    #             s = v + d2[k]
    #             if s < min_s:
    #                 res = [k]
    #                 min_s = s
    #             elif s == min_s:
    #                 res.append(k)
    #     return res

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        方法3：哈希
        :param list1:
        :param list2:
        :return:
        """
        d2 = {item: idx for idx, item in enumerate(list2)}

        res = []
        min_s = float('inf')
        for idx1, item1 in enumerate(list1):
            if item1 in d2:
                s = idx1 + d2[item1]
                if s < min_s:
                    res = [item1]
                    min_s = s
                elif s == min_s:
                    res.append(item1)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    # list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    # list2 = ["KFC", "Shogun", "Burger King"]
    result = Solution().findRestaurant(list1, list2)
    print(result)
