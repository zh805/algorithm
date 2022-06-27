# 实现RandomizedSet 类： 
# 
#  
#  
#  
#  RandomizedSet() 初始化 RandomizedSet 对象 
#  bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。 
#  bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。 
#  int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。 
#  
# 
#  你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。 
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", 
# "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# 输出
# [null, true, false, true, 2, true, false, 2]
# 
# 解释
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
# randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
# randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
# randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  -2³¹ <= val <= 2³¹ - 1 
#  最多调用 insert、remove 和 getRandom 函数 2 * 10⁵ 次 
#  在调用 getRandom 方法时，数据结构中 至少存在一个 元素。 
#  
#  
#  
#  👍 480 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import random


# class RandomizedSet:
#
#     def __init__(self):
#         """
#         方法1：只使用字典。能通过，效率较低。
#         数组（列表）特性：插入O（1），但是根据值删除元素需要遍历,需要O（n），通过索引访问是O(1)
#         哈希（字典）：查找、插入、删除都是O（1）
#         由于要随机返回集合中一项，需要知道集合长度。根据此来计算一个随机索引，O（1）时间访问下标获取元素。
#         """
#         self.data = dict()
#
#     def insert(self, val: int) -> bool:
#         if val not in self.data:
#             self.data[val] = val
#             return True
#         else:
#             return False
#
#     def remove(self, val: int) -> bool:
#         if val in self.data:
#             del self.data[val]
#             return True
#         else:
#             return False
#
#     def getRandom(self) -> int:
#         keys = list(self.data.keys())
#         n = len(keys)
#         idx = random.randint(0, n-1)
#         return self.data[keys[idx]]

class RandomizedSet:

    def __init__(self):
        """
        方法1：哈希+变长数组。
        字典：key为val，值为变长数组索引。可实现O（1）的插入和删除。
        变长数组：存Val。
        核心：在删除的时候，从字典找到val的index，把数组中index位置元素与末尾元素交换位置（需要在字典中更新末尾元素的index），然后删除末尾元素。
        """
        self.data = dict()
        self.values = []

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.values.append(val)
            self.data[val] = len(self.values) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        # if val in self.data:
        #     idx = self.data[val]
        #     last_val = self.values[-1]
        #     # 交换元素
        #     self.values[idx], self.values[-1] = self.values[-1], self.values[idx]
        #     # 更新字典
        #     self.data[last_val] = idx
        #     # 删除字典和数组
        #     del self.data[val]
        #     self.values.pop()
        #     return True
        # else:
        #     return False

        if val in self.data:
            idx = self.data[val]
            # 因为总要删除末尾的，所以只需把末尾元素放到idx位置即可，覆盖原有元素。
            self.values[idx] = self.values[-1]
            # 更新字典
            self.data[self.values[idx]] = idx
            # 删除字典和数组
            del self.data[val]
            self.values.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        # idx = random.randint(0, len(self.values) - 1)
        # return self.values[idx]
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    randomizedSet = RandomizedSet()
    randomizedSet.insert(1)
    randomizedSet.remove(2)
    randomizedSet.insert(2)
    randomizedSet.getRandom()
    randomizedSet.remove(1)
    randomizedSet.insert(2)
    randomizedSet.getRandom()

    print(random.randrange(1, 10, 2))
    a = [1, 2, 3, 4]
    random.shuffle(a)
    print(a)
