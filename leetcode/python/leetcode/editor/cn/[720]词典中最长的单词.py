# 给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。 
# 
#  若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：words = ["w","wo","wor","worl", "world"]
# 输出："world"
# 解释： 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。
#  
# 
#  示例 2： 
# 
#  
# 输入：words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# 输出："apple"
# 解释："apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply" 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 1000 
#  1 <= words[i].length <= 30 
#  所有输入的字符串 words[i] 都只包含小写字母。 
#  
#  👍 212 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Trie:
    def __init__(self):
        self.is_end = False
        self.nex = [None for _ in range(26)]

    def insert(self, word):
        # 单词插入前缀树
        cur = self
        for ch in word:
            if not cur.nex[ord(ch) - ord('a')]:
                cur.nex[ord(ch) - ord('a')] = Trie()
            cur = cur.nex[ord(ch) - ord('a')]
        cur.is_end = True

    def valid(self, word):
        # word是否由其他单词逐步添加一个字母组成
        cur = self
        for ch in word:
            nex = cur.nex[ord(ch) - ord('a')]
            if not nex:
                return False
            if not nex.is_end:
                return False

            cur = nex
        return True


class Solution:
    # def longestWord(self, words: List[str]) -> str:
    #     """
    #     方法1：排序+集合
    #     排序：对words排序，先按长度升序排；若长度相同，按字典序降序排。在遍历时，长的会覆盖短的，字典序小的会覆盖字典序大的。
    #     集合：集合记录遍历过的符合要求的单词。
    #     """
    #     res = ''
    #     words.sort(key=lambda w: (-len(w), w), reverse=True)
    #     # print(words)
    #     # 集合存储遍历过的单词
    #     s = {""}
    #     for w in words:
    #         if w[:-1] in s:
    #             res = w
    #             s.add(w)
    #     return res

    def longestWord(self, words: List[str]) -> str:
        """
        方法2：前缀树。
        1.构建前缀树，把所有单词加入
        2.遍历words，若单词符合要求，更新答案。
        """
        root = Trie()
        for word in words:
            root.insert(word)

        res = ''
        for w in words:
            if root.valid(w):
                if len(w) > len(res):
                    res = w
                elif len(w) == len(res):
                    res = w if w < res else res
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # words = ["w", "wo", "wor", "worl", "world"]
    # words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    words = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]
    result = Solution().longestWord(words)
    print(result)
