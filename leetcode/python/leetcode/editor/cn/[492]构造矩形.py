# 作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 所以，现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下
# 要求的矩形的页面。要求： 
# 
#  
#  你设计的矩形页面必须等于给定的目标面积。 
#  宽度 W 不应大于长度 L ，换言之，要求 L >= W 。 
#  长度 L 和宽度 W 之间的差距应当尽可能小。 
#  
# 
#  返回一个 数组 [L, W]，其中 L 和 W 是你按照顺序设计的网页的长度和宽度。 
#  
# 
#  示例1： 
# 
#  
# 输入: 4
# 输出: [2, 2]
# 解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
# 但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。
#  
# 
#  示例 2: 
# 
#  
# 输入: area = 37
# 输出: [37,1]
#  
# 
#  示例 3: 
# 
#  
# 输入: area = 122122
# 输出: [427,286]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= area <= 10⁷ 
#  
#  👍 115 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math
from typing import List


class Solution:
    # def constructRectangle(self, area: int) -> List[int]:
    #     """
    #     方法1:先判断是否为素数，再除。
    #     :param area:
    #     :return:
    #     """
    #     # 判断是否是素数，是的话直接返回[area,1]
    # 
    #     def is_prime(num: int) -> bool:
    #         if num == 0 or num == 1:
    #             return False
    #         elif num == 2 or num == 3:
    #             return True
    #         elif num & 1 == 0:
    #             return False
    #         if num % 6 != 1 and num % 6 != 5:
    #             return False
    # 
    #         for i in range(5, int(num ** 0.5) + 1, 6):
    #             if (num % i == 0) or (num % (i + 2) == 0):
    #                 return False
    #         return True
    #     
    #     if is_prime(area):
    #         return [area, 1]
    # 
    #     for w in range(int(area ** 0.5), -1, -1):
    #         if area % w == 0:
    #             l = area // w
    #             return [l, w]

    def constructRectangle(self, area: int) -> List[int]:
        """
        方法2：直接除
        :param area: 
        :return: 
        """
        w = int(math.sqrt(area))
        while area % w:
            w -= 1
        return [area//w, w]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # area = 37
    # area = 122122
    area = 1
    result = Solution().constructRectangle(area)
    print(result)
