/*
 * @lc app=leetcode.cn id=1637 lang=golang
 *
 * [1637] 两点之间不包含任何点的最宽垂直面积
 */

package main

import "sort"

// @lc code=start
func maxWidthOfVerticalArea(points [][]int) int {
	res := 0
	sort.Slice(points, func(i, j int) bool {
		return points[i][0] < points[j][0]
	})
	for i := 1; i < len(points); i++ {
		res = max1637(res, points[i][0]-points[i-1][0])
	}
	return res
}

func max1637(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end
