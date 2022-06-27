//给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
//
//
// 例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
//
//
// 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
//
// 返回这些数字之和。题目数据保证答案是一个 32 位 整数。
//
//
//
// 示例 1：
//
//
//输入：root = [1,0,1,0,1,0,1]
//输出：22
//解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
//
//
// 示例 2：
//
//
//输入：root = [0]
//输出：0
//
//
//
//
// 提示：
//
//
// 树中的节点数在 [1, 1000] 范围内
// Node.val 仅为 0 或 1
//
// Related Topics 树 深度优先搜索 二叉树 👍 154 👎 0

package main

//leetcode submit region begin(Prohibit modification and deletion)

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func sumRootToLeaf(root *TreeNode) int {
	return dfs(root, 0)
}

func dfs(root *TreeNode, cur int) int {
	if root == nil {
		return 0
	}

	cur = cur<<1 | root.Val

	if root.Left == nil && root.Right == nil {
		return cur
	}
	return dfs(root.Left, cur) + dfs(root.Right, cur)
}

//leetcode submit region end(Prohibit modification and deletion)

//func main() {
//	root := &TreeNode{
//		Val: 1,
//		Left: &TreeNode{
//			Val: 0,
//			Left: &TreeNode{
//				Val: 0,
//			},
//			Right: &TreeNode{
//				Val: 1,
//			},
//		},
//		Right: &TreeNode{
//			Val: 1,
//			Left: &TreeNode{
//				Val: 0,
//			},
//			Right: &TreeNode{
//				Val: 1,
//			},
//		},
//	}
//
//	result := sumRootToLeaf(root)
//	fmt.Println(result)
//
//}
