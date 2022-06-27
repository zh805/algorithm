# 
#  运用所掌握的数据结构，设计和实现一个 LRU (Least Recently Used，最近最少使用) 缓存机制 。 
# 
#  实现 LRUCache 类： 
# 
#  
#  LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存 
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
#  void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上
# 限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 10000 
#  0 <= value <= 10⁵ 
#  最多调用 2 * 10⁵ 次 get 和 put 
#  
#  
# 
#  
# 
#  进阶：是否可以在 O(1) 时间复杂度内完成这两种操作？ 
# 
#  
# 
#  注意：本题与主站 146 题相同：https://leetcode-cn.com/problems/lru-cache/ 
#  Related Topics 设计 哈希表 链表 双向链表 👍 23 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class Node:
    def __init__(self, key, value, pre, next):
        self.key = key
        self.value = value
        self.pre_node = pre
        self.next_node = next


class LRUCache:
    """
    方法1：使用双向链表实现LRU,最新访问的数据放到链表尾（尾插法）；链表满时删除头节点。
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        # 字典存key和value，实现O（1）访问；键为key，值为node；
        self.data = {}
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, None, None)
        self.head.next_node = self.tail
        self.tail.pre_node = self.head

    def get(self, key: int) -> int:
        """
        根据key获取value
        :param key:
        :return:
        """
        if key in self.data:
            node = self.data[key]
            # 把node移动到链表头
            self.move_to_tail(key)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        存入key和value
        :param key:
        :param value:
        :return:
        """
        if key in self.data:
            # 有则更新
            node = self.data[key]
            node.value = value
            self.move_to_tail(key)
        else:
            # 无则加入
            if len(self.data) == self.capacity:
                # 容量已满，需删除首节点
                self.delete_the_first()
            node = Node(key, value, self.tail.pre_node, self.tail)
            self.tail.pre_node.next_node = node
            self.tail.pre_node = node
            self.data[key] = node

    def move_to_tail(self, key: int) -> None:
        """
        把node移动到头节点
        :param key:
        :return:
        """
        node = self.data[key]

        # 删除节点
        node.pre_node.next_node = node.next_node
        node.next_node.pre_node = node.pre_node

        # 节点放到尾部
        self.tail.pre_node.next_node = node
        node.pre_node = self.tail.pre_node
        node.next_node = self.tail
        self.tail.pre_node = node

    def delete_the_first(self) -> None:
        """
        删除头节点
        :return:
        """
        node = self.head.next_node
        del self.data[node.key]

        self.head.next_node = node.next_node
        node.next_node.pre_node = self.head


# from collections import OrderedDict
#
#
# class LRUCache:
#     """
#     方法2：python内置数据结构OrderedDict（其内置的也为一个双向链表）
#     """
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.data = OrderedDict()
#
#     def get(self, key: int) -> int:
#         if key in self.data:
#             self.data.move_to_end(key)
#             return self.data[key]
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.data:
#             self.data[key] = value
#             self.data.move_to_end(key)
#         else:
#             if len(self.data) == self.capacity:
#                 self.data.popitem(last=False)
#             self.data[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
