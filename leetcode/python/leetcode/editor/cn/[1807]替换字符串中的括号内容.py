# 给你一个字符串 s ，它包含一些括号对，每个括号中包含一个 非空 的键。 
# 
#  
#  比方说，字符串 "(name)is(age)yearsold" 中，有 两个 括号对，分别包含键 "name" 和 "age" 。 
#  
# 
#  你知道许多键对应的值，这些关系由二维字符串数组 knowledge 表示，其中 knowledge[i] = [keyi, valuei] ，表示键 
# keyi 对应的值为 valuei 。 
# 
#  你需要替换 所有 的括号对。当你替换一个括号对，且它包含的键为 keyi 时，你需要： 
# 
#  
#  将 keyi 和括号用对应的值 valuei 替换。 
#  如果从 knowledge 中无法得知某个键对应的值，你需要将 keyi 和括号用问号 "?" 替换（不需要引号）。 
#  
# 
#  knowledge 中每个键最多只会出现一次。s 中不会有嵌套的括号。 
# 
#  请你返回替换 所有 括号对后的结果字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
# 输出："bobistwoyearsold"
# 解释：
# 键 "name" 对应的值为 "bob" ，所以将 "(name)" 替换为 "bob" 。
# 键 "age" 对应的值为 "two" ，所以将 "(age)" 替换为 "two" 。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "hi(name)", knowledge = [["a","b"]]
# 输出："hi?"
# 解释：由于不知道键 "name" 对应的值，所以用 "?" 替换 "(name)" 。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
# 输出："yesyesyesaaa"
# 解释：相同的键在 s 中可能会出现多次。
# 键 "a" 对应的值为 "yes" ，所以将所有的 "(a)" 替换为 "yes" 。
# 注意，不在括号里的 "a" 不需要被替换。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  0 <= knowledge.length <= 10⁵ 
#  knowledge[i].length == 2 
#  1 <= keyi.length, valuei.length <= 10 
#  s 只包含小写英文字母和圆括号 '(' 和 ')' 。 
#  s 中每一个左圆括号 '(' 都有对应的右圆括号 ')' 。 
#  s 中每对括号内的键都不会为空。 
#  s 中不会有嵌套括号对。 
#  keyi 和 valuei 只包含小写英文字母。 
#  knowledge 中的 keyi 不会重复。 
#  
# 
#  👍 58 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict()
        for k in knowledge:
            d[k[0]] = k[1]

        res = ''
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '(':
                j = i
                while j < n and s[j] != ')':
                    j += 1
                key = s[i+1:j]
                if key in d:
                    res += d[key]
                else:
                    res += '?'
                i = j + 1
            else:
                res += s[i]
                i += 1

        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = "(name)is(age)yearsold"
    knowledge = [["name", "bob"], ["age", "two"]]
    result = Solution().evaluate(s, knowledge)
    print(result)
    assert result == "bobistwoyearsold"

    s = "hi(name)"
    knowledge = [["a", "b"]]
    result = Solution().evaluate(s, knowledge)
    print(result)
    assert result == "hi?"

    s = "(a)(a)(a)aaa"
    knowledge = [["a","yes"]]
    result = Solution().evaluate(s, knowledge)
    print(result)
    assert result == "yesyesyesaaa"
