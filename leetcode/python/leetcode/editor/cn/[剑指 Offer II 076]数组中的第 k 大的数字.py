# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 
# 
#  请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
# 
#  注意：本题与主站 215 题相同： https://leetcode-cn.com/problems/kth-largest-element-in-an-
# array/ 
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 👍 23 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        方法1：最小堆。
        :param nums:
        :param k:
        :return:
        """
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                if num < min_heap[0]:
                    continue
                else:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
        return min_heap[0]

class Good:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        if self.price < other.price:
            return True
        elif self.price == other.price:
            return self.name < other.name


class DataBase:
    def __init__(self):
        self.data = []

    def add(self, good):
        heapq.heappush(self.data, good)
        # self.data.append((price, name))
        # self.data.sort()
        # print(self.data)

    def get(self, idx):
        return self.data[idx].name

def getitem(entries):
    res = []
    db = DataBase()
    idx =0
    for entry in entries:
        if entry[0] == 'INSERT':
            name, price = entry[1], entry[2]
            good = Good(name, int(price))
            db.add(good)
        elif entry[0] == 'VIEW':
            name = db.get(idx)
            idx += 1
            res.append(name)
    return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    entries = [['INSERT', 'fries', 4],
               ['INSERT', 'doda', 2],
               ['VIEW'],
               ['VIEW'],
               ['INSERT', 'humb', 5],
               ['VIEW'],
               ['INSERT', 'nuggets', 4],
               ['INSERT', 'cookie', 1],
               ['VIEW'],
               ['VIEW']]

    result = getitem(entries)
    print(result)
