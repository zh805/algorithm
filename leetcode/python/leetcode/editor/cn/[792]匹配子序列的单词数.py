# 给定字符串 s 和字符串数组 words, 返回 words[i] 中是s的子序列的单词个数 。 
# 
#  字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。 
# 
#  
#  例如， “ace” 是 “abcde” 的子序列。 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcde", words = ["a","bb","acd","ace"]
# 输出: 3
# 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
#  
# 
#  Example 2: 
# 
#  
# 输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# 输出: 2
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  1 <= words.length <= 5000 
#  1 <= words[i].length <= 50 
#  words[i]和 s 都只由小写字母组成。 
#  
# 
# 
#  👍 311 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        m = len(s)

        def is_sub(word):
            n = len(word)
            if n > m:
                return False
            i, j = 0, 0
            while i < m and j < n:
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return True if j == n else False

        res = 0
        sub_set = set()
        nosub_set = set()
        for word in words:
            if word in nosub_set:
                continue
            elif word in sub_set:
                res += 1
                continue
            else:
                if is_sub(word):
                    res += 1
                    sub_set.add(word)
                else:
                    nosub_set.add(word)

        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = "abcde"
    words = ["a", "bb", "acd", "ace"]
    result = Solution().numMatchingSubseq(s, words)
    assert result == 3

    s = "dsahjpjauf"
    words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    result = Solution().numMatchingSubseq(s, words)
    assert result == 2
