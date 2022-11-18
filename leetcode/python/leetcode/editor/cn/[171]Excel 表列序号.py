# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。 
# 
#  例如： 
# 
#  
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ... 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: columnTitle = "A"
# 输出: 1
#  
# 
#  示例 2: 
# 
#  
# 输入: columnTitle = "AB"
# 输出: 28
#  
# 
#  示例 3: 
# 
#  
# 输入: columnTitle = "ZY"
# 输出: 701 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= columnTitle.length <= 7 
#  columnTitle 仅由大写英文组成 
#  columnTitle 在范围 ["A", "FXSHRXW"] 内 
#  
# 
#  👍 357 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        n = len(columnTitle)
        for i in range(n):
            res += (ord(columnTitle[i]) - 64) * (26 ** (n-i-1))
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # columnTitle = "A"
    # columnTitle = "AB"
    columnTitle = "ZY"
    result = Solution().titleToNumber(columnTitle)
    print(result)
