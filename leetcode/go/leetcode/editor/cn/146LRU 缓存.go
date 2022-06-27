//请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。
//
// 实现 LRUCache 类：
//
//
//
//
// LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
// int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
// void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组
//key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
//
//
// 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
//
//
//
//
//
// 示例：
//
//
//输入
//["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
//[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
//输出
//[null, null, null, 1, null, -1, null, -1, 3, 4]
//
//解释
//LRUCache lRUCache = new LRUCache(2);
//lRUCache.put(1, 1); // 缓存是 {1=1}
//lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
//lRUCache.get(1);    // 返回 1
//lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
//lRUCache.get(2);    // 返回 -1 (未找到)
//lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
//lRUCache.get(1);    // 返回 -1 (未找到)
//lRUCache.get(3);    // 返回 3
//lRUCache.get(4);    // 返回 4
//
//
//
//
// 提示：
//
//
// 1 <= capacity <= 3000
// 0 <= key <= 10000
// 0 <= value <= 10⁵
// 最多调用 2 * 10⁵ 次 get 和 put
//
// 👍 2220 👎 0

package main

import (
	"fmt"
)

//leetcode submit region begin(Prohibit modification and deletion)

type DLNode struct {
	key, val  int
	pre, next *DLNode
}

func DLConstructor(key, val int) *DLNode {
	return &DLNode{
		key: key,
		val: val,
	}
}

type LRUCache struct {
	capacity int
	data     map[int]*DLNode
	head     *DLNode
	tail     *DLNode
}

func LruConstructor(capacity int) LRUCache {
	l := LRUCache{
		capacity: capacity,
		data:     map[int]*DLNode{},
		head:     DLConstructor(0, 0),
		tail:     DLConstructor(0, 0),
	}
	l.head.next = l.tail
	l.tail.pre = l.head
	return l
}

func (this *LRUCache) Get(key int) int {
	node, ok := this.data[key]
	if ok {
		//	如果key在
		this.MoveToHead(node)
		return node.val
	} else {
		return -1
	}
}

func (this *LRUCache) Put(key int, val int) {
	node, ok := this.data[key]
	if ok {
		//	key已存在，移动到链表头，更新val
		node.val = val
		this.MoveToHead(node)
	} else {
		// key不存在
		// node放入缓存
		node = DLConstructor(key, val)
		this.data[key] = node
		// 移动节点到链表头
		this.AddToHead(node)

		// 缓存已经满，删除链表尾节点，删除字典键
		if len(this.data) > this.capacity {
			delNode := this.tail.pre
			delete(this.data, delNode.key)
			this.DelNode(delNode)
		}
	}
}

// AddToHead 节点放头部
func (this *LRUCache) AddToHead(node *DLNode) {
	node.pre = this.head
	node.next = this.head.next
	this.head.next.pre = node
	this.head.next = node
}

// MoveToHead 把链表节点移动到链表头
func (this *LRUCache) MoveToHead(node *DLNode) {
	this.DelNode(node)
	this.AddToHead(node)
}

// DelNode 删除链表节点
func (this *LRUCache) DelNode(node *DLNode) {
	node.pre.next = node.next
	node.next.pre = node.pre
	//node.pre = nil
	//node.next = nil
}

func (this *LRUCache) PrintListValue() {
	var arr []int
	cur := this.head
	for cur != this.tail {
		cur = cur.next
		arr = append(arr, cur.val)
	}
	fmt.Printf("arr: %v\n", arr)
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
//leetcode submit region end(Prohibit modification and deletion)

func main() {

	lRUCache := LruConstructor(2)
	lRUCache.Put(1, 1)
	lRUCache.Put(1, 1) // 缓存是 {1=1}
	lRUCache.Put(2, 2) // 缓存是 {1=1, 2=2}
	lRUCache.PrintListValue()

	r1 := lRUCache.Get(1) // 返回 1
	lRUCache.PrintListValue()
	fmt.Println(r1)
	lRUCache.Put(3, 3)    // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
	r2 := lRUCache.Get(2) // 返回 -1 (未找到)
	fmt.Println(r2)
	lRUCache.Put(4, 4)    // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
	r3 := lRUCache.Get(1) // 返回 -1 (未找到)
	fmt.Println(r3)
	r4 := lRUCache.Get(3) // 返回 3
	fmt.Println(r4)
	r5 := lRUCache.Get(4) // 返回 4
	fmt.Println(r5)
	lRUCache.PrintListValue()
}
