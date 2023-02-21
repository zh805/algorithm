/*
 * @lc app=leetcode.cn id=1326 lang=golang
 *
 * [1326] 灌溉花园的最少水龙头数目
 */

// @lc code=start
// 方法1：贪心
package main

func minTaps(n int, ranges []int) int {
	rightMost := make([]int, n+1)
	for i := range rightMost {
		rightMost[i] = i
	}
	for i, r := range ranges {
		start := max(0, i-r)
		end := min(n, i+r)
		rightMost[start] = max(rightMost[start], end)
	}
	pre, last, ans := 0, 0, 0
	for i := 0; i < n; i++ {
		last = max(rightMost[i], last)
		if last <= i {
			return -1
		}
		if i == pre {
			ans++
			pre = last
		}
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end
