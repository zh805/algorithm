//给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
//
// 假设二叉树中至少有一个节点。
//
//
//
// 示例 1:
//
//
//
//
//输入: root = [2,1,3]
//输出: 1
//
//
// 示例 2:
//
//
//
//
//输入: [1,2,3,4,null,5,6,null,null,7]
//输出: 7
//
//
//
//
// 提示:
//
//
// 二叉树的节点个数的范围是 [1,10⁴]
// -2³¹ <= Node.val <= 2³¹ - 1
//
// 👍 303 👎 0

//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

package main

import (
	"fmt"
)

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

// 方法1：广度优先，层序遍历。
// 每层从右向左遍历，遍历到的最后一个节点即是所求。
//func findBottomLeftValue(root *TreeNode) int {
//	var res int
//	q := []*TreeNode{root}
//	for len(q) > 0 {
//		node := q[0]
//		q = q[1:]
//		if node.Right != nil {
//			q = append(q, node.Right)
//		}
//		if node.Left != nil {
//			q = append(q, node.Left)
//		}
//		res = node.Val
//	}
//	return res
//}

// 深度优先
func findBottomLeftValue(root *TreeNode) int {

	var res, maxDepth int
	var dfs func(*TreeNode, int)
	dfs = func(node *TreeNode, depth int) {
		if node == nil {
			return
		}
		if depth > maxDepth {
			maxDepth = depth
			res = node.Val
		}
		dfs(node.Left, depth+1)
		dfs(node.Right, depth+1)
	}
	dfs(root, 1)
	return res
}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	root := &TreeNode{
		Val:   2,
		Left:  &TreeNode{Val: 1},
		Right: &TreeNode{Val: 3},
	}
	result := findBottomLeftValue(root)
	fmt.Println(result)
}
