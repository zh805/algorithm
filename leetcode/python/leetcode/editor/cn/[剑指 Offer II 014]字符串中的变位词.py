# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。 
# 
#  换句话说，第一个字符串的排列之一是第二个字符串的 子串 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#  
# 
#  示例 2： 
# 
#  
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 10⁴ 
#  s1 和 s2 仅包含小写字母 
#  
# 
#  
# 
#  注意：本题与主站 567 题相同： https://leetcode-cn.com/problems/permutation-in-string/ 
#  Related Topics 哈希表 双指针 字符串 滑动窗口 👍 25 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import itertools


class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     """
    #     方法1：使用itertools.permutations排列出s1的所有组合; 能解，但会超时；
    #     :param s1:
    #     :param s2:
    #     :return:
    #     """
    #     if len(s1) > len(s2):
    #         return False
    #     for item in itertools.permutations(s1, len(s1)):
    #         s = ''.join(item)
    #         print(s)
    #         if s in s2:
    #             return True
    #     return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        方法2: 滑动窗口
        在s2上维护一个长度为len(s1)的滑动窗口，统计窗口内每个字符出现的次数，若和s1一样则说明变位词存在。
        :param s1:
        :param s2:
        :return:
        """
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        # 统计s1中每个字符出现的次数
        s1_list = [0 for _ in range(26)]
        for c in s1:
            idx = ord(c) - ord('a')
            s1_list[idx] += 1
        #
        # # 初始化window
        # window = [0 for _ in range(26)]
        # for c in s2[:n1]:
        #     window[ord(c) - ord('a')] += 1
        # if window == s1_list:
        #     return True
        # print('window')
        # print(window)
        #
        # for right in range(n1, n2):
        #     window[ord(s2[right - n1]) - ord('a')] -= 1
        #     window[ord(s2[right]) - ord('a')] += 1
        #     print('window')
        #     print(window)
        #     if window == s1_list:
        #         return True

        window = [0 for _ in range(26)]
        for right in range(n2):
            if right < n1:
                window[ord(s2[right]) - ord('a')] += 1
            else:
                window[ord(s2[right - n1]) - ord('a')] -= 1
                window[ord(s2[right]) - ord('a')] += 1
            if window == s1_list:
                return True

        return False
# leetcode submit region end(Prohibit modification and deletion)
