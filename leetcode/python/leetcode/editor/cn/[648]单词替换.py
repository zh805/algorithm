# 在英语中，我们有一个叫做 词根(root) 的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词
# 根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。 
# 
#  现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。你需要将句子中的所有继承词用词根替换掉。如果继
# 承词有许多可以形成它的词根，则用最短的词根替换它。 
# 
#  你需要输出替换之后的句子。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by 
# the battery"
# 输出："the cat was rat by the bat"
#  
# 
#  示例 2： 
# 
#  
# 输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# 输出："a a b c"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= dictionary.length <= 1000 
#  1 <= dictionary[i].length <= 100 
#  dictionary[i] 仅由小写字母组成。 
#  1 <= sentence.length <= 10^6 
#  sentence 仅由小写字母和空格组成。 
#  sentence 中单词的总量在范围 [1, 1000] 内。 
#  sentence 中每个单词的长度在范围 [1, 1000] 内。 
#  sentence 中单词之间由一个空格隔开。 
#  sentence 没有前导或尾随空格。 
#  
# 
#  
#  👍 164 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

    def get(self, ch):
        """
        根据ch获取孩子
        """
        return self.children[ord(ch) - ord('a')]

    def put(self, ch, node):
        """
        加入孩子
        """
        self.children[ord(ch) - ord('a')] = node

    def contain(self, ch):
        """
        是否有ch这个孩子
        """
        return self.get(ch) is not None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        把word加入前缀树
        """
        cur = self.root
        for ch in word:
            if not cur.contain(ch):
                cur.put(ch, TrieNode())
            cur = cur.get(ch)
        cur.is_end = True

    def replace(self, word):
        """
        找到word最短的词根
        """
        cur = self.root
        for idx, ch in enumerate(word):
            if not cur.contain(ch):
                return word
            cur = cur.get(ch)
            if cur.is_end:
                return word[:idx+1]
        return word


class Solution:
    # def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    #     """
    #     方法1：前缀树
    #     """
    #     trie = Trie()
    #     for word in dictionary:
    #         trie.insert(word)
    #
    #     words = sentence.split(' ')
    #     res = [trie.replace(word) for word in words]
    #     return ' '.join(res)

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        方法2: 遍历
        """
        dictionary = set(dictionary)
        sentence = sentence.split(' ')
        res = []
        for word in sentence:
            for i in range(len(word)):
                if word[:i] in dictionary:
                    res.append(word[:i])
                    break
                elif i == len(word) - 1:
                    res.append(word)
        return ' '.join(res)

# leetcode submit region end(Prohibit modification and deletion)
