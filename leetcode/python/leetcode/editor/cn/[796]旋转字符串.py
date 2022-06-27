# 给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。 
# 
#  s 的 旋转操作 就是将 s 最左边的字符移动到最右边。 
# 
#  
#  例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcde", goal = "cdeab"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abcde", goal = "abced"
# 输出: false
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, goal.length <= 100 
#  s 和 goal 由小写英文字母组成 
#  
#  👍 192 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def rotateString(self, s: str, goal: str) -> bool:
    #     """
    #     方法1：模拟
    #     """
    #     n = len(s)
    #     m = len(goal)
    #     if n != m:
    #         return False
    #     for i in range(n):
    #         new = s[i:n] + s[:i]
    #         # print(new)
    #         if new == goal:
    #             return True
    #     return False

    def rotateString(self, s: str, goal: str) -> bool:
        """
        方法2：判断 goal 是否为 s + s 的子串即可。
        """
        return len(s) == len(goal) and goal in s + s



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = "abcde"
    goal = "cdeab"
    result = Solution().rotateString(s, goal)
    print(result)
