# 你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足: 
# 
#  
#  subtexti 是 非空 字符串 
#  所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text ) 
#  对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立 
#  
# 
#  返回k可能最大值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：text = "ghiabcdefhelloadamhelloabcdefghi"
# 输出：7
# 解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。
#  
# 
#  示例 2： 
# 
#  
# 输入：text = "merchant"
# 输出：1
# 解释：我们可以把字符串拆分成 "(merchant)"。
#  
# 
#  示例 3： 
# 
#  
# 输入：text = "antaprezatepzapreanta"
# 输出：11
# 解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)"。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 1000 
#  text 仅由小写英文字符组成 
#  
# 
#  👍 76 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestDecomposition(self, text: str) -> int:
        """
        方法1：贪心+双指针
        """
        n = len(text)
        i, j = 0, n-1
        left, right = '', ''
        res = 0
        while i <= j:
            left += text[i]
            right = text[j] + right
            if i == j:
                break
            else:
                if left == right:
                    left = ''
                    right = ''
                    res += 2
            i += 1
            j -= 1
        if left != '' and right != '':
            res += 1
        return res



# leetcode submit region end(Prohibit modification and deletion)
