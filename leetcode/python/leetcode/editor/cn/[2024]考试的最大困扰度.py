# 一位老师正在出一场由 n 道判断题构成的考试，每道题的答案为 true （用 'T' 表示）或者 false （用 'F' 表示）。老师想增加学生对自己做出
# 答案的不确定性，方法是 最大化 有 连续相同 结果的题数。（也就是连续出现 true 或者连续出现 false）。 
# 
#  给你一个字符串 answerKey ，其中 answerKey[i] 是第 i 个问题的正确结果。除此以外，还给你一个整数 k ，表示你能进行以下操作的最
# 多次数： 
# 
#  
#  每次操作中，将问题的正确答案改为 'T' 或者 'F' （也就是将 answerKey[i] 改为 'T' 或者 'F' ）。 
#  
# 
#  请你返回在不超过 k 次操作的情况下，最大 连续 'T' 或者 'F' 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：answerKey = "TTFF", k = 2
# 输出：4
# 解释：我们可以将两个 'F' 都变为 'T' ，得到 answerKey = "TTTT" 。
# 总共有四个连续的 'T' 。
#  
# 
#  示例 2： 
# 
#  
# 输入：answerKey = "TFFT", k = 1
# 输出：3
# 解释：我们可以将最前面的 'T' 换成 'F' ，得到 answerKey = "FFFT" 。
# 或者，我们可以将第二个 'T' 换成 'F' ，得到 answerKey = "TFFF" 。
# 两种情况下，都有三个连续的 'F' 。
#  
# 
#  示例 3： 
# 
#  
# 输入：answerKey = "TTFTTFTT", k = 1
# 输出：5
# 解释：我们可以将第一个 'F' 换成 'T' ，得到 answerKey = "TTTTTFTT" 。
# 或者我们可以将第二个 'F' 换成 'T' ，得到 answerKey = "TTFTTTTT" 。
# 两种情况下，都有五个连续的 'T' 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == answerKey.length 
#  1 <= n <= 5 * 10⁴ 
#  answerKey[i] 要么是 'T' ，要么是 'F' 
#  1 <= k <= n 
#  
#  👍 52 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
    #     """
    #     方法1：滑动窗口，求包含有K个T或者K个F的最长窗口。
    #     """
    #     n = len(answerKey)
    #
    #     def maxconsecutive(ch):
    #         nonlocal n, k
    #         num = 0
    #         max_c = 0
    #         j = 0
    #         for i in range(n):
    #             if answerKey[i] == ch:
    #                 num += 1
    #
    #             while num > k:
    #                 if answerKey[j] == ch:
    #                     num -= 1
    #                 j += 1
    #             max_c = max(max_c, i - j + 1)
    #         return max_c
    #
    #     return max(maxconsecutive('T'), maxconsecutive('F'))

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """
        方法2：滑动窗口
        """
        n = len(answerKey)

        def max_consecutive(ch):
            nonlocal answerKey, k, n

            left, right = 0, 0
            ch_cnt = 0
            max_len = 0
            while right < n:
                if answerKey[right] == ch:
                    ch_cnt += 1

                while ch_cnt > k:
                    if answerKey[left] == ch:
                        ch_cnt -= 1

                    left += 1

                max_len = max(max_len, right - left + 1)

                right += 1
            return max_len

        return max(max_consecutive('T'), max_consecutive('F'))


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # answerKey = "TTFF"
    # k = 2
    answerKey = "TFFT"
    k = 1
    # answerKey = "TTFTTFTT"
    # k = 1
    result = Solution().maxConsecutiveAnswers(answerKey, k)
    print(result)
