# 给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。 
# 
#  有效的表达式需遵循以下约定： 
# 
#  
#  "t"，运算结果为 True 
#  "f"，运算结果为 False 
#  "!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT） 
#  "&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND） 
#  "|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR） 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：expression = "!(f)"
# 输出：true
#  
# 
#  示例 2： 
# 
#  输入：expression = "|(f,t)"
# 输出：true
#  
# 
#  示例 3： 
# 
#  输入：expression = "&(t,f)"
# 输出：false
#  
# 
#  示例 4： 
# 
#  输入：expression = "|(&(t,f,t),!(t))"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= expression.length <= 20000 
#  expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。 
#  expression 是以上述形式给出的有效表达式，表示一个布尔值。 
#  
# 
#  👍 160 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        """
        方法1：栈
        """
        stack = []
        for c in expression:
            if c == ',':
                continue
            if c != ')':
                stack.append(c)
                continue
            t = f = 0
            while stack[-1] != '(':
                if stack.pop() == 't':
                    t += 1
                else:
                    f += 1
            stack.pop()
            op = stack.pop()
            if op == '&':
                stack.append('t' if f == 0 else 'f')
            elif op == '|':
                stack.append('t' if t else 'f')
            elif op == '!':
                stack.append('t' if f == 1 else 'f')

        return True if stack[-1] == 't' else False



# leetcode submit region end(Prohibit modification and deletion)
