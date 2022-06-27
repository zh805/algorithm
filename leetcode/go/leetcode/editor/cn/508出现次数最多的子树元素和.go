//给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
//
// 一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
//
//
//
// 示例 1：
//
//
//
//
//输入: root = [5,2,-3]
//输出: [2,-3,4]
//
//
// 示例 2：
//
//
//
//
//输入: root = [5,2,-5]
//输出: [2]
//
//
//
//
// 提示:
//
//
// 节点数在 [1, 10⁴] 范围内
// -10⁵ <= Node.val <= 10⁵
//
// 👍 174 👎 0

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

import "fmt"


// 方法1，后续遍历，计算节点和
func findFrequentTreeSum(root *TreeNode) []int {
	// key为和，value为次数
	times := make(map[int]int)
	var res []int
	calcSum(root, times)
	var maxTimes int
	for k, v := range times {
		if v > maxTimes {
			maxTimes = v
			res = []int{k}
		} else if v == maxTimes {
			res = append(res, k)
		}
	}
	return res
}

func calcSum(root *TreeNode, times map[int]int) int {
	if root == nil {
		return 0
	}
	left := calcSum(root.Left, times)
	right := calcSum(root.Right, times)
	s := left + right + root.Val
	if _, ok := times[s]; ok {
		times[s]++
	} else {
		times[s] = 1
	}
	return s
}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	root := &TreeNode{
		Val:   5,
		Left:  &TreeNode{Val: 2},
		Right: &TreeNode{Val: -5},
	}
	result := findFrequentTreeSum(root)
	fmt.Println(result)
}
