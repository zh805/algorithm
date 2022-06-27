# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用 一次 。 
# 
#  注意：解集不能包含重复的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ] 
# 
#  示例 2: 
# 
#  
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
#  Related Topics 数组 回溯 👍 839 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     """
    #     方法1：回溯
    #     :param candidates:
    #     :param target:
    #     :return:
    #     """
    #     res = []
    #     candidates.sort()
    #
    #     def track_back(idx, path, target):
    #         if target < 0:
    #             return
    #         if target == 0:
    #             res.append(path[:])
    #             return
    #         for i in range(idx, len(candidates)):
    #             # 去重
    #             if i > idx and candidates[i] == candidates[i - 1]:
    #                 continue
    #             path.append(candidates[i])
    #             track_back(i + 1, path, target - candidates[i])
    #             path.pop()
    #
    #     track_back(0, [], target)
    #     return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        方法2：回溯
        """
        n = len(candidates)
        res = []
        path = []
        candidates.sort()

        def traceback(start, target_sum):
            if target_sum == target:
                res.append(path[:])
                return

            # bigger than target, stop
            if target_sum > target:
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                target_sum += candidates[i]
                path.append(candidates[i])
                traceback(i+1, target_sum)
                target_sum -= candidates[i]
                path.pop()

        traceback(0, 0)
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = Solution().combinationSum2(candidates, target)
    print(result)
