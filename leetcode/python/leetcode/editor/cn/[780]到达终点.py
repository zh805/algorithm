# 给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，则返回 true，否则返回 
# false。 
# 
#  从点 (x, y) 可以转换到 (x, x+y) 或者 (x+y, y)。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: sx = 1, sy = 1, tx = 3, ty = 5
# 输出: true
# 解释:
# 可以通过以下一系列转换从起点转换到终点：
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#  
# 
#  示例 2: 
# 
#  
# 输入: sx = 1, sy = 1, tx = 2, ty = 2 
# 输出: false
#  
# 
#  示例 3: 
# 
#  
# 输入: sx = 1, sy = 1, tx = 1, ty = 1 
# 输出: true
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= sx, sy, tx, ty <= 10⁹ 
#  
#  👍 146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    # def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
    #     """
    #     方法1：遍历，找出所有路径。能解，单递归深度过深，数据较大时不通过。
    #     """
    #     res = False
    #
    #     def traverse(x, y):
    #         # 尝试回溯法解决
    #         print(x, y)
    #         if x > tx or y > ty:
    #             return False
    #
    #         if x == tx and y == ty:
    #             return True
    #
    #         r1 = traverse(x, x+y)
    #         if r1:
    #             return r1
    #         r2 = traverse(x+y, y)
    #         return r2
    #
    #     res = traverse(sx, sy)
    #     return res

    # def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
    #     """
    #     方法2：层序遍历。时间复杂度过高。超时。
    #     应该需要剪枝
    #     """
    #     from collections import deque
    #     q = deque([(sx, sy)])
    #     while q:
    #         print(q)
    #         for _ in range(len(q)):
    #             x, y = q.popleft()
    #             # print(x, y)
    #             if x == tx and y == ty:
    #                 return True
    #             if x > tx or y > ty:
    #                 continue
    #
    #             q.append((x + y, y))
    #             q.append((x, x + y))
    #     return False

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """
        方法3：倒着计算
        (a, b)是由 (a-b, b)或者(a, b-a) 转化而来。
        若 a < b, 要想让a、b的大小关系转换，则要 a-n*b，直到 a < b。
        """
        while sx < tx and sy < ty and tx != ty:
            if tx < ty:
                ty %= tx
            else:
                tx %= ty

        if sx == tx and sy == ty:
            return True
        elif sx == tx:
            return sy < ty and (ty - sy) % sx == 0
        elif sy == ty:
            return sx < tx and (tx - sx) % sy == 0
        else:
            return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # sx = 1
    # sy = 1
    # tx = 3
    # ty = 5
    sx = 11
    sy = 33
    tx = 121
    ty = 198
    # sx = 3
    # sy = 3
    # tx = 12
    # ty = 9
    # sx = 35
    # sy = 13
    # tx = 455955547
    # ty = 420098884
    result = Solution().reachingPoints(sx, sy, tx, ty)
    print(result)
