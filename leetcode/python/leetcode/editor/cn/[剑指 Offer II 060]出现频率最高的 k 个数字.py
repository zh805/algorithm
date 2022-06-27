# 给定一个整数数组 nums 和一个整数 k ，请返回其中出现频率前 k 高的元素。可以按 任意顺序 返回答案。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  k 的取值范围是 [1, 数组中不相同的元素的个数] 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的 
#  
# 
#  
# 
#  进阶：所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。 
# 
#  
# 
#  注意：本题与主站 347 题相同：https://leetcode-cn.com/problems/top-k-frequent-elements/ 
#  Related Topics 数组 哈希表 分治 桶排序 计数 快速选择 排序 堆（优先队列） 👍 18 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from typing import List


class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     """
    #     方法1: 统计频率后排序，输出最高的k个
    #     :param nums:
    #     :param k:
    #     :return:
    #     """
    #     from collections import Counter
    #     d = Counter(nums)
    #     print(d)
    #     d_s = sorted(d.items(), key=lambda item: item[1], reverse=True)
    #     print(d_s)
    #     res = [d_s[i][0] for i in range(k)]
    #     return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        方法2：统计完频次后，建立一个小顶堆，大于堆顶数字出现次数的加入堆；最后输出堆中所有元素即可。
        :param nums:
        :param k:
        :return:
        """
        from collections import Counter
        d = Counter(nums)

        # 维护一个K个节点的小顶堆
        h = []
        for num, times in d.items():
            if len(h) == k:
                if h[0][0] < times:
                    heapq.heappop(h)
                    heapq.heappush(h, (times, num))
            else:
                heapq.heappush(h, (times, num))
        print(h)
        return [item[1] for item in h]

# leetcode submit region end(Prohibit modification and deletion)
