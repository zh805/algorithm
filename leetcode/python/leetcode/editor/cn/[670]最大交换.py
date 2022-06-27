# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。 
# 
#  示例 1 : 
# 
#  
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
#  
# 
#  示例 2 : 
# 
#  
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。
#  
# 
#  注意: 
# 
#  
#  给定数字的范围是 [0, 10⁸] 
#  
#  👍 228 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        方法1：遍历，找出最大的数字，且其不在高位，再将其和高位交换。
        :param num:
        :return:
        """
        def parse_num(num):
            # 先把num各个位上的数解析出来
            nums = []
            while num:
                nums.append(num % 10)
                num //= 10
            return nums[::-1]

        def calc(nums):
            # 把单个数字拼起来
            res = 0
            for num in nums:
                res = res * 10 + num
            return res

        nums = parse_num(num)
        n = len(nums)
        for i in range(n):
            m = max(nums[i:])
            if nums[i] != m:
                for j in range(n-1, i, -1):
                    if nums[j] == m:
                        nums[i], nums[j] = nums[j], nums[i]
                        # print(nums)
                        return calc(nums)
        return num
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # num = 2736
    # num = 9973
    # num = 2099
    # num = 0
    # num = 1
    # num = 10
    # num = 11
    num = 12
    result = Solution().maximumSwap(num)
    print(result)
