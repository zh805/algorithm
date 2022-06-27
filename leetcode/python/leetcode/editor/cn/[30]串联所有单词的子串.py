# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。 
# 
#  注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 由小写英文字母组成 
#  1 <= words.length <= 5000 
#  1 <= words[i].length <= 30 
#  words[i] 由小写英文字母组成 
#  
#  Related Topics 哈希表 字符串 滑动窗口 👍 603 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     """
    #     方法1：找出所有的word组合，在s中寻找位置。超时
    #     """
    #     from itertools import permutations
    #     res = []
    #     len_s = len(s)
    #     len_w = len(words[0]) * len(words)
    #
    #     words_p = set()
    #     # 这一步耗时太长
    #     for p in list(permutations(words)):
    #         sub = ''.join(p)
    #         words_p.add(sub)
    #
    #     for i in range(len_s - len_w + 1):
    #         if s[i:i+len_w] in words_p:
    #             res.append(i)
    #     return res

    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     """
    #     方法2: 哈希。统计每个单词出现的次数，如果一样，则相同。
    #     """
    #     res = []
    #     from collections import Counter
    #     len_s = len(s)
    #     len_one = len(words[0])
    #     len_w = sum(map(len, words))
    #     words_c = Counter(words)
    #
    #     for i in range(len_s - len_w + 1):
    #         sub_words = []
    #         for j in range(i, i + len_w, len_one):
    #             sub_words.append(s[j:j + len_one])
    #         sub_c = Counter(sub_words)
    #         if words_c == sub_c:
    #             res.append(i)
    #     return res

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        方法3：
        """





# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # s = "barfoothefoobarman"
    # words = ["foo", "bar"]
    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "word"]
    # s = "barfoofoobarthefoobarman"
    # words = ["bar", "foo", "the"]
    # s = "foobarfoobar"
    # words = ["foo", "bar"]
    s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel "
    words = ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj", "lnle", "sefg", "vimw", "bxcb"]
    result = Solution().findSubstring(s, words)
    print(result)
