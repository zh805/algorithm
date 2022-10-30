# 给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。 
# 
#  返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "3z4"
# 输出: ["3z4","3Z4"]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 12 
#  s 由小写英文字母、大写英文字母和数字组成 
#  
# 
#  👍 468 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        方法1： DFS
        """
        res = []
        path = ''
        n = len(s)

        def dfs(start, path: str):
            nonlocal n
            if start == n:
                res.append(path)
                return

            ch = s[start]
            num = ord(ch)
            if 48 <= num <= 57:
                dfs(start + 1, path + ch)
            else:
                if 65 <= num <= 90:
                    # 大写的
                    dfs(start + 1, path + ch)
                    dfs(start + 1, path + chr(num + 32))
                else:
                    # 小写的
                    dfs(start + 1, path + ch)
                    dfs(start + 1, path + chr(num - 32))

        dfs(0, path)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # s = "a1b2"
    s = "3z4"
    result = Solution().letterCasePermutation(s)
    print(result)
