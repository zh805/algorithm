# 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 
# first = "pale"
# second = "ple"
# 输出: True 
# 
#  
# 
#  示例 2: 
# 
#  输入: 
# first = "pales"
# second = "pal"
# 输出: False
#  
#  👍 146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        """
        方法1：动态规划, 编辑距离
        """
        n1 = len(first)
        n2 = len(second)
        if abs(n1-n2) > 1:
            return False

        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        # dp[i][j]表示first[0...i] 变成 second[0...j]所需的次数
        for i in range(n1+1):
            dp[i][0] = i
        for j in range(n2+1):
            dp[0][j] = j

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if first[i-1] == second[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i-1][j],
                                   dp[i][j-1],
                                   dp[i-1][j-1]) + 1
        # print(dp)
        dis = dp[-1][-1]
        # print(dis)
        return True if dis <= 1 else False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    first = "pale"
    second = "ple"
    # first = "pales"
    # second = "pal"
    # first = "a"
    # second = "ab"
    # first = ""
    # second = "a"
    # first = "ab"
    # second = "bc"
    result = Solution().oneEditAway(first, second)
    print(result)
