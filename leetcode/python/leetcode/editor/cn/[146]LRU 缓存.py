# 请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。 
# 
#  实现 LRUCache 类： 
# 
#  
#  
#  
#  LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存 
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
#  void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 
# key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。 
#  
# 
#  函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。 
#  
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
#  👍 2017 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class Node:
    def __init__(self, key, value, pre=None, nex=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.nex = nex


class LRUCache:
    """
    方法1：使用双向链表和字典实现。
    字典key为缓存key，value为链表节点。链表头存储最近使用的值。
    get:
    1) key不存在，返回-1
    2）key存在，找到链表中对应节点，获取值。然后把节点移动到表头。
    put
    1) key在缓存中，修改value，移动到链表头。
    2）key不在缓存中
        2.1）缓存已满，删除链表尾节点。新节点添加到表头。
        2.2）缓存未满。添加新节点到链表头。
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(0, 0, None, None)
        self.tail = Node(0, 0, None, None)
        self.head.nex = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.del_node(node)
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.del_node(node)
            self.move_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                node = self.tail.pre
                self.del_node(node)
                del self.cache[node.key]

            node = Node(key, value)
            self.cache[key] = node
            self.move_to_head(node)

    def move_to_head(self, node):
        """
        节点移动到链表头
        """
        node.nex = self.head.nex
        node.pre = self.head
        self.head.nex.pre = node
        self.head.nex = node

    def del_node(self, node: Node):
        """
        链表中删除该节点
        """
        node.pre.nex = node.nex
        node.nex.pre = node.pre


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # lRUCache = LRUCache(2)
    # lRUCache.put(1, 1)  # 缓存是 {1=1}
    # lRUCache.put(2, 2)  # 缓存是 {1=1, 2=2}
    # lRUCache.get(1)  # 返回 1
    # lRUCache.put(3, 3)  # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    # lRUCache.get(2)  # 返回 -1 (未找到)
    # lRUCache.put(4, 4)  # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    # lRUCache.get(1)  # 返回 -1 (未找到)
    # lRUCache.get(3)  # 返回 3
    # lRUCache.get(4)  # 返回 4

    lRUCache = LRUCache(1)
    lRUCache.put(2, 1)  # 缓存是 {2=1}
    r = lRUCache.get(2)
    print(r)
