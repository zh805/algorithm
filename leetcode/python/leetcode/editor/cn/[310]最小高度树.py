# 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。 
# 
#  给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中
#  edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。 
# 
#  可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度
# 树 。 
# 
#  请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。 
# 树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, edges = [[1,0],[1,2],[1,3]]
# 输出：[1]
# 解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。 
# 
#  示例 2： 
# 
#  
# 输入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# 输出：[3,4]
#  
# 
#  
# 
#  
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2 * 10⁴ 
#  edges.length == n - 1 
#  0 <= ai, bi < n 
#  ai != bi 
#  所有 (ai, bi) 互不相同 
#  给定的输入 保证 是一棵树，并且 不会有重复的边 
#  
#  👍 511 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    #     """
    #     方法1：计算每个节点的深度。会超时。
    #     """
    #     # 把edges先转化为邻接表
    #     graph = [[] for _ in range(n)]
    #     for edge in edges:
    #         graph[edge[0]].append(edge[1])
    #         graph[edge[1]].append(edge[0])
    #
    #     visited = [False for _ in range(n)]
    #
    #     def traverse(i, h):
    #         # 计算i为root时的树高
    #         if visited[i]:
    #             return h
    #
    #         if not graph[i]:
    #             return h
    #
    #         visited[i] = True
    #         height = []
    #         for node in graph[i]:
    #             hi = traverse(node, h + 1)
    #             height.append(hi)
    #         visited[i] = False
    #         return max(height)
    #
    #     from collections import defaultdict
    #     height_d = defaultdict(list)
    #     min_h = float('inf')
    #     for i in range(n):
    #         h = traverse(i, 0)
    #         min_h = min(h, min_h)
    #         height_d[h].append(i)
    #     # print(height_d)
    #     # print(min_h)
    #     # print(height_d[min_h])
    #     return height_d[min_h]

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        方法1：BFS。最小高度树的根节点，应该尽量靠近中间，在有非叶子节点的情况下，肯定不会是叶子结点。
        """
        res = []
        if n == 1:
            res.append(0)
            return res

        # 计算每个节点的邻接表和出度
        graph = [[] for _ in range(n)]
        degree = [0 for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1

        # 把出度为1的节点先入队列
        from collections import deque
        q = deque()
        for i, d in enumerate(degree):
            if d == 1:
                q.append(i)

        # 开始广度优先遍历
        while q:
            # res存结果，最后加入res的是最靠中间的节点。
            res = []
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                res.append(cur)

                for neighbor in graph[cur]:
                    # 遍历过cur了，所以将neighbor的出度减去1
                    degree[neighbor] -= 1
                    # 如果成为叶子节点了，就加入队列。
                    if degree[neighbor] == 1:
                        q.append(neighbor)
        return res


# leetcode submit region end(Prohibit modification and deletion)
