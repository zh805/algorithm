# 在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能
# 围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# 输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# 解释:
# 
#  
# 
#  示例 2: 
# 
#  输入: [[1,2],[2,2],[4,2]]
# 输出: [[1,2],[2,2],[4,2]]
# 解释:
# 
# 即使树都在一条直线上，你也需要先用绳子包围它们。
#  
# 
#  
# 
#  注意: 
# 
#  
#  所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。 
#  输入的整数在 0 到 100 之间。 
#  花园至少有一棵树。 
#  所有树的坐标都是不同的。 
#  输入的点没有顺序。输出顺序也没有要求。 
#  👍 164 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:

        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        leftMost = 0
        for i, tree in enumerate(trees):
            if tree[0] < trees[leftMost][0]:
                leftMost = i

        ans = []
        vis = [False] * n
        p = leftMost
        while True:
            q = (p + 1) % n
            for r, tree in enumerate(trees):
                # 如果r在pq的右侧，则q=r
                if cross(trees[p], trees[q], tree) < 0:
                    q = r
            # 是否存在点i, 使p，q，i在同一条直线
            for i, b in enumerate(vis):
                if not b and i != p and i != q and cross(trees[p], trees[q], trees[i]) == 0:
                    ans.append(trees[i])
                    vis[i] = True

            if not vis[q]:
                ans.append(trees[q])
                vis[q] = True

            p = q
            if p == leftMost:
                break
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    trees = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
    result = Solution().outerTrees(trees)
    print(result)
