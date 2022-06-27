# 你有一个单词列表 words 和一个模式 pattern，你想知道 words 中的哪些单词与模式匹配。 
# 
#  如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。 
# 
#  （回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。） 
# 
#  返回 words 中与给定模式匹配的单词列表。 
# 
#  你可以按任何顺序返回答案。 
# 
#  
# 
#  示例： 
# 
#  输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# 输出：["mee","aqq"]
# 解释：
# "mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
# "ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
# 因为 a 和 b 映射到同一个字母。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 50 
#  1 <= pattern.length = words[i].length <= 20 
#  
#  👍 178 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        方法1：双映射
        """
        def match(word, pat):
            w_p = {}
            p_w = {}
            for w, p in zip(word, pat):
                if w in w_p:
                    if p != w_p[w]:
                        return False
                else:
                    w_p[w] = p

                if p in p_w:
                    if w != p_w[p]:
                        return False
                else:
                    p_w[p] = w
            return True

        return [word for word in words if match(word, pattern)]


if __name__ == '__main__':
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    result = Solution().findAndReplacePattern(words, pattern)
    print(result)





# leetcode submit region end(Prohibit modification and deletion)
