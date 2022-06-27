# 给定非负整数数组 heights ，数组中的数字用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入： heights = [2,4]
# 输出： 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= heights.length <=10⁵ 
#  0 <= heights[i] <= 10⁴ 
#  
# 
#  
# 
#  注意：本题与主站 84 题相同： https://leetcode-cn.com/problems/largest-rectangle-in-
# histogram/ 
#  Related Topics 栈 数组 单调栈 👍 21 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        方法1：单调栈
        :param heights:
        :return:
        """
        stack = [-1]
        ret = 0
        for i, h in enumerate(heights):
            # 栈中高度是递增的
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ret = max(width * height, ret)
            # 当前高度的索引入栈
            stack.append(i)

        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            ret = max(width * height, ret)

        return ret
        
# leetcode submit region end(Prohibit modification and deletion)
