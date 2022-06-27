# 设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存
# 被填满时，它应该删除最近最少使用的项目。 
# 
#  它应该支持以下操作： 获取数据 get 和 写入数据 put 。 
# 
#  获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。 
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新
# 的数据值留出空间。 
# 
#  示例: 
# 
#  LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#  
#  👍 147 👎 0


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
