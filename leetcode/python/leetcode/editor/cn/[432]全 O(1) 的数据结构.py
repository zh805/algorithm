# 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。 
# 
#  实现 AllOne 类： 
# 
#  
#  AllOne() 初始化数据结构的对象。 
#  inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。 
#  dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例
# 保证：在减少计数前，key 存在于数据结构中。 
#  getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。 
#  getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", 
# "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# 输出
# [null, null, null, "hello", "hello", null, "hello", "leet"]
# 
# 解释
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "leet"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= key.length <= 10 
#  key 由小写英文字母组成 
#  测试用例保证：在每次调用 dec 时，数据结构中总存在 key 
#  最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 10⁴ 次 
#  
#  👍 151 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class AllOne:
#     """
#     方法1：只用dict存单词次数。会超时。
#     """
#     def __init__(self):
#         # key为单词，value为次数
#         self.count = dict()
#
#     def inc(self, key: str) -> None:
#         if key in self.count:
#             self.count[key] += 1
#         else:
#             self.count[key] = 1
#
#     def dec(self, key: str) -> None:
#         if self.count[key] == 1:
#             del self.count[key]
#         else:
#             self.count[key] -= 1
#
#     def getMaxKey(self) -> str:
#         if self.count:
#             return sorted(self.count.items(), key=lambda item: item[1])[-1][0]
#         else:
#             return ''
#
#     def getMinKey(self) -> str:
#         if self.count:
#             return sorted(self.count.items(), key=lambda item: item[1])[0][0]
#         else:
#             return ''

class Node:
    def __init__(self, key=None, value=None, pre=None, nex=None):
        self.key = key
        # value为字符串
        self.value = value
        self.pre = pre
        self.nex = nex


class AllOne:
    """
    方法2：双向链表+字典
    字典中key为单词，值为双向链表节点node，node中存单词次数。双向链表按从小到大顺序排列。
    """

    def __init__(self):
        self.count = dict()
        self.head = Node()
        self.tail = Node()

        self.head.nex = self.tail
        self.tail.pre = self.head

    def inc(self, key: str) -> None:
        if key in self.count:
            node = self.count[key]
            node.value += 1
            # 向后移动节点
            self.remove_node(node)
            self.move_back(node)
        else:
            node = Node(key, 1)
            self.move_to_head(node)

    def dec(self, key: str) -> None:
        node = self.count[key]
        node.value -= 1
        if node.value == 0:
            pass
        else:
            pass

    def getMaxKey(self) -> str:
        pass

    def getMinKey(self) -> str:
        pass

    def move_to_head(self, node: Node):
        # 移动节点到链表头
        node.pre = self.head
        node.nex = self.head.nex
        self.head.nex.pre = node
        self.head.nex = node

    def remove_node(self, node: Node):
        # 删除链表节点
        node.pre.next = node.nex
        node.nex.pre = node.pre

    def move_back(self, node: Node):
        # 向后移动节点
        if node.nex == self.tail or node.value <= node.nex.value:
            return
        cur = node
        while cur.nex != self.tail and cur.nex.value < node.value:
            cur = cur.nex

        node.pre = cur
        node.nex = cur.nex
        cur.nex.pre = node
        cur.nex = node

    def move_forward(self, node: Node):
        # 向前移动节点
        pass



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    allOne = AllOne()
    allOne.inc("hello")
    allOne.inc("hello")
    r = allOne.getMaxKey()  # 返回 "hello"
    print(r)
    r = allOne.getMinKey()  # 返回 "hello"
    print(r)
    allOne.inc("leet")
    r = allOne.getMaxKey()  # 返回 "hello"
    print(r)
    r = allOne.getMinKey()  # 返回 "leet"
    print(r)
