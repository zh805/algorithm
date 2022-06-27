# 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序） 
# 
#  graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。 
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
#  
# 
#  提示： 
# 
#  
#  n == graph.length 
#  2 <= n <= 15 
#  0 <= graph[i][j] < n 
#  graph[i][j] != i（即不存在自环） 
#  graph[i] 中的所有元素 互不相同 
#  保证输入为 有向无环图（DAG） 
#  
# 
#  
#  👍 265 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    #     """
    #     方法1：图遍历
    #     """
    #     n = len(graph)
    #     res = []
    #     path = [0]
    #
    #     def dfs(s):
    #         if s == n - 1:
    #             # 到达终点
    #             res.append(path[:])
    #
    #         for v in graph[s]:
    #             # 添加节点s到路径
    #             path.append(v)
    #             dfs(v)
    #             # 移出节点s
    #             path.pop()
    #
    #     dfs(0)
    #     return res

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        方法2：图遍历
        """
        res = []
        n = len(graph)

        def traverse(i, path):
            path.append(i)
            if i == n - 1:
                res.append(path[:])
                path.pop()
                return

            for node in graph[i]:
                traverse(node, path)
            path.pop()

        traverse(0, [])
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    graph = [[1, 2], [3], [3], []]
    result = Solution().allPathsSourceTarget(graph)
    print(result)
