# 给定两个数组，arr1 和 arr2， 
# 
#  
#  arr2 中的元素各不相同 
#  arr2 中的每个元素都出现在 arr1 中 
#  
# 
#  对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末
# 尾。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr1.length, arr2.length <= 1000 
#  0 <= arr1[i], arr2[i] <= 1000 
#  arr2 中的元素 arr2[i] 各不相同 
#  arr2 中的每个元素 arr2[i] 都出现在 arr1 中 
#  
# 
#  
# 
#  注意：本题与主站 1122 题相同：https://leetcode-cn.com/problems/relative-sort-array/ 
#  Related Topics 数组 哈希表 计数排序 排序 👍 15 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        方法1：计数排序
        :param arr1:
        :param arr2:
        :return:
        """
        count_list = [0 for _ in range(1001)]
        # 计数列表，统计arr1中每个元素出现的次数
        for num in arr1:
            count_list[num] += 1
        res = []
        for num in arr2:
            # 在arr2中出现的元素，先按顺序放入res
            res.extend(num for _ in range(count_list[num]))

        for idx, times in enumerate(count_list):
            if idx in arr2:
                continue
            # 按顺序放入不在arr2中出现的元素
            res.extend([idx for _ in range(times)])
        return res

# leetcode submit region end(Prohibit modification and deletion)
