# 给定一个有 n 个节点的有向无环图，用二维数组 graph 表示，请找到所有从 0 到 n-1 的路径并输出（不要求按顺序）。 
# 
#  graph 的第 i 个数组中的单元都表示有向图中 i 号节点所能到达的下一些结点（译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a ），若
# 为空，就是没有下一个节点了。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：graph = [[1,2],[3],[3],[]]
# 输出：[[0,1,3],[0,2,3]]
# 解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
# 输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
#  
# 
#  示例 3： 
# 
#  
# 输入：graph = [[1],[]]
# 输出：[[0,1]]
#  
# 
#  示例 4： 
# 
#  
# 输入：graph = [[1,2,3],[2],[3],[]]
# 输出：[[0,1,2,3],[0,2,3],[0,3]]
#  
# 
#  示例 5： 
# 
#  
# 输入：graph = [[1,3],[2],[3],[]]
# 输出：[[0,1,2,3],[0,3]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == graph.length 
#  2 <= n <= 15 
#  0 <= graph[i][j] < n 
#  graph[i][j] != i 
#  保证输入为有向无环图 (GAD) 
#  
# 
#  
# 
#  注意：本题与主站 797 题相同：https://leetcode-cn.com/problems/all-paths-from-source-to-
# target/ 
#  👍 14 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        方法1：图遍历，深度优先，回溯。
        """
        res = []
        path = [0]
        n = len(graph)

        def dfs(s):
            if s == n-1:
                res.append(path[:])
                return

            for v in graph[s]:
                path.append(v)
                dfs(v)
                path.pop()
        dfs(0)
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    graph = [[1, 2], [3], [3], []]
    result = Solution().allPathsSourceTarget(graph)
    print(result)
