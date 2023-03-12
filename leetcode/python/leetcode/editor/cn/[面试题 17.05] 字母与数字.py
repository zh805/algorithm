# 给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。 
# 
#  返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。 
# 
#  示例 1: 
# 
#  
# 输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K",
# "L","M"]
# 
# 输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
#  
# 
#  示例 2: 
# 
#  
# 输入: ["A","A"]
# 
# 输出: []
#  
# 
#  提示： 
# 
#  
#  array.length <= 100000 
#  
# 
#  👍 152 👎 0

from typing import List
from itertools import accumulate


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        """
        方法1：前缀和 + 哈希
        """
        s = list(accumulate((-1 if v[0].isdigit() else 1 for v in array), initial=0))
        begin = end = 0
        first = {}
        for i, v in enumerate(s):
            j = first.get(v, -1)
            if j < 0:
                first[v] = i
            elif i - j > end - begin:
                begin, end = j, i
        return array[begin: end]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    array = ["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L","M"]
    result = Solution().findLongestSubarray(array)
    print(result)
