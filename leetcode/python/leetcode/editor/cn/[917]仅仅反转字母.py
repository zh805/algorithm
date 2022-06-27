# 给你一个字符串 s ，根据下述规则反转字符串： 
# 
#  
#  所有非英文字母保留在原有位置。 
#  所有英文字母（小写或大写）位置反转。 
#  
# 
#  返回反转后的 s 。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ab-cd"
# 输出："dc-ba"
#  
# 
#  
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#  
# 
#  
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#  
# 
#  
# 
#  提示 
# 
#  
#  1 <= s.length <= 100 
#  s 仅由 ASCII 值在范围 [33, 122] 的字符组成 
#  s 不含 '\"' 或 '\\' 
#  
#  Related Topics 双指针 字符串 👍 148 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        方法1：双指针
        :param s:
        :return:
        """
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isalpha():
                right -= 1
            if left >= right:
                break
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = "ab-cd"
    result = Solution().reverseOnlyLetters(s)
    print(result)
