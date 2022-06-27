# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。 
# 
#  找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。 
# 
#  返回容器可以储存的最大水量。 
# 
#  说明：你不能倾斜容器。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 
# 
#  示例 2： 
# 
#  
# 输入：height = [1,1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  2 <= n <= 10⁵ 
#  0 <= height[i] <= 10⁴ 
#  
#  Related Topics 贪心 数组 双指针 👍 3191 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     """
    #     方法1：暴力遍历，会超时。
    #     :param height:
    #     :return:
    #     """
    #     area = 0
    #     for i in range(len(height)):
    #         for j in range(i + 1, len(height)):
    #             area = max(area, (j - i) * min(height[i], height[j]))
    #     return area

    def maxArea(self, height: List[int]) -> int:
        """
        方法2：双指针
        左右指针初始时分别在开始和末尾，向中间靠拢。
        假设间隔为t，则area = min(l, r) * t，必须移动值小的边界才有可能时新值大于 area。
        :param height:
        :return:
        """
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return area


    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # height = [1, 1]
    result = Solution().maxArea(height)
    print(result)
