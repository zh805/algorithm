# 给你一个嵌套的整数列表 nestedList 。每个元素要么是一个整数，要么是一个列表；该列表的元素也可能是整数或者是其他列表。请你实现一个迭代器将其扁平化
# ，使之能够遍历这个列表中的所有整数。 
# 
#  实现扁平迭代器类 NestedIterator ： 
# 
#  
#  NestedIterator(List<NestedInteger> nestedList) 用嵌套列表 nestedList 初始化迭代器。 
#  int next() 返回嵌套列表的下一个整数。 
#  boolean hasNext() 如果仍然存在待迭代的整数，返回 true ；否则，返回 false 。 
#  
# 
#  你的代码将会用下述伪代码检测： 
# 
#  
# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res 
# 
#  如果 res 与预期的扁平化列表匹配，那么你的代码将会被判为正确。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nestedList = [[1,1],2,[1,1]]
# 输出：[1,1,2,1,1]
# 解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。 
# 
#  示例 2： 
# 
#  
# 输入：nestedList = [1,[4,[6]]]
# 输出：[1,4,6]
# 解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nestedList.length <= 500 
#  嵌套列表中的整数值在范围 [-10⁶, 10⁶] 内 
#  
#  👍 417 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         """
#         方法1：实例化时就把数据解析到队列中（耗内存）
#         :param nestedList:
#         """
#         from collections import deque
#         self.data = deque()
#
#         def parse(nests):
#             # dfs, 相当于多叉树遍历
#             for nest in nests:
#                 if nest.isInteger():
#                     self.data.append(nest)
#                 else:
#                     parse(nest.getList())
#         parse(nestedList)
#
#     def next(self) -> int:
#         return self.data.popleft()
#
#     def hasNext(self) -> bool:
#         return True if len(self.data) else False


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """
        方法2：每次调用hasNext时，迭代下一个元素。
        :param nestedList:
        """
        # 使用栈，先逆序遍历存入nestedList所有元素。
        # 获取元素时，若是int则弹出；若是list则遍历压入栈
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        cur = self.stack.pop()
        return cur.getInteger()

    def hasNext(self):
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            self.stack.pop()
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.stack.append(cur.getList()[i])
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # nestedList = [[1, 1], 2, [1, 1]]
    # nestedList = [[1,1],2,[1,1]]
    nestedList = [1,[4,[6]]]

    res = []


    def parse(item):
        if isinstance(item, int):
            res.append(item)
            return
        for i in item:
            parse(i)


    parse(nestedList)
    print(res)
