# 正整数 n 代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
# 
#  
# 
#  注意：本题与主站 22 题相同： https://leetcode-cn.com/problems/generate-parentheses/ 
#  👍 27 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     """
    #     Method 1: traceback。Solved by myself.
    #     当位置i放置')'时，需要保证i之前已放置的'('的数量大于')'的数量。
    #     """
    #     res = []
    #     pa = ['(', ')']
    #     p_d = {
    #         '(': 0,
    #         ')': 0,
    #     }
    #
    #     def traceback(path: List[str]):
    #         if len(path) == n * 2:
    #             if p_d['('] == p_d[')']:
    #                 res.append(''.join(path))
    #             return
    #
    #         for p in pa:
    #             if p == '(':
    #                 p_d['('] += 1
    #                 path.append(p)
    #                 traceback(path)
    #                 p_d['('] -= 1
    #                 path.pop()
    #             elif p == ')':
    #                 if p_d['('] <= p_d[')']:
    #                     continue
    #                 p_d[')'] += 1
    #                 path.append(p)
    #                 traceback(path)
    #                 p_d[')'] -= 1
    #                 path.pop()
    #
    #     traceback([])
    #     return res

    def generateParenthesis(self, n: int) -> List[str]:
        """
        方法2：回溯。通过参数传递左括号和右括号的数量，然后执行不同的回溯。
        """
        res, path = [], []

        def traceback(left, right):
            if len(path) == n * 2:
                res.append(''.join(path))
                return

            if left > right:
                path.append(')')
                right += 1
                traceback(left, right)
                path.pop()
                right -= 1

            if left < n:
                path.append('(')
                left += 1
                traceback(left, right)
                path.pop()
                left -= 1

        traceback(0, 0)
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    n = 3
    result = Solution().generateParenthesis(n)
    print(result)
