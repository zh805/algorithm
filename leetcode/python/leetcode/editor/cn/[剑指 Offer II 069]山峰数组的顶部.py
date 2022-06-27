# 符合下列属性的数组 arr 称为 山峰数组（山脉数组） ： 
# 
#  
#  arr.length >= 3 
#  存在 i（0 < i < arr.length - 1）使得：
#  
#  arr[0] < arr[1] < ... arr[i-1] < arr[i] 
#  arr[i] > arr[i+1] > ... > arr[arr.length - 1] 
#  
#  
#  
# 
#  给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 
# 1] > ... > arr[arr.length - 1] 的下标 i ，即山峰顶部。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [0,1,0]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [1,3,5,4,2]
# 输出：2
#  
# 
#  示例 3： 
# 
#  
# 输入：arr = [0,10,5,2]
# 输出：1
#  
# 
#  示例 4： 
# 
#  
# 输入：arr = [3,4,5,1]
# 输出：2
#  
# 
#  示例 5： 
# 
#  
# 输入：arr = [24,69,100,99,79,78,67,36,26,19]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= arr.length <= 10⁴ 
#  0 <= arr[i] <= 10⁶ 
#  题目数据保证 arr 是一个山脉数组 
#  
# 
#  
# 
#  进阶：很容易想到时间复杂度 O(n) 的解决方案，你可以设计一个 O(log(n)) 的解决方案吗？ 
# 
#  
# 
#  注意：本题与主站 852 题相同：https://leetcode-cn.com/problems/peak-index-in-a-mountain-
# array/ 
#  Related Topics 数组 二分查找 👍 69 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #     """
    #     方法1：暴力遍历，找到数字n,其大于左右两侧数字(其实只要找到大于右侧的即可)。时间服务度O（n）
    #     :param arr:
    #     :return:
    #     """
    #     # arr_length = len(arr)
    #     # for num in range(0, arr_length - 2):
    #     #     if arr[num] < arr[num + 1] > arr[num + 2]:
    #     #         return num + 1
    #
    #     for num in range(1, len(arr) -1):
    #         if arr[num] > arr[num + 1]:
    #             return num

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        方法2：二分法
        :param arr:
        :return:
        """
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                right = mid
            else:
                left = mid

    # def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #     """
    #     方法3：骚操作，取最大值的索引
    #     :param arr:
    #     :return:
    #     """
    #     return arr.index(max(arr))

# leetcode submit region end(Prohibit modification and deletion)
