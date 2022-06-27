# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
# 式重构得到原数据。 
# 
#  请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
# 反序列化为原始的树结构。 
# 
#  提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的
# 方法解决这个问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：[1]
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [1,2]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中结点数在范围 [0, 10⁴] 内 
#  -1000 <= Node.val <= 1000 
#  
#  👍 766 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # def serialize(self, root):
    #     """Encodes a tree to a single string.
    #     方法1：层序遍历
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     if not root:
    #         return ''
    #     from collections import deque
    #     ans = []
    #     d = deque()
    #     d.append(root)
    #     while d:
    #         for _ in range(len(d)):
    #             node = d.popleft()
    #             if node:
    #                 ans.append(str(node.val))
    #                 d.append(node.left)
    #                 d.append(node.right)
    #             else:
    #                 ans.append('#')
    #
    #     return ','.join(ans)
    #
    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
    #     层序遍历
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     if not data:
    #         return
    #     from collections import deque
    #     data = data.split(',')
    #     root = TreeNode(data[0])
    #     d = deque([root])
    #     i = 1
    #     while d:
    #         node = d.popleft()
    #         if data[i] != '#':
    #             node.left = TreeNode(data[i])
    #             d.append(node.left)
    #         i += 1
    #
    #         if data[i] != '#':
    #             node.right = TreeNode(data[i])
    #             d.append(node.right)
    #         i += 1
    #
    #     return root

    # def serialize(self, root):
    #     """Encodes a tree to a single string.
    #     方法2：前序遍历
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     ans = []
    #
    #     def traverse(root):
    #         if not root:
    #             ans.append('#')
    #             return
    #         ans.append(str(root.val))
    #         traverse(root.left)
    #         traverse(root.right)
    #     traverse(root)
    #     return ','.join(ans)
    #
    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
    #     前序遍历
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     from collections import deque
    #     data = data.split(',')
    #     d = deque(data)
    #
    #     def traverse(d):
    #         if not d:
    #             return
    #         first = d.popleft()
    #         if first == '#':
    #             return
    #         root = TreeNode(first)
    #         root.left = traverse(d)
    #         root.right = traverse(d)
    #         return root
    #
    #     return traverse(d)


    def serialize(self, root):
        """
        方法3: 后序遍历
        :param root:
        :return:
        """
        if not root:
            return ''

        res = []
        def traverse(root):
            if not root:
                res.append('#')
                return
            traverse(root.left)
            traverse(root.right)
            res.append(str(root.val))

        traverse(root)
        return ','.join(res)

    def deserialize(self, data):
        if not data:
            return
        data = data.split(',')
        from collections import deque
        d = deque(data)

        def traverse(d):
            if not d:
                return
            val = d.pop()
            if val == '#':
                return
            root = TreeNode(val)
            root.right = traverse(d)
            root.left = traverse(d)
            return root

        return traverse(d)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
