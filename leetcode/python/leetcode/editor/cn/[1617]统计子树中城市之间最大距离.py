# 给你 n 个城市，编号为从 1 到 n 。同时给你一个大小为 n-1 的数组 edges ，其中 edges[i] = [ui, vi] 表示城市 ui 和
#  vi 之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 树 。 
# 
#  一棵 子树 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另
# 一棵子树中不存在。 
# 
#  对于 d 从 1 到 n-1 ，请你找到城市间 最大距离 恰好为 d 的所有子树数目。 
# 
#  请你返回一个大小为 n-1 的数组，其中第 d 个元素（下标从 1 开始）是城市间 最大距离 恰好等于 d 的子树数目。 
# 
#  请注意，两个城市间距离定义为它们之间需要经过的边的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：n = 4, edges = [[1,2],[2,3],[2,4]]
# 输出：[3,4,0]
# 解释：
# 子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
# 子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
# 不存在城市间最大距离为 3 的子树。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 2, edges = [[1,2]]
# 输出：[1]
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 3, edges = [[1,2],[2,3]]
# 输出：[2,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 15 
#  edges.length == n-1 
#  edges[i].length == 2 
#  1 <= ui, vi <= n 
#  题目保证 (ui, vi) 所表示的边互不相同。 
#  
# 
#  👍 72 👎 0

from typing import List
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        方法1：二进制枚举+DFS
        """
        # 邻接表
        g = defaultdict(list)
        for u, v in edges:
            u, v = u - 1, v - 1
            g[u].append(v)
            g[v].append(u)

        def dfs(u: int, d: int = 0):
            nonlocal mx, nxt, msk
            if mx < d:
                mx, nxt = d, u
            msk ^= 1 << u
            for v in g[u]:
                if msk >> v & 1:
                    dfs(v, d + 1)

        ans = [0 for _ in range(n - 1)]
        nxt = mx = 0
        # 二进制位为1的位置表示选取此节点，枚举所有组合
        for mask in range(1, 1 << n):
            # 只有1个节点排除
            if mask & (mask - 1) == 0:
                continue
            msk, mx = mask, 0
            cur = msk.bit_length() - 1
            dfs(cur)
            if msk == 0:
                msk, mx = mask, 0
                dfs(nxt)
                ans[mx - 1] += 1

        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 4
    edges = [[1, 2], [2, 3], [2, 4]]
    result = Solution().countSubgraphsForEachDiameter(n, edges)
    print(result)
