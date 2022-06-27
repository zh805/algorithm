# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "()"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "()[]{}"
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "(]"
# 输出：false
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "([)]"
# 输出：false
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "{[]}"
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 仅由括号 '()[]{}' 组成 
#  
#  Related Topics 栈 字符串 👍 2987 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def isValid(self, s: str) -> bool:
    #     """
    #     方法1：字符串替换
    #     :param s:
    #     :return:
    #     """
    #     n = len(s)
    #     if n == 0:
    #         return True
    #     if n % 2 != 0:
    #         return False
    #     while '()' in s or '[]' in s or '{}' in s:
    #         s = s.replace('{}', '').replace('[]', '').replace('()', '')
    #
    #     if s == '':
    #         return True
    #     else:
    #         return False

    # def isValid(self, s: str) -> bool:
    #     """
    #     方法2：栈
    #     :param s:
    #     :return:
    #     """
    #     if s is None:
    #         return True
    #     stack = []
    #     for t in s:
    #         if t == ')':
    #             try:
    #                 current = stack.pop()
    #                 if current != '(':
    #                     return False
    #             except:
    #                 return False
    #         elif t == ']':
    #             try:
    #                 current = stack.pop()
    #                 if current != '[':
    #                     return False
    #             except:
    #                 return False
    #         elif t == '}':
    #             try:
    #                 current = stack.pop()
    #                 if current != '{':
    #                     return False
    #             except:
    #                 return False
    #         else:
    #             stack.append(t)
    #     if len(stack) == 0:
    #         return True
    #     else:
    #         return False

    def isValid(self, s: str) -> bool:
        """
        方法3：栈
        :param s:
        :return:
        """
        if len(s) % 2 == 1:
            return False
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack

# leetcode submit region end(Prohibit modification and deletion)
