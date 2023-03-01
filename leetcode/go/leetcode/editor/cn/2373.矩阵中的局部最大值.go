/*
 * @lc app=leetcode.cn id=2373 lang=golang
 *
 * [2373] 矩阵中的局部最大值
 */

package main

// @lc code=start
func largestLocal(grid [][]int) [][]int {
	n := len(grid)
	res := make([][]int, n-2)
	for i := 0; i < n-2; i++ {
		row := make([]int, n-2)
		for j := 0; j < n-2; j++ {
			mx := grid[i][j]
			for a := i; a <= i+2; a++ {
				for b := j; b <= j+2; b++ {
					if grid[a][b] > mx {
						mx = grid[a][b]
					}
				}
			}
			row[j] = mx
		}
		res[i] = row
	}
	return res
}

// @lc code=end
