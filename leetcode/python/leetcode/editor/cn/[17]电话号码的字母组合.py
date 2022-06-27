# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  示例 2： 
# 
#  
# 输入：digits = ""
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：digits = "2"
# 输出：["a","b","c"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] 是范围 ['2', '9'] 的一个数字。 
#  
#  Related Topics 哈希表 字符串 回溯 👍 1717 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        方法1: 哈希，遍历
        :param digits:
        :return:
        """
        phone = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        if not digits:
            return res

        res.append('')
        for idx, digit in enumerate(digits):
            chars = phone[int(digit)]
            tmp = []
            for c in chars:
                for r in res:
                    tmp.append(r + c)
            res = tmp
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    digits = "23"
    result = Solution().letterCombinations(digits)
    print(result)
