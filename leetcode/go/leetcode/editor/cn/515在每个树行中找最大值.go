//给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。
//
//
//
// 示例1：
//
//
//
//
//输入: root = [1,3,2,5,3,null,9]
//输出: [1,3,9]
//
//
// 示例2：
//
//
//输入: root = [1,2,3]
//输出: [1,3]
//
//
//
//
// 提示：
//
//
// 二叉树的节点个数的范围是 [0,10⁴]
// -2³¹ <= Node.val <= 2³¹ - 1
//
//
//
// 👍 216 👎 0

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
//
//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

// 方法1：广度优先，层序遍历
//func largestValues(root *TreeNode) []int {
//	var res []int
//	if root == nil{
//		return res
//	}
//	q := []*TreeNode{root}
//	for len(q) != 0 {
//		maxVal := math.MinInt
//		var p []*TreeNode
//		for i := 0; i < len(q); i++ {
//			node := q[i]
//			if node.Val > maxVal {
//				maxVal = node.Val
//			}
//			if node.Left != nil {
//				p = append(p, node.Left)
//			}
//			if node.Right != nil {
//				p = append(p, node.Right)
//			}
//		}
//		res = append(res, maxVal)
//		q = p
//	}
//	return res
//}

// 方法2：深度优先
func largestValues(root *TreeNode) []int {
	var res []int

	var dfs func(*TreeNode, int)
	dfs = func(node *TreeNode, height int) {
		if node == nil {
			return
		}
		if height == len(res) {
			res = append(res, node.Val)
		} else {
			res[height] = max515(res[height], node.Val)
		}
		dfs(node.Left, height+1)
		dfs(node.Right, height+1)
	}

	dfs(root, 0)
	return res
}

func max515(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	root := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val:   3,
			Left:  &TreeNode{Val: 5},
			Right: &TreeNode{Val: 3},
		},
		Right: &TreeNode{
			Val:   2,
			Right: &TreeNode{Val: 9},
		},
	}
	result := largestValues(root)
	fmt.Println(result)
}
