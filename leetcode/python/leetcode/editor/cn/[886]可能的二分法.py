# 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。 
# 
#  给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和 bi的人归入同一组。当可以用
# 这种方法将所有人分进两组时，返回 true；否则返回 false。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, dislikes = [[1,2],[1,3],[2,4]]
# 输出：true
# 解释：group1 [1,4], group2 [2,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 3, dislikes = [[1,2],[1,3],[2,3]]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2000 
#  0 <= dislikes.length <= 10⁴ 
#  dislikes[i].length == 2 
#  1 <= dislikes[i][j] <= n 
#  ai < bi 
#  dislikes 中每一组都 不同 
#  
# 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 246 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    #     """
    #     方法1：二分图，深度优先搜索
    #     https://labuladong.gitee.io/algo/2/22/52/
    #     """
    #     graph = [[] for i in range(n)]
    #     for x, y in dislikes:
    #         graph[x - 1].append(y - 1)
    #         graph[y - 1].append(x - 1)
    #
    #     ok = True
    #     visited = [False for i in range(n)]
    #     color = [False for i in range(n)]
    #
    #     def traverse(v):
    #         nonlocal ok, graph
    #         if not ok:
    #             return
    #         visited[v] = True
    #         for w in graph[v]:
    #             if not visited[w]:
    #                 color[w] = not color[v]
    #                 traverse(w)
    #             else:
    #                 if color[w] == color[v]:
    #                     ok = False
    #                     return
    #
    #     for v in range(n):
    #         if not visited[v]:
    #             traverse(v)
    #
    #     return ok

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
        方法1：二分图，广度优先搜索
        https://labuladong.gitee.io/algo/2/22/52/
        """
        graph = [[] for i in range(n)]
        for x, y in dislikes:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        ok = True
        visited = [False for i in range(n)]
        color = [False for i in range(n)]

        def bfs(v):
            nonlocal ok
            q = list()
            visited[v] = True
            q.append(v)

            while q and ok:
                v = q.pop()
                for w in graph[v]:
                    if not visited[w]:
                        color[w] = not color[v]
                        visited[w] = True
                        q.append(w)
                    else:
                        if color[w] == color[v]:
                            ok = False
                            return

        for i in range(n):
            if not visited[i]:
                bfs(i)
        return ok


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # n = 4
    # dislikes = [[1, 2], [1, 3], [2, 4]]
    # n = 3
    # dislikes = [[1, 2], [1, 3], [2, 3]]
    n = 5
    dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    result = Solution().possibleBipartition(n, dislikes)
    print(result)
