# 给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。 
# 
#  题目保证至少有一个词不在禁用列表中，而且答案唯一。 
# 
#  禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。 
# 
#  
# 
#  示例： 
# 
#  输入: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# 输出: "ball"
# 解释: 
# "hit" 出现了3次，但它是一个禁用的单词。
# "ball" 出现了2次 (同时没有其他单词出现2次)，所以它是段落里出现次数最多的，且不在禁用列表中的单词。 
# 注意，所有这些单词在段落里不区分大小写，标点符号需要忽略（即使是紧挨着单词也忽略， 比如 "ball,"）， 
# "hit"不是最终的答案，虽然它出现次数更多，但它在禁用单词列表中。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= 段落长度 <= 1000 
#  0 <= 禁用单词个数 <= 100 
#  1 <= 禁用单词长度 <= 10 
#  答案是唯一的, 且都是小写字母 (即使在 paragraph 里是大写的，即使是一些特定的名词，答案都是小写的。) 
#  paragraph 只包含字母、空格和下列标点符号!?',;. 
#  不存在没有连字符或者带有连字符的单词。 
#  单词里只包含字母，不会出现省略号或者其他标点符号。 
#  
#  👍 127 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import re
from typing import List
from collections import defaultdict


# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         """
#         方法1：使用正则
#         """
#         ban = set(banned)
#         w_c = defaultdict(int)
#         # r = re.compile('[^a-zA-Z]')
#         r = re.compile('\W')
#         words = re.sub(r, ' ', paragraph).split(' ')
#         # words = paragraph.split(' ')
#         max_w = float('-inf')
#         res = ''
#         for word in words:
#             word = re.sub(r, '', word).lower()
#             if len(word) > 0 and word not in ban:
#                 w_c[word] += 1
#                 if w_c[word] > max_w:
#                     res = word
#                     max_w = w_c[word]
#         return res

    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #     """
    #     方法2：遍历字符
    #     """
    #     ban = set(banned)
    #     w_c = defaultdict(int)
    #     max_w = float('-inf')
    #     res = ''
    #     n = len(paragraph)
    #     i = 0
    #     while i < n:
    #         if not paragraph[i].isalpha():
    #             i += 1
    #             continue
    #         word = ''
    #         while i < n and paragraph[i].isalpha():
    #             word += paragraph[i]
    #             i += 1
    #             word = word.lower()
    #         if word not in ban:
    #             w_c[word] += 1
    #             if w_c[word] > max_w:
    #                 res = word
    #                 max_w = w_c[word]
    #     return res


class Solution:
    def digitSum(self, s: str, k: int) -> str:

        result = ''

        def trans(s):
            nonlocal result
            if len(s) <= k:
                result = s
                return

            n = len(s)
            i = 0
            res = ''
            while i < n:

                j = 0
                sum_s = 0
                while i < n and j < k:
                    sum_s += int(s[i])
                    i += 1
                    j += 1
                res += str(sum_s)
            if len(res) <= k:
                result = res
                return
            else:
                trans(res)

        trans(s)
        return result


def getIdealNums(low, high):
    # Write your code here

    t = 1
    three = [1]
    for _ in range(21):
        t *= 3
        three.append(t)
    print(three)

    f = 1
    five = [1]
    for _ in range(14):
        f *= 5
        five.append(f)
    print(five)

    total = {1}
    for t in three:
        for f in five:
            total.add(t * f)

    res = 0
    for num in range(low, high + 1):
        if num in total:
            print(num)
            res += 1

    return res


def triplets(t: int, d: List[int]):
    # traceback
    res = 0
    n = len(d)
    d.sort()

    def traceback(path: List[int], start: int, total: int):
        if len(path) == 3:
            if total <= t:
                print(path)
                nonlocal res
                res += 1
            return

        for i in range(start, n):
            num = d[i]
            path.append(num)
            total += num
            if total > t:
                path.pop()
                total -= num
                continue
            traceback(path, i + 1, total)
            path.pop()
            total -= num

    traceback([], 0, 0)
    return res


def commonPrefix(inputs):

    res = []
    for word in inputs:
        n = len(word)

        total = n
        for i in range(1, n):
            a = word[i:]
            print(a)

            j = 0
            while j < len(a) and a[j] == word[j]:
                j += 1

            total += j

        res.append(total)

    return res

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]
    # paragraph = "a, a, a, a, b,b,b,c, c"
    # banned = ["a"]
    # result = Solution().mostCommonWord(paragraph, banned)
    # print(result)

    # s = "11111222223"
    # k = 3
    # s = '1'
    # k = 2
    # result = Solution().digitSum(s, k)
    # print(result)

    # res = getIdealNums(200, 405)
    # print(res)

    t = 8
    d = [1, 2, 3, 4, 5]
    r = triplets(t, d)
    print(r)

    # inputs = ['abcabcd']
    # # inputs = ['ababaa']
    # result = commonPrefix(inputs)
    # print(result)


