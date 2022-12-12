# 一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。 
# 
#  
#  比方说，"abaacc" 的美丽值为 3 - 1 = 2 。 
#  
# 
#  给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aabcb"
# 输出：5
# 解释：美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。 
# 
#  示例 2： 
# 
#  
# 输入：s = "aabcbaa"
# 输出：17
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 只包含小写英文字母。 
#  
# 
#  👍 75 👎 0

from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def beautySum(self, s: str) -> int:
        """
        方法1：枚举计数
        """
        res, n = 0, len(s)
        for i in range(n):
            d = defaultdict(int)
            mx = 0
            for j in range(i, n):
                d[s[j]] += 1
                mx = max(mx, max(d.values()))
                res += mx - min(d.values())
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = "aabcb"
    result = Solution().beautySum(s)
    print(result)
