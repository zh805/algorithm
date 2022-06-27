# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：5
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 19 
#  
#  Related Topics 树 二叉搜索树 数学 动态规划 二叉树 👍 1564 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTrees(self, n: int) -> int:
        """
        方法1：动态规划
        i 为root时，左子树由小于i的 [1, i-1]数字组成，右子树[i+1, n]。
        dp[i]表示0..i 组成的二叉树的个数。

        g(n)表示以n个节点组成的二叉树的个数，f(i)表示以i为根节点时二叉树的个数。
        g(n) = f(1) + f(2) + ... + f(n)   ----- (1)
        当i为根节点时，其左子树节点个数为i-1个，右子树节点个数为n-i,因此
        f(i) = g(i-1) * g(n-i)   ----- (2)
        把（2）带入（1）可得：
        g(n) = g(0)*g(n-1) + g(1)*g(n-2) + ... + g(n-1)*g(0)  ---- 卡特兰数公式
        :param n:
        :return:
        """
        # dp[i]即为g(i)，从小到大计算g
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 5
    result = Solution().numTrees(n)
    print(result)
