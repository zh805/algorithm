# 有两种特殊字符： 
# 
#  
#  第一种字符可以用一个比特 0 来表示 
#  第二种字符可以用两个比特(10 或 11)来表示、 
#  
# 
#  给定一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一位字符，则返回 true 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: bits = [1, 0, 0]
# 输出: true
# 解释: 唯一的编码方式是一个两比特字符和一个一比特字符。
# 所以最后一个字符是一比特字符。
#  
# 
#  示例 2: 
# 
#  
# 输入: bits = [1, 1, 1, 0]
# 输出: false
# 解释: 唯一的编码方式是两比特字符和两比特字符。
# 所以最后一个字符不是一比特字符。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= bits.length <= 1000 
#  bits[i] == 0 or 1 
#  
#  Related Topics 数组 👍 237 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        方法1：顺序遍历。遇到0，i+1, 遇到 1，i+2，若遍历到最后 i=n-1,则为True。
        :param bits:
        :return:
        """
        res = False
        if bits[-1] != 0:
            return res

        bits_len = len(bits)
        i = 0
        while i < bits_len - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2

        return i == bits_len - 1

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    bits = [1, 0, 0]
    # bits = [1, 1, 1, 0]
    result = Solution().isOneBitCharacter(bits)
    print(result)
