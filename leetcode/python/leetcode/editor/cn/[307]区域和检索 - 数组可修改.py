# 给你一个数组 nums ，请你完成两类查询。 
# 
#  
#  其中一类查询要求 更新 数组 nums 下标对应的值 
#  另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right 
#  
# 
#  实现 NumArray 类： 
# 
#  
#  NumArray(int[] nums) 用整数数组 nums 初始化对象 
#  void update(int index, int val) 将 nums[index] 的值 更新 为 val 
#  int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元
# 素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]） 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# 输出：
# [null, 9, null, 8]
# 
# 解释：
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -100 <= nums[i] <= 100 
#  0 <= index < nums.length 
#  -100 <= val <= 100 
#  0 <= left <= right < nums.length 
#  调用 pdate 和 sumRange 方法次数不大于 3 * 10⁴ 
#  
#  👍 362 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        size = int(n ** 0.5)
        sums = [0] * ((n + size - 1) // size)  # n/size 向上取整
        for i, num in enumerate(nums):
            sums[i // size] += num
        self.nums = nums
        self.sums = sums
        self.size = size

    def update(self, index: int, val: int) -> None:
        self.sums[index // self.size] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        m = self.size
        b1, b2 = left // m, right // m
        if b1 == b2:  # 区间 [left, right] 在同一块中
            return sum(self.nums[left:right + 1])
        return sum(self.nums[left:(b1 + 1) * m]) + sum(self.sums[b1 + 1:b2]) + sum(self.nums[b2 * m:right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # [[1, 3, 5]], [0, 2], [1, 2], [0, 2]
    numArray = NumArray([1, 3, 5])
    r1 = numArray.sumRange(0, 2)
    print(r1)
    numArray.update(1, 2)
    r2 = numArray.sumRange(0, 2)
    print(r2)
