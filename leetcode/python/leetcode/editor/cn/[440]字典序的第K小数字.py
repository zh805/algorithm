# 给定整数 n 和 k，返回 [1, n] 中字典序第 k 小的数字。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = 13, k = 2
# 输出: 10
# 解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
#  
# 
#  示例 2: 
# 
#  
# 输入: n = 1, k = 1
# 输出: 1
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= k <= n <= 10⁹ 
#  
#  👍 315 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def findKthNumber(self, n: int, k: int) -> int:
    #     """
    #     方法1：转换成字符串排序。会超时。
    #     """
    #     nums = [str(i) for i in range(1, n+1)]
    #     nums.sort()
    #     print(nums)
    #     return int(nums[k-1])

    def findKthNumber(self, n: int, k: int) -> int:
        """
        方法2：构造字典树，前序深度优先遍历。会超时
        """
        if n < 10:
            return k

        # 求出n是几位是，比如若n为19，则两位数最大值不超过100；n为732，三位数最大值不超过1000。
        # 最大值在遍历二叉树时使用。
        num = n
        bits = 0
        while num:
            num //= 10
            bits += 1

        max_num = 10 ** bits
        idx = 0
        res = 0

        def dfs(num):
            nonlocal res
            # 父节点为num, 求其子节点
            if num >= max_num:
                return
            if 1 <= num <= n:
                nonlocal idx
                idx += 1
                if idx == k:
                    # print(num)
                    res = num
                    return
            for i in range(10):
                pre = num * 10 + i
                dfs(pre)

        for i in range(1, 10):
            dfs(i)
            if res:
                return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = 1
    # k = 1
    # n = 13
    # k = 2
    # n = 999
    # k = 2
    # n = 10
    # k = 3
    # n = 100
    # k = 90
    # n = 4289384
    # k = 1922239
    n = 1692778
    k = 1545580
    result = Solution().findKthNumber(n, k)
    print(result)
