# 给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i 
# + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [3,1,3,6]
# 输出：false
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [2,1,2,6]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：arr = [4,-2,2,-4]
# 输出：true
# 解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= arr.length <= 3 * 10⁴ 
#  arr.length 是偶数 
#  -10⁵ <= arr[i] <= 10⁵ 
#  
#  👍 97 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        """
        方法1：对每个元素计数
        奇数索引位的数字是偶数索引位的二倍。
        """
        from collections import Counter
        c = Counter(arr)
        if c[0] & 1 == 1:
            return False

        for num in sorted(c, key=abs):
            if c[num*2] < c[num]:
                return False
            c[num*2] -= c[num]
        return True




# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # arr = [3, 1, 3, 6]
    # arr = [2, 1, 2, 6]
    # arr = [4, -2, 2, -4]
    arr = [2, 4, 0, 0, 8, 1]
    result = Solution().canReorderDoubled(arr)
    print(result)
