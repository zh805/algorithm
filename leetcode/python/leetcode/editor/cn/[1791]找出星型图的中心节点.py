# 有一个无向的 星型 图，由 n 个编号从 1 到 n 的节点组成。星型图有一个 中心 节点，并且恰有 n - 1 条边将中心节点与其他每个节点连接起来。 
# 
#  给你一个二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示在节点 ui 和 vi 之间存在一条边。请你找出并返回 edges 
# 所表示星型图的中心节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：edges = [[1,2],[2,3],[4,2]]
# 输出：2
# 解释：如上图所示，节点 2 与其他每个节点都相连，所以节点 2 是中心节点。
#  
# 
#  示例 2： 
# 
#  
# 输入：edges = [[1,2],[5,1],[1,3],[1,4]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= n <= 10⁵ 
#  edges.length == n - 1 
#  edges[i].length == 2 
#  1 <= ui, vi <= n 
#  ui != vi 
#  题目数据给出的 edges 表示一个有效的星型图 
#  
#  Related Topics 图 👍 35 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def findCenter(self, edges: List[List[int]]) -> int:
    #     """
    #     方法1：统计每个节点的度，度为n的即为中心
    #     :param edges: 
    #     :return: 
    #     """
    #     degrees = [0 for _ in range(len(edges) + 2)]
    #     for edge in edges:
    #         degrees[edge[0]] += 1
    #         degrees[edge[1]] += 1
    #     for idx, degrees in enumerate(degrees):
    #         if degrees == len(edges):
    #             return idx
    
    # def findCenter(self, edges: List[List[int]]) -> int:
    #     """
    #     方法2：中心点会出现在每个edge中
    #     :param edges:
    #     :return:
    #     """
    #     s = list(set(edges[0]) & set(edges[1]))
    #     return s[0]

    def findCenter(self, edges: List[List[int]]) -> int:
        """
        方法3：同时出现在edge[0]和edge[1]的即为中心点
        :param edges:
        :return:
        """
        return edges[0][0] if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1] else edges[0][1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [4, 2]]
    # edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
    result = Solution().findCenter(edges)
    print(result)
